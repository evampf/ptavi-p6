#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys

# Cliente UDP simple.

# Dirección IP del servidor.

INF = sys.argv[2]
INF1 = INF.split("@")
INF2 = INF1[1].split(":")


PORT = int(INF2[1])
SERVER = (INF2[0])
USER = (INF1[0])

REQUEST = sys.argv[1]


if len(sys.argv) != 3:
    sys.exit("Usage: python client.py method receiver@IP:SIPport")


# Contenido que vamos a enviar
LINE_SIP = " sip:" + USER + "@" + SERVER + " SIP/2.0\r\n\r\n"
LINE = REQUEST + LINE_SIP
print(LINE)

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.connect((SERVER, PORT))

print("Enviando: " + LINE)
my_socket.send(bytes(LINE, 'utf-8') + b'\r\n')
data = my_socket.recv(1024)

print(data.decode('utf-8'))
RecibidoInvite = data.decode('utf-8').split('\r\n\r\n')[0:-1]

Recibido100 = ("SIP/2.0 100 Trying")
Recibido180 = ("SIP/2.0 180 Ring")
Recibido200 = ("SIP/2.0 200 OK")
Recibido = [Recibido100, Recibido180, Recibido200]


if RecibidoInvite == Recibido:
    LINE_ACK = "ACK" + LINE_SIP
    print("Enviando ACK...", LINE_ACK)
    my_socket.send(bytes(LINE_ACK, 'utf-8') + b'\r\n')
    data = my_socket.recv(1024)

print('Recibido -- ', Recibido)
print("Terminando socket...")


# Cerramos todo
my_socket.close()
print("Fin.")
