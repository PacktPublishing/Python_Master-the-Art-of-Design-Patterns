class MailSender:
    def send_mail(self, message):
        print("Sending mail to " + self.email)
        # Add e-mail logic here

class EmailableContact(Contact, MailSender):
    pass
