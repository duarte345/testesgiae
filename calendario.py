from __future__ import print_function

import datetime
import os.path
import os
from giae import Testes

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly','https://www.googleapis.com/auth/calendar']
calendarId = 'c_vrsorjnl70s8qq2vsv824rugu8@group.calendar.google.com' # calendário associado
t = Testes(os.getenv('UTILIZADOR'), os.getenv('PASSWORD'))
minutos_antes = 60*24 # minutos antes, aqui está 1 dia antes (60 minutos * 24 horas)
email_destinatario = 'turma_10f@csmiguel.pt'
t.update


# fnction used to access the testes calendar of giae
def giae():
    utilizador = os.getenv('UTILIZADOR')
    password = os.getenv('PASSWORD')
    lista = Testes(utilizador, password)
    lista.update()
    return lista


# get calendars from the google Calendar API
def obter_eventos(calendarId):
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        events_result = service.events().list(calendarId=calendarId, timeMin=now,
                                              maxResults=10, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])
        return events

    except HttpError as error:
        print('An error occurred: %s' % error)


# Create an event on Google Calendar based on the calendarId
def criar_evento(evento, calendarId):
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None

# configuring the configurations and the token.json file, in case it's not congigured
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)
        # Call the Google Calendar API 
        event = service.events().insert(calendarId=calendarId, body=evento).execute()
        # Creates a variable with the essential information
        status_output = {
            "Nome": event.get('summary'),
            "status": event.get('status')
        }
        return status_output

    except HttpError as error:
        print('An error occurred: %s' % error)


# Verify if the event given is on the google calendar or not
def teste_ja_em_calendario(teste):
    data = teste.get('date')
    iteracao = []
    for evento in obter_eventos(calendarId):
        if evento.get('start').get('dateTime') is None:
            data_evento = evento.get('start').get('date')
        else:
            data_evento = evento.get('start').get('dateTime').split('T')[0]
        if data_evento == data:
            iteracao.append(True)
        else:
            iteracao.append(False)
    if True in iteracao:
        return True
    return False