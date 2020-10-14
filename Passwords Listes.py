Green="[\033[1;32m\]"
from V7xStyle import Animation
from V7xStyle import Style

##############################
#Style And Animation
An= Animation
An.DL()
print(s)
s = Style(Green+"                        Pass                ",Green+'                        Word                    ').Square()


##############################
o=1
while True:
	num =  input ("please the Number ==> ")
	if num =='exit':
		An.DL()
		break
	try:
		num = int(num)
		while o < num :
		        o = o + 1
		        print (o)
	except ValueError:
		print("Please the Numbe")
		