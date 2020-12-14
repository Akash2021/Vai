def preprocess(query):

    query=query.split("open",1)[1] 
    query=query.translate(str.maketrans('', '', string.punctuation)) # remove punctuations 
    query= query.split()
    s=""
    for word in query:
        if word not in en_stops:
            s+=word
    return s

if __name__ == '__main__':
	# print(preprocess("open youtube "))
	print("hello")