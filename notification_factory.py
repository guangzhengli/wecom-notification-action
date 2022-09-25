from file_notification import FileNotification
from message_notification import MessageNotification

class NotificationFactory:
    def get_notification(self, type):
        if type == 'message':
            return MessageNotification()
        elif type == 'file':
            return FileNotification()
        else:
            raise ValueError(type)