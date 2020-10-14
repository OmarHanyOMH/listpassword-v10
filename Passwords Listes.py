Green="[\033[1;32m\]"
from V7xStyle import Animation
from V7xStyle import Style

##############################
#Style And Animation
An= Animation
An.DL()
s = Style(Green+"                  Pass                ",Green+'            Word                    ').Square()
print(s)


##############################
print ("Tybe : help ","Type : exit")

o=1
while True:
	num =  input ("please the Number ==> ")
	if num == "help":
		print('The tool is still under development',"To communicate or to develop the tool, please contact us at hanyoaao@gmail.com")
	
	if num =='exit':
		An.DL()
		break
	elif num == "x":
		An.DL()
		break
	try:
		num = int(num)
		while o < num :
		        o = o + 1
		        print (o)
	except ValueError:
		print("Please the Numbe")
		