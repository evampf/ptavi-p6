#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys


class EchoHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """

    SERVER = (sys.argv[1])
    PORT = int(sys.argv[2])
    SONG = (sys.argv[3])
    MP3 = sys.argv[3][-4:]


    if len(sys.argv) != 4:
        if sys.argv[3][-4:] != ".mp3":
            sys.exit("Usage: python server.py IP port audio_file")


    def handle(self):

        while 1:
            # Leyendo línea a línea lo que nos envía el cliente       
            text = self.rfile.read()
            line = self.rfile.read()
            print("El cliente nos manda " + text.decode('utf-8'))
            LINE = text.decode('utf-8')
            Words_LINES = LINE.split()
            REQUEST = Words_LINES[0]
            print("La peticion es: ", REQUEST)
            print("Listening...")


            if REQUEST == 'INVITE':
                mensaje = b"SIP/2.0 100 Trying\r\n\r\n"
                mensaje += b"SIP/2.0 180 Ring\r\n\r\n"
                mensaje += b"SIP/2.0 200 OK\r\n\r\n"
                self.wfile.write(mensaje)
            elif REQUEST == 'ACK':
                SONG = (sys.argv[3])
                aEjecutar = './mp32rtp -i 127.0.0.1 -p 23032 < ' + self.SONG
                os.system(aEjecutar)
            elif REQUEST == 'BYE':
                self.wfile.write(b'SIP/2.0 200 OK\r\n\r\n')

            # Si no hay más líneas salimos del bucle infinito
            if not line:
                break

if __name__ == "__main__":
    serv = socketserver.UDPServer((sys.argv[1], int(sys.argv[2])), EchoHandler)
    print("Lanzando servidor UDP de eco...")
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
