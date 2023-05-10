import time
from abc import ABC, abstractmethod


class SocialChannel:
    def __init__(self, network_type: str, num_followers: int):
        self.type = network_type
        self.num_followers = num_followers


class Post:
    def __init__(self, message: str, timestamp: int):
        self.message = message
        self.timestamp = timestamp


class SocialNetwork(ABC):
    @abstractmethod
    def post(self, message: str) -> None:
        ...


class Youtube(SocialNetwork):
    def __init__(self, channel: SocialChannel):
        self.channel = channel

    def post(self, message: str) -> None:
        ...


class Facebook(SocialNetwork):
    def __init__(self, channel: SocialChannel):
        self.channel = channel

    def post(self, message: str) -> None:
        ...


class Twitter(SocialNetwork):
    def __init__(self, channel: SocialChannel):
        self.channel = channel

    def post(self, message: str) -> None:
        ...


def post_a_message(channel: SocialChannel, message: str) -> None:
    network_type = channel.type
    if network_type == "youtube":
        network = Youtube(channel)
    elif network_type == "facebook":
        network = Facebook(channel)
    elif network_type == "twitter":
        network = Twitter(channel)
    else:
        raise ValueError(f"Unsupported network type: {network_type}")
    network.post(message)


def process_schedule(posts: list[Post], channels: list[SocialChannel]) -> None:
    for post in posts:
        message, timestamp = post.message, post.timestamp
        if timestamp <= time.time():
            for channel in channels:
                if channel.type == "youtube":
                    network = Youtube(channel)
                elif channel.type == "facebook":
                    network = Facebook(channel)
                elif channel.type == "twitter":
                    network = Twitter(channel)
                else:
                    raise ValueError(f"Unknown network type:{channel.type}")
                network.post(message)
