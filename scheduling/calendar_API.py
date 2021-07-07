import datetime
from datetime import timedelta

import pytz
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
from . import views

service_account_email = "booking-app@booking-app-318011.iam.gserviceaccount.com"
SCOPES = ["https://www.googleapis.com/auth/calendar"]
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    filename="scheduling/credentials.json", scopes=SCOPES
)


def build_service():
    service = build("calendar", "v3", credentials=credentials)
    return service


