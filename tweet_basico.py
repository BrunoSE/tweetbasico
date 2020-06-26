#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Bruno Stefoni
# Created Date: Mon May 10 23:02:20 EDT 2020
# =============================================================================
"""Este script es un "bot" básico que simplemente twittea lo deseado a la misma
hora cada día. Para esto basta cambiar variables tuit, hora, minuto, segundo.
Es necesario obtener las llaves o token de API, entregadas por twitter.
"""
# =============================================================================

from twython import Twython
import datetime
from time import sleep

# Aquí los 4 parámetros a cambiar por el usuario
tuit = 'Tweet de Prueba que puede decir cualquier cosa!'

hora = 0
minuto = 15
segundo = 0

# Estas llaves o Token se consiguen en la misma página de Twitter
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_KEY = ""
ACCESS_SECRET = ""

# Acá abajo el código que hace todo

if len(tuit) > 280 or (hora < 0 or hora > 24 or
                       minuto < 0 or minuto > 59 or
                       segundo < 0 or segundo > 59):
    exit()

if hora == 24:
    hora = 0

t_ahora = datetime.datetime.today()

hora_tuit = datetime.datetime(t_ahora.year, t_ahora.month, t_ahora.day,
                              hora, minuto, segundo)

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)

while True:

    segundos_durmiendo = (hora_tuit - t_ahora).total_seconds()
    if segundos_durmiendo < 0:
        hora_tuit = hora_tuit + datetime.timedelta(days=1)
        hora_tuit = hora_tuit.replace(hour=hora, minute=minuto, second=segundo)
        segundos_durmiendo = (hora_tuit - t_ahora).total_seconds()

    hrs_sleep = int(segundos_durmiendo / 3600)
    mins_sleep = int((segundos_durmiendo / 60) - hrs_sleep * 60)
    secs_sleep = int(segundos_durmiendo - hrs_sleep * 3600 - mins_sleep * 60)

    hrs_str = "horas" if hrs_sleep != 1 else "hora"
    min_str = "minutos" if mins_sleep != 1 else "minuto"
    sec_str = "segundos" if secs_sleep != 1 else "segundo"

    print('Se va a twittear en %d %s %d %s %d %s' % (hrs_sleep, hrs_str,
                                mins_sleep, min_str, secs_sleep, sec_str,))
    sleep(segundos_durmiendo)

    print('Tuiteando: ', tuit)
    twitter.update_status(status=tuit)

    sleep(2)
    t_ahora = datetime.datetime.today()
