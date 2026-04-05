"""
State Manager: Đọc/ghi trạng thái vào Redis
"""
import redis
import json

class StateManager:
    def __init__(self, redis_url="redis://localhost:6379/0"):
        self.r = redis.Redis.from_url(redis_url, decode_responses=True)

    def get_state(self, session_id):
        state = self.r.get(session_id)
        return json.loads(state) if state else None

    def set_state(self, session_id, state_dict):
        self.r.set(session_id, json.dumps(state_dict))
