class Notification:
    def send(self,message):
        pass

class MessageSender:
    def send_message(self,message,method):
        print(f"Sending {method} : {message}")

class EmailNotification(Notification):
    def __init__(self):
        self.sendingMessage = MessageSender()

    def send(self,message):
        self.sendingMessage.send_message(message,"Email")


class SMSNotification(Notification):
    def __init__(self):
        self.sendingMessage = MessageSender()

    def send(self,message):
        self.sendingMessage.send_message(message,"SMS")

class PushNotification(Notification):
    def __init__(self):
        pass

    def send(self,message):
        message_obj = MessageSender()
        message_obj.send_message(message,"Push Notification")   

notifications = [
    EmailNotification(),
    SMSNotification(),
    PushNotification()
]

def notify_all(notifications,message):
        for n in notifications:
            n.send(message)


if __name__ == '__main__':
    for n in notifications:
        n.send("Hello user!")
        
    notify_all(notifications, "System Update")