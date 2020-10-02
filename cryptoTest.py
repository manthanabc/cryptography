import crypto,random

string = 'ABCDEFGHIJKLMNOPQ'#	RSTUV'WXYZabcdefghijklmnopqrstuvwxyz'


for i in range(2000):

	testString=string*random.randint(1,10)


	for key in range(1,int(len(string)/2)):

			encrypted=crypto.rows(testString,key)

			decrypted=crypto.decryptrow(encrypted,key)

			if decrypted == testString :
				continue

			print("failed for -%s- with key -%s- and decrypted as -%s-"%(testString,key,decrypted))
			
			exit()