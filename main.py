from twilio.rest import Client

SID = ''
AUTH_TOKEN = ''

cl = Client(SID, AUTH_TOKEN)

cl.messages.create(body='Hey, I am GreyMatters Here', from_='YOUR_NUMBER' to='RECIEVER_NUMBER')
