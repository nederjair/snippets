import gspread
from google.oauth2.service_account import Credentials

scopes = [
    "https://www.googleapis.com/auth/spreadsheets"
]

creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
client = gspread.authorize(creds)

wb_id = '1qJUZcY8tsyfwTUU6bay-QZpxvCPa6WMYfUgNs76Wvyo'
ws_title = 'attendance'

wb = client.open_by_key(wb_id)
ws_list = wb.worksheets()

if ws_title in [ws.title for ws in ws_list]:
    sh = wb.worksheet(ws_title)
    all_values = sh.get_all_values()
    header = all_values[0]
    colCount = len(header)
    rowCount = len(all_values)
    print('rowCount:', rowCount)
    print('colCount:', colCount)
else:
    print('worksheet', ws_title, 'not found!')


