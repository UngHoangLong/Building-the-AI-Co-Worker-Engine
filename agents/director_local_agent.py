
"""
Director Local Agent: Giám sát tiến độ, gửi hint/chỉ thị, can thiệp khi cần.
TODO:
    - Theo dõi state (trust_score, patience_level, tension_score, list_task_done)
    - Gửi hint cho user nếu cần
    - Tiêm chỉ thị cho Main Agent nếu cần
    - Đóng băng/kết thúc module nếu fail/pass
"""

class DirectorLocalAgent:
    def __init__(self, state_manager):
        self.state_manager = state_manager

    def monitor_and_intervene(self, state, chat_history):
        # TODO: Theo dõi state, gửi hint/chỉ thị khi cần
        pass
