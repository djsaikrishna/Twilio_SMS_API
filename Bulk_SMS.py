import openpyxl
from twilio.rest import Client

# Your Twilio account SID and auth token
account_sid = ''
auth_token = ''

# Path to the Excel file
excel_file_path = 'C:\\Users\\moksh\\Downloads\\Telegram Desktop\\80.xlsx'

# Sheet name containing the phone numbers
sheet_name = 'Sheet1'

# Column number containing the phone numbers (A=1, B=2, etc.)
phone_number_column = 1

# Create a Twilio client
client = Client(account_sid, auth_token)

# Load the Excel file
workbook = openpyxl.load_workbook(excel_file_path)
sheet = workbook[sheet_name]

# Iterate over the rows in the sheet and send messages
for row in sheet.iter_rows(min_row=2, values_only=True):
    phone_number = row[phone_number_column - 1]
    
    message = client.messages.create(
        body='Hi, Subscribe to my YouTube Channel https://youtube.com/@GreyMattersYT',
        from_='12543234627',
        to=phone_number
    )
    
    print('Message sent to {number}'.format(number=phone_number))
