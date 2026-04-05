"""
Event Handler: Theo dõi sự kiện, trigger agent phù hợp
"""


from agents.support_agent import SupportAgent
from agents.main_agent import MainAgent
from agents.director_local_agent import DirectorLocalAgent
from agents.director_global_agent import DirectorGlobalAgent

class EventHandler:
    def __init__(self, queue_manager, state_manager, rag_manager, persona):
        self.queue_manager = queue_manager
        self.state_manager = state_manager
        self.rag_manager = rag_manager
        self.persona = persona
        # Khởi tạo agent với cognitive_layers
        self.support_agent = SupportAgent(state_manager, persona)
        self.main_agent = MainAgent(state_manager, persona, rag_manager)
        self.director_local_agent = DirectorLocalAgent(state_manager)
        self.director_global_agent = DirectorGlobalAgent(state_manager)

    def handle_event(self, event):
        """
        Tổng quát pipeline:
        1. Nhận event (user_message, system_event...)
        2. Nếu là user_message:
            - Gọi SupportAgent xử lý intent, cập nhật state
            - Gọi DirectorLocalAgent kiểm tra trạng thái, gửi chỉ thị nếu cần
            - Gọi MainAgent sinh phản hồi
        3. Nếu là tổng hợp (end_simulation):
            - Gọi DirectorGlobalAgent tổng hợp feedback
        """
        event_type = event.get("type")
        session_id = event.get("session_id")
        user_input = event.get("user_input")
        short_history = event.get("short_history", [])

        if event_type == "user_message":
            # 1. Support Agent xử lý intent, cập nhật state
            self.support_agent.process(user_input, short_history)
            # 2. Director Local Agent kiểm tra trạng thái, gửi chỉ thị nếu cần
            state = self.state_manager.get_state(session_id)
            chat_history = state.get("chat_history", []) if state else []
            self.director_local_agent.monitor_and_intervene(state, chat_history)
            # 3. Main Agent sinh phản hồi
            context_payload = {
                "user_input": user_input,
                "state": state,
                "persona": self.persona
            }
            response = self.main_agent.generate_response(context_payload)
            return response
        elif event_type == "end_simulation":
            # Tổng hợp feedback cuối cùng
            all_states = event.get("all_states", [])
            all_histories = event.get("all_histories", [])
            feedback = self.director_global_agent.aggregate_and_feedback(all_states, all_histories)
            return feedback
        else:
            # Các loại event khác
            return None
