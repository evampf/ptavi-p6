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

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.connect((SERVER, PORT))

print("Enviando: " + LINE)
my_socket.send(bytes(LINE, 'utf-8') + b'\r\n')
data = my_socket.recv(1024)

print('Recibido -- ', data.decode('utf-8'))
print("Terminando socket...")

# Cerramos todo
my_socket.close()
print("Fin.")
