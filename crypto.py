import math	
import pyperclip
import mathModule as m
'''
gcd=greatest comon divisor (a%b)=1
modInvers= inverse mod ((A*i)%len)==1
caesarshift//caesarShift//= a=>b b=>c
deceasar//decaesarCrypto// =  b=>a  c=>a
transppose//rows//
detreanpose
multiplicative//multiplicativeCrypt//
and demultipicaive //decryptMultiplicative//
'''


def caesarShift(plain,key):
	
	out=''
	
	arr=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

	for j in range(len(plain)):
		added=False
		for i in range(len(arr)):
			if arr[i]==plain[j]:
				index=i+key
				if i+key > 25:
					index = (i+key)-26
				out=out+arr[index]
				added = True
				break
		if not added:
			out = out + plain[j]

	return(out)



def decaesarCrypto(plain,key):
	out=''
	arr=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	for j in range(len(plain)):
		added=False
		for i in range(len(arr)):
			if arr[i]==plain[j]:
				index=i-key
				if index < 0:
					index = (i-key) +26
				out=out+arr[index]
				added = True
				break
		if not added:
			out = out + plain[j]

	return(out)


def rows(plan,key):
	
	out=''
	shift=0
	for char in range(len(plan)):
		
		if char == key :
			break

		#print(char)
		current=char  
		while current+shift < len(plan):
			out=out+plan[current+shift]
			current += key
	
	return out



SET='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijlmnopqrstuvwxyz1234567890.,?! '
	
def multiplicativeCrypt(plain,key):

	SET='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijlmnopqrstuvwxyz1234567890.,?! '
	out=''
	for i in plain:

		current_index=SET.find(i)*key
		#print (current_index)
		print(i,"moddedd is === ",current_index%len(SET),'  -orignal - is == ',current_index)
		out=out + SET[current_index%len(SET)]
	print(out)
	return out


def decryptMultiplicative(plain,nkey):

	SET='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijlmnopqrstuvwxyz1234567890.,?! '
	out=''
	key=m.modInverse(nkey,len(SET))
	for i in plain:

		current_index=SET.find(i)*key
		#print (current_index)
		print(i,"moddedd is === ",current_index%len(SET),'  -orignal - is == ',current_index)
		out=out + SET[current_index%len(SET)]
	print(out)
	return out



def decryptrow(plain,key):

	norows=math.ceil((len(plain)/key))
	row=[]
	print("prin")
	out=''
	shift=0
	allw=key-((key*norows)-len(plain))
	print("allowed are ",allw)
	print("no of rows ",norows)

	for row in range(norows):
		for colom in range(key):
			if colom > allw-1 and row == norows-1:
				print(f'added at row {row} and colom {colom} added sap no{(colom*norows)+row}')
				print("shifti in "+str(shift))
				# insert dash in between
				plain=plain[:(colom*norows)+row+shift]+' '+plain[(colom*norows)+row+shift:]
				#shift+=1


	shift=0
	print('-'+plain+'-')
	row=[]
	for colom in range(norows):
		for ro in range(key):
			print(f'at {colom} and ro {ro}')
			'''
			if colom == norows-1 and ro > allw:
				ro=ro+1
				colom=0
				shift=shift+1
				print("addedrgtaelrigjeriiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiigja",colom,ro)
				continue
			'''
			if len(plain)-((ro*norows)+colom) >= 0 :

				row.append(plain[((norows*ro)+colom)])
				print(shift)
				print(f'mafde this time wasss {row}')
				out=out+''.join(row)
				row=[]
	
	print(out)
	return out.strip()
	
def maink():
	
	print("type s or t or cs or ct followed by -")

	raw_plain = input("enter the sentence -");
	
	choice=''
	plain=''
	
	if '-' in raw_plain :
		plain,choice=raw_plain.split('-')
	else:
		print("invalid choice one of the options must be selected")

	print(choice[:3])
	
	while True:
		
		try:
			key=int(input("enter the key -"))
			break		
		except :
			print('key must be a number ')
			continue

	crypto=''

	if 's' in choice:
		print("\n....Encripted....\n")
		crypto=caesarShift(plain,key)

	if 't' in choice:
		print("...decrypted...")
		crypto=rows(plain,key)

	if 'cs' in choice:
		print("...decrypted...")
		crypto=decaesarCrypto(plain,key)	


	if 'ct' in choice:
		print("...decrypted...")
		crypto=decryptrow(plain,key)

	print(crypto)

	pyperclip.copy(crypto)


def main():

	plain=input('-')

	print(f'size of keyis{len(plain)}')

	print("VALID KEYS_-_-")
	for i in range(len(SET)):
		if m.gcd(i,len(SET))==1:
			print(i)
	key=int(input("key-"))
	crypted=multiplicativeCrypt(plain,int(key))
	print(crypted)
	pyperclip.copy(crypted)
	print(decryptMultiplicative(crypted,key))

if __name__ == '__main__' :
	main()
