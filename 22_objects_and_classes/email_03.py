""" Checking emails """


class Email:
    """ function for checking the emails """
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        """ Turning the sent from False to Send """
        self.is_sent = True

    def get_info(self):
        """ Getting the info """
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


info = input()
final_emails = []
while info != "Stop":
    new_sender, new_receiver, new_content = info.split()
    email_info = Email(new_sender, new_receiver, new_content)
    final_emails.append(email_info)
    info = input()
indexes = [int(index) for index in input().split(", ")]
for index in indexes:
    final_emails[index].send()
for current_email in final_emails:
    print(current_email.get_info())
