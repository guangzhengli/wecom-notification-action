import os

class MessageNotification:
    def get_message():
        message = os.environ.get("INPUT_MESSAGE")
        if message:
            return message
        else:
            raise ValueError("message content is empty")