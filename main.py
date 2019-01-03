"""
Project Goals:
	- Be able to feed data into a neural network that defines the disparate elements an arbitrary dungeon
	- Be able to evaluate a dungeon's data and identify reoccuring elements
	- Using a predictive algorithm, generate a new dungeon using the most commonly occuring elements (with some degree of randomness, in placement, chosen elements, orientation, etc.)
"""

from keras.models import Sequential


def main():
	"""
		Use Keras neural net to read numerical representation of a dungeon and find patterns within input data.
		Use a generative adversarial network (GAN) to generate new images based off the patterns found.
	"""
	model = Sequential()
	model.add(Dense(units=64, activation='relu', input_dim=100))
	model.add(Dense(units=10, activation='softmax'))

	model.compile(loss='categorical_crossentropy',
	              optimizer='sgd',
	              metrics=['accuracy'])

if __name__ == "__main__":
	main()