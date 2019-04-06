#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from socket import *
import time
import os
from config import banner as ban
from config.banner import colors 

os.system('cls' if os.name == 'nt' else 'clear')

iniciar = time.time()

def start():

	descricao = ban.banner()
	print(descricao)

	iniciar = time.time()
	if __name__ == '__main__':
		alvo = input('Informe o alvo [127.0.0.1]: ')
		t_IP = gethostbyname(alvo)
		print('Iniciando varredura no alvo: {YELLOW}{}{END}'.format(t_IP, **colors))

		# Quantida de portas deve ser definida de 1-65535 dentro da range
		for i in range(21, 100):
			s = socket(AF_INET, SOCK_STREAM)

			conn = s.connect_ex((t_IP, i))
			if(conn == 0):
				print('Porta {}: {GREEN}ABERTA{END}'.format((i), **colors))
			s.close()
	print('Tempo total: {}'.format(time.time() - iniciar))

try:
    start()
except KeyboardInterrupt:
    print('\n{GREEN}Saindo do portFIAPscan.{END}'.format(**colors))
exit()