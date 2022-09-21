import os

def send_notification(message):
    # put your notification code here.
    print(f"send notification successd, message: {message}")

def main():
    message = os.environ.get("INPUT_MESSAGE")
    send_notification(message)

if __name__ == "__main__":
    main()