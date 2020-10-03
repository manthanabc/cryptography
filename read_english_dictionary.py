def load_words():
    with open('words.txt') as word_file:
        valid_words = (word_file.read().split())
        #valid_words=file.read()
        words={}
        for i in valid_words:
        	words[i.lower()]=None

    return words

def isEnglish(wordc,dic):
	#print('checking for  -'+wordc)
	if wordc.lower().strip() in dic:
		return True

	else:
		return False


def removechar(i):
	out=i
	numbersandsymbol='''10!@#$%23456789^&*():"{<?>][]}{//.,?><'''
	for symbol in numbersandsymbol:
		#print('now checking for   -'+symbol)
		if symbol in out:
			#print ('replacing '+symbol)
			out=out.replace(symbol,'')
	return out 

def english(sentence,dic,min_word_percent=85,min_char_percent=60):

	noofeng=0
	totalchar=len(sentence)
	noofvalid=totalchar
	total=0
	sent=sentence.lower().split()
	for i in sent:
		i=i.lower()
		total=total+1
		it=removechar(i)
		if it != i:
			noofvalid=noofvalid-1
			i=it
		if isEnglish(i,dic):
			noofeng=noofeng+1

	ratioofwords=noofeng/total
	ratioofchar=noofvalid/totalchar
	#print(f'word percent is {ratioofwords} and char percent is {ratioofchar}')
	if ratioofwords > min_word_percent/100 and ratioofchar>min_char_percent/100:
		return True
	else:
		return False



if __name__ == '__main__':
    english_words = load_words()
    # demo print
    print('fate' in english_words)
