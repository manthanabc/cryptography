#from book itself not mine

import math,sys,pyperclip,mathModule,random

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

def main():
	
	myMessage="""this is the top secrate nuclear codes from world war 3"""
	myKey=getRandomKey()
	mymode='encrypt'

	if mymode == 'encrypt':
		translated=encryptMessage(myKey,myMessage)
	elif mymode == 'decrypt':
		translated=decryptMessage(myKey,myMessage)

	print('key: %s'%(myKey)) 
	print('%sed text:'%(mymode),translated)
	pyperclip.copy(translated)
	print('full %sed text copied to clipboard'%(mymode))

def getKeyPairs(key):

	keyA=key//len(SYMBOLS)
	keyB=key%len(SYMBOLS)
	return(keyA,keyB)


def checkKeys(keyA,keyB,mode):

	if keyA ==1 and mode =='encrypt':
		sys.exit("key A is chosn too weak to proceed")
	if keyB == 0 and mode=='encrypt':
		sys.exit("key b s 0 soits too weak")
	if keyA < 0 or keyB < 0 or keyB > len(SYMBOLS)-1:
		sys.exit("keya must be grater than 0 and b between 0 and len symbols")
	if mathModule.gcd(keyA,len(SYMBOLS)) != 1:
		sys.exit("not relatively prime")

def encryptMessage(key,message):
	keyA,keyB=getKeyPairs(key)
	checkKeys(keyA,keyB,'encrypt')
	ciphertext=''
	for symbol in message:
		if symbol in SYMBOLS:
			symbolIndex=SYMBOLS.find(symbol)
			ciphertext+=SYMBOLS[(symbolIndex*keyA+keyB)%len(SYMBOLS)]
		else:
			ciphertext+=symbol
	return ciphertext

def decryptMessage(key,message):
	keyA,keyB=getKeyPairs(key)
	checkKeys(keyA,keyB,'decrypt')
	plaintext=''
	modInverseOfKeyA=mathModule.modInverse(keyA,len(SYMBOLS))
	for symbol in message:
		if symbol in SYMBOLS:
			symbolIndex=SYMBOLS.find(symbol)
			plaintext+=SYMBOLS[(symbolIndex-keyB)*modInverseOfKeyA %len(SYMBOLS)]
		else:
			plaintext+=symbol
	return plaintext

def getRandomKey():
	while True:
		keyA=random.randint(2,len(SYMBOLS))
		keyB=random.randint(2,len(SYMBOLS))
		if mathModule.gcd(keyA,len(SYMBOLS)) == 1:
			return keyA*len(SYMBOLS)+keyB

if __name__=="__main__":
	main()