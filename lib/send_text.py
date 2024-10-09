import os
from twilio.rest import Client
from lib.authorisation import acc_sid, token

class SendText:

    def __init__(self, number):
        self.number = number
        self.acc_sid = acc_sid
        self.token = token

    def get_request(self):
        account_sid = self.acc_sid
        auth_token = self.token
        client = Client(account_sid, auth_token)

        message = client.messages.create(
        from_='whatsapp:+14155238886',
        content_sid='HX350d429d32e64a552466cafecbe95f3c',
        content_variables='{"1":"today","2":"18:00"}',
        to= f"whatsapp:{self.number}"
        )

        return message.body


    def format_text(self):
        confirmation_text = self.get_request()
        return(confirmation_text)
