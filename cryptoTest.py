import crypto,random,mathModule
import affine
import read_english_dictionary as e



def carckTrans():
	string = 'ABCDEFGHIJKLMNOPQ'#	RSTUV'WXYZabcdefghijklmnopqrstuvwxyz'

	for i in range(2000):

		testString=string*random.randint(1,10)


		for key in range(3,len(string)**2):#
				if mathModule.gcd(affine.getKeyPairs(key)[0],len(affine.SYMBOLS)) == 1 and affine.getKeyPairs(key)[0] >2:

					#key=affine.getKeyPairs(key)
					encrypted=affine.encryptMessage(key,testString)#crypto.rows(testString,key)

					decrypted=affine.decryptMessage(key,testString)#crypto.decryptrow(encrypted,key)

					if decrypted == testString :
						continue

					print("failed for -%s- with key -%s- and decrypted as -%s-"%(testString,key,decrypted))
					
					exit()

def crackAffine():
	b=e.load_words()
	encrypted="zn cu cuznkuzCZuck5FKzkutI5.kKFu5CNkcu8FCWu3CF.Nu3KFu9"
	for i in range(len(affine.SYMBOLS)**2):
		#print("at kwwywy")
		if mathModule.gcd(affine.getKeyPairs(i)[0],len(affine.SYMBOLS)) == 1:
			text=affine.decryptMessage(i,encrypted)
			if e.english(text,b,75):
				print(f'found {text}')
				exit()


if __name__=="__main__":
	carckTrans()