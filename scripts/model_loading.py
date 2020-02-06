
import numpy as np 
import pandas as pd
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense, Embedding, LSTM, SpatialDropout1D
from keras.callbacks import EarlyStopping
from keras.layers import Dropout
import pickle


def get_location(instruction=['go to tsc from ekushey hall through shaheed minar']):

	MAX_NB_WORDS = 5000
	MAX_SEQUENCE_LENGTH = 30
	EMBEDDING_DIM = 100


	# loading tokenizer
	with open('scripts/tokenizer.pickle', 'rb') as handle:
		tokenizer = pickle.load(handle)


	# defining model architecture
	model = Sequential()
	model.add(Embedding(MAX_NB_WORDS, EMBEDDING_DIM, input_length=30))
	model.add(SpatialDropout1D(0.2))
	model.add(LSTM(128, dropout=0.2, recurrent_dropout=0.2))
	model.add(Dense(8, activation='softmax'))
	model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

	model.load_weights('scripts/model.h5')



	new_instruction = instruction
	seq = tokenizer.texts_to_sequences(new_instruction)
	padded = pad_sequences(seq, maxlen=MAX_SEQUENCE_LENGTH)
	pred = model.predict(padded)
	pred = pred.ravel()
	labels = np.array(["Curzon Hall", "Dr. Muhammad Shahidullah Hall", "Amar Ekushey Hall", "Fazlul Haque Muslim Hall", "Bangla Academy", "TSC", "Shaheed Minar", "Dhaka Medical College Hospital"])

	top = pred.argsort()[::-1]

	result = []
	for i in range(3):   
	    if pred[top[i]] > 0.1:
	        # print(labels[top[i]])
	        result.append(labels[top[i]])

	# return labels[np.argsort(pred)[0][::-1][:3]]
	return result


# go to tsc from ekushey hall through shaheed minar