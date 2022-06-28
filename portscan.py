#!/usr/bin/python
#import sys, socket

if len(sys.argv) <= 1:
	print "Portscan - Modo de uso: Python arquivo.py 192.168.0.1"
else:
	for porta in range(0, 65536):
		socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		resultado = socket1.connect_ex((sys.argv[1], porta))
		if resultado == 0:
			print "Porta",porta,"Aberta"
			socket1.close()
		else:
			socket1.close()