import os.path
from googleapiclient.discovery import build
from google.oauth2 import service_account
import requests
from bs4 import BeautifulSoup
from decouple import config


def google_read():
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    SERVICE_ACCOUNT_FILE = os.path.join(BASE_DIR, 'credentials.json')

    credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    SAMPLE_SPREADSHEET_ID = config('SAMPLE_SPREADSHEET_ID')
    SAMPLE_RANGE_NAME = 'L1!A2:F'

    service = build('sheets', 'v4', credentials=credentials)

    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])
    return values


def kurs_uah():
    url = f'https://tables.finance.ua/ru/currency/official/-/1._'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'lxml')
    usdt = soup.find(class_="topcurs1 haslink")
    kurs = usdt.find(class_="value").text
    return kurs


def telegram_sender(order_id):
    text = f'Order #{order_id} delivery overdue!'
    token = config("TOKEN-TELEGRAM-BOT")
    chat_id = config("CHAT-ID")
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
    requests.get(url_req)
