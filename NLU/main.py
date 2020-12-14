
import random
import json

import torch

from model import *
from nltk_utils import bag_of_words, tokenize
from result import answer

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "NLU/neuralnet.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

# model = LSTMClassifier(12, 20, len(all_words),len(tags)).to(device)
model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

def nlu(sentence):
	query=sentence
	sentence = tokenize(sentence)
	X = bag_of_words(sentence, all_words)
	X = X.reshape(1, X.shape[0])
	# X = torch.from_numpy(X).to(dtype=torch.long).to(device) for lstm
	X = torch.from_numpy(X).to(device) #for neuralnetwoek

	output = model(X)
	_, predicted = torch.max(output, dim=1)

	tag = tags[predicted.item()]
	result=""
	probs = torch.softmax(output, dim=1)
	prob = probs[0][predicted.item()]
	if prob.item() > 0.6:
	    pass
	else:
	    # print(f"{bot_name}: I do not understand...")
	    tag="search on the web"

	result=answer(tag,query)
	return result
