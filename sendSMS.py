from twilio.rest import Client

#authentication
def send(msg):
    account_sid = 'AC86c6334ae38973ad83e7d262feb2fc66'
    auth_token = 'a7385fb854f5e30ae41923c8a74846a7'
    twilio_phone_number = '+15642323524'

    # Recipient's phone number
    recipient_phone_number = '+919585559723'  # Replace with the actual phone number

    
    # Initialize the Twilio client
    client = Client(account_sid, auth_token)

    # Send the SMS
    message = client.messages.create(
        to=recipient_phone_number,
        from_=twilio_phone_number,
        body=msg
    )

    # Print the SID (unique identifier) of the sent message
    print(f"Message SID: {message.sid}")
        
    
