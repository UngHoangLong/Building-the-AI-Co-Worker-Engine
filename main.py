"""
Entry point: Khởi tạo hệ thống, load persona, tạo agent, ví dụ flow message
"""
from data.cognitive_layers import CognitiveLayers
from data.state_manager import StateManager
from data.rag_manager import RAGManager
from orchestration.queue_manager import QueueManager
from orchestration.event_handler import EventHandler

# Khởi tạo các thành phần chính
persona_path = "data/persona_schema/ceo.json"
cognitive_layers = CognitiveLayers(persona_path)
state_manager = StateManager()
rag_manager = RAGManager(vector_db_client=None)  # Placeholder
queue_manager = QueueManager()

# Khởi tạo event handler (trung tâm điều phối)
event_handler = EventHandler(
    queue_manager=queue_manager,
    state_manager=state_manager,
    rag_manager=rag_manager,
    persona=cognitive_layers
)

# Ví dụ flow: nhận message từ user
if __name__ == "__main__":
    session_id = "demo-session-1"
    user_input = "Chào sếp, em muốn áp dụng KPI chung cho tất cả các brand."
    short_history = []
    event = {
        "type": "user_message",
        "session_id": session_id,
        "user_input": user_input,
        "short_history": short_history
    }
    response = event_handler.handle_event(event)
    print("AI Response:", response)
