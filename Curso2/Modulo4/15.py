import os
import time
import datetime
import calendar

print("Diretório atual:", os.getcwd())

agora = datetime.datetime.now()
print("Data e hora atual:", agora.strftime("%d/%m/%Y %H:%M:%S"))

ano = agora.year
mes = agora.month
print(f"\nCalendário de {mes}/{ano}:")
print(calendar.month(ano, mes))

print("Esperando 3 segundos...")
time.sleep(3)
print("Continuando o programa.")
