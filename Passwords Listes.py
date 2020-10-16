
##############################
Green="[\033[1;32m\]"
from V7xStyle import Animation
from V7xStyle import Style
import os
import compileall
##############################
compileall.compile_dir('listpassword-v10')

os.system("clear")
###############################
#Style And Animation	

An= Animation
An.DL()
def style ():
	print(Green+"     ___  ___   _   _       ___  ___        _   _       ___   _   _    _____   _____")   
	print(Green+"    /   |/   | | | | |     /   |/   |      | | | |     /   | | | / /  | ____| |  _  \ ") 
	print(Green+'   / /|   /| | | |_| |    / /|   /| |      | |_| |    / /| | | |/ /   | |__   | |_| |  ')
	print(Green+'/ / / | | |  _ |  _  | | / / |__/ | |      |  _  |   / / | | | |\ \   |  __|  |  _  /  ')
	print(Green+' / /       | | | | | |  / /       | |      | | | |  / /  | | | | \ \  | |___  | | \ \  ')
	print(Green+"/_/        |_| |_| |_| /_/        |_|      |_| |_| /_/   | | | |  \ \ | ____| | |  \ ")

##############################
style ()

print (" Tybe :\[\033[1;34m\] help ","\[\033[1;31m\]Type : \[\033[1;31m\]exit")

o=1
while True:
	num =  input ("Please the Number ==> ")
	if num == "help":
		print('The tool is still under development',"To communicate or to develop the tool, please contact us at hanyoaao@gmail.com")
	
	if num =='exit':
		An.DL()
		break
	elif num == "x":
		An.DL()
		break
	elif num == "clear":
		os.system("clear")
	elif num == "banner":
		style ()
	try:
		num = int(num)
		while o < num :
		        o = o + 1
		        print (o)
	except ValueError:
		print("Please the Numbe")
		
