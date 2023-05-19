# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Your Twilio account SID and auth token
account_sid = ""
auth_token = ""

client = Client(account_sid, auth_token)

assistant = client.autopilot.v1.assistants.create()

print(assistant.sid)
