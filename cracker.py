abc='abcdefghijklmnopqrstuvwxyz	ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789012347890-[];(*^$%)'
output=''

def check(s,password):
	if (s==password):
		print("done")
		return True

def crack(pas):
	for a in abc :
		for b in abc :
			for c in abc :
				for d in abc :
					if(check(a+b+c+d,pas)):
						print("done")
						print('whaot i found is ',a+b+c+d)
						return
	print('sorry not found')

c=input()
crack(c)