from twilio.rest import Client


def send_sms(to_phone, message):
    account_sid = "TWILIO_ACCOUNT_SID"
    auth_token = "TWILIO_AUTH_TOKEN"
    from_phone = "+111111111"

    client = Client(account_sid, auth_token)
    client.messages.create(body=message, from_=from_phone, to=to_phone)
