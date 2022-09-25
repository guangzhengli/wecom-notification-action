import os
from corpwechatbot.chatbot import CorpWechatBot

def send_notification():
    bot = CorpWechatBot(key=get_webhook_url())
    if (is_at_all() == 'true'):
        bot.send_text(content=get_message_content(), mentioned_list=['@all'])
    else:
        bot.send_text(content=get_message_content())
    print(f"send notification successd, message: {get_message_content()}")

def get_message_content():
    message = os.environ.get("INPUT_MESSAGE")
    if message:
        return message
    else:
        raise ValueError("message content is empty")
    
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