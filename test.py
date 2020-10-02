from jaro import jaro_Winkler
import string
from nltk.corpus import stopwords
en_stops = set(stopwords.words('english'))
def test(query):

	query=query.split("open",1)[1] 
	query=query.translate(str.maketrans('', '', string.punctuation)) # remove punctuations 
	query= query.split()
	s=""
	for word in query:
		if word not in en_stops:
			s+=word

	return s
file1 = open("websitelist.txt","r") 
def find(s1):
	ma=float(0.0)
	ans=""
	for x in file1.readlines():
		temp=jaro_Winkler(s1,x)
		if temp>ma and temp>0.75:
			ans=x
			ma=temp
	return ans


if __name__ == "__main__" : 
	s1=test("can you open imsnit for me")
	# print(test("open youtube please"))
	print(find(s1))


