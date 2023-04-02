import numpy as np
from keras.models import Sequential
from keras.layers import Dense, LSTM

# Prepare the data
data = [256, 793, 235, 909, 248, 852]
# Convert each number to a sequence of digits
data = [[int(digit) for digit in str(num)] for num in data]
# Convert the digits to one-hot encodings
data = np.array([np.eye(10)[num] for num in data])
# Create input-output pairs
X = data[:-1]
y = data[1:]

# Define the LSTM model
model = Sequential()
model.add(LSTM(32, input_shape=(X.shape[1], X.shape[2])))
model.add(Dense(10, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the LSTM model
model.fit(X, y, epochs=100, batch_size=1, verbose=2)

# Generate predictions
test_data = [467, 123, 789]
test_data = [[int(digit) for digit in str(num)] for num in test_data]
test_data = np.array([np.eye(10)[num] for num in test_data])
for i in range(len(test_data)):
    test_input = test_data[i:i+1]
    pred = model.predict(test_input)
    next_num = np.argmax(pred)
    print('Predicted next number for input', test_data[i], 'is', next_num)
