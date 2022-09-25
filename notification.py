import os
from corpwechatbot.chatbot import CorpWechatBot
from notification_factory import NotificationFactory

def send_notification():
    message = get_message_by_type()
    bot = CorpWechatBot(key=get_webhook_url())
    if (is_at_all() == 'true'):
        bot.send_text(content=message, mentioned_list=['@all'])
    else:
        bot.send_text(content=message)
    print(f"send notification successd, message: {message}")

def get_message_by_type():
    type = os.environ.get("INPUT_TYPE")
    factory = NotificationFactory()
    return factory.get_notification(type).get_message()
    
def get_webhook_url():
    webhook = os.environ.get("INPUT_WEBHOOK")
    if webhook:
        return webhook
    else:
        raise ValueError("webhook URL is empty")

def is_at_all():
    return os.environ.get("INPUT_IS_AT_ALL")

def main():
    send_notification()

if __name__ == "__main__":
    main()
