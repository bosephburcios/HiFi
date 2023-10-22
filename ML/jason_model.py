import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, MinMaxScaler

data = pd.read_csv('synthetic_data.csv')

def unique(col):
  unique_arr = []
  for i in range(len(col)):
    if col[i] not in unique_arr:
      unique_arr.append(col[i])
  return unique_arr

unique(data["Recommendation"])

# Normalize numerical columns
scaler = MinMaxScaler()
data[['Heartbeat', 'Hours_Worked']] = scaler.fit_transform(data[['Heartbeat', 'Hours_Worked']])

# One-Hot Encode categorical columns
data = pd.get_dummies(data, columns=['Weather', 'Location'])

# Convert 'Recommendation' into integers
label_encoder = LabelEncoder()
data['Recommendation'] = label_encoder.fit_transform(data['Recommendation'])

data = data.sample(frac=1)
X = data.drop('Recommendation', axis=1)
y = data['Recommendation']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu', input_dim=X_train.shape[1]),
    tf.keras.layers.Dropout(0.3),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dropout(0.3),
    tf.keras.layers.Dense(len(y.unique()), activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=50, batch_size=32)

loss, accuracy = model.evaluate(X_test, y_test)
print(f"Test accuracy: {accuracy * 100:.2f}%")


# Plot accuracy
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Model Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

# Plot loss
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Model Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.show()