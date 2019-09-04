#__author__ == "Priya"
#https://www.authsmtp.com/python/index.html
import xlrd
import requests
from collections import defaultdict
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import google.oauth2
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import base64
import json


SCOPES = ['https://www.googleapis.com/auth/gmail.send']
ClIENT_SECRET_FILE = 'client_secret.json'
EMAIL = "eswari.gangikunta@gmail.com"


def get_excel_data(File):
    wbk = xlrd.open_workbook(File)
    sh = wbk.sheet_by_index(0)
    File_data = defaultdict(list)
    for row in range(1, sh.nrows):
        val = sh.row_values(row)
        _list = [val[0]]+val[2:]
        File_data[str(val[1])].append(_list)
    return File_data


def get_date_in_format():
    date = datetime.today().strftime('%d-%m-%Y')
    return date


def get_today_bday(File_data, tdate):
    if tdate in File_data.keys():
        return File_data[tdate]


def get_access_token(client_id, client_secret, refresh_token):
    params = {
        "grant_type": "refresh_token",
        "client_id": client_id,
        "client_secret": client_secret,
        "refresh_token": refresh_token
    }

    authorization_url = "https://www.googleapis.com/oauth2/v4/token"

    r = requests.post(authorization_url, data=params)

    if r.ok:
        return r.json()['access_token']
    else:
        return None


def get_service():
    flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', scopes=SCOPES)
    # cred = flow.run_local_server()
    #
    # with open('refresh.token', 'w+') as f:
    #     f.write(cred._refresh_token)
    #
    # print('Refresh Token:', cred._refresh_token)
    # print('Saved Refresh Token to file: refresh.token')

    with open(ClIENT_SECRET_FILE, "r") as f:
        creds = json.load(f)["installed"]
    with open("refresh.token", "r") as r:
        token = r.read()

    access_token = get_access_token(creds['client_id'], creds['client_secret'], token)
    credentials = google.oauth2.credentials.Credentials(access_token)
    service = build('gmail', 'v1', credentials=credentials)
    return service


def send_wishes(service, bday_list):
    for each in bday_list:
        mesg = "Hi Dear"+str(each[0])+",\n\n"+str(each[2])+"\n\nYours,\nPriya"
        msg = MIMEMultipart()
        msg["Subject"] = "Happy Birthday!!(Test mail)"
        msg["From"] = EMAIL
        msg["To"] = str(each[1])
        msg.attach(MIMEText(mesg, "plain"))
        attachment = open(str(each[3]), "rb")
        body = MIMEText('<p align="center">Test Image<img src="cid:image1" /></p>', _subtype='html')
        msg.attach(body)

        img = MIMEImage(attachment.read(), 'jpeg')
        img.add_header('Content-Id', '<image1>')
        msg.attach(img)
        raw = base64.urlsafe_b64encode(msg.as_bytes())
        raw = raw.decode()
        body = {'raw': raw}
        service.users().messages().send(userId="me", body=body).execute()


def main():
    file = "BirthdayWishes.xlsx"
    File_data = get_excel_data(file)
    tdate = get_date_in_format()
    print(tdate)
    today_bday = get_today_bday(File_data, tdate)
    print("BDAY:", today_bday)
    service = get_service()
    send_wishes(service, today_bday)


if __name__ == "__main__":
    main()




