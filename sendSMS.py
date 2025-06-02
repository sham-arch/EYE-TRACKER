from twilio.rest import Client
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def send(msg):
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    twilio_phone_number = os.getenv('TWILIO_PHONE_NUMBER')
    recipient_phone_number = os.getenv('RECIPIENT_PHONE_NUMBER')

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to=recipient_phone_number,
        from_=twilio_phone_number,
        body=msg
    )

    print(f"Message SID: {message.sid}")
