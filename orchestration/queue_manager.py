"""
Queue Manager: Điều phối job giữa các agent qua Redis Pub/Sub
"""
import redis

class QueueManager:
    def __init__(self, redis_url="redis://localhost:6379/0"):
        self.r = redis.Redis.from_url(redis_url, decode_responses=True)

    def publish(self, channel, message):
        self.r.publish(channel, message)

    def subscribe(self, channel):
        pubsub = self.r.pubsub()
        pubsub.subscribe(channel)
        return pubsub
