from giae import Testes
import os, logging
from calendario import obter_eventos, criar_evento, teste_ja_em_calendario

t = Testes(os.getenv('UTILIZADOR'),os.getenv('PASSWORD'))
calendarId = 'c_vrsorjnl70s8qq2vsv824rugu8@group.calendar.google.com' # calendário associado
eventos = obter_eventos(calendarId)
minutos = 60*24 # minutos, aqui é 1 dia antes ou 1440 min antes
email_destinatario = 'turma_10f@csmiguel.pt'

def main():
    for teste in t.testes_futuros():
        if teste_ja_em_calendario(teste):
            print('Já em calendário')
            pass
        else:
            evento = {
                'summary': teste.get('summary'),
                'description': teste.get('summary'),
                'start': {
                    'dateTime': teste.get('start'),
                    'timeZone': 'Europe/Lisbon',
                },
                'end': {
                    'dateTime': teste.get('end'),
                    'timeZone': 'Europe/Lisbon',
                },
                'attendees': [
                    {'email': email_destinatario},
                ],
                'reminders': {
                    'useDefault': False,
                    'overrides': [
                    {'method': 'email', 'minutes': minutos},
                    {'method': 'popup', 'minutes': minutos},
                    ],
                },
            }
            print(criar_evento(evento, calendarId))

if __name__ == '__main__':
    main()