import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, Concatenate

# Load your dataset
df = pd.read_csv('synthetic_data.csv')

# Define numerical features and categorical features
numerical_features = ['Heartbeat', 'Hours_Worked']
categorical_features = ['Weather', 'Location']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df[numerical_features + categorical_features], df['Recommendation'], test_size=0.2, random_state=42, stratify=df['Recommendation'])

# Standardize numerical features
scaler = StandardScaler()
X_train[numerical_features] = scaler.fit_transform(X_train[numerical_features])
X_test[numerical_features] = scaler.transform(X_test[numerical_features])

# One-hot encode categorical features
encoder = OneHotEncoder(drop='first', sparse=False)
X_train_encoded = encoder.fit_transform(X_train[categorical_features])
X_test_encoded = encoder.transform(X_test[categorical_features])

# Combine numerical and categorical features
X_train_final = pd.concat([X_train[numerical_features], pd.DataFrame(X_train_encoded, columns=encoder.get_feature_names(categorical_features))], axis=1)
X_test_final = pd.concat([X_test[numerical_features], pd.DataFrame(X_test_encoded, columns=encoder.get_feature_names(categorical_features))], axis=1)

# Define the neural network architecture
input_dim = X_train_final.shape[1]

# Input Layer
input_layer = Input(shape=(input_dim,))

# Dense layers for processing
x = Dense(64, activation='relu')(input_layer)
x = Dense(32, activation='relu')(x)

# Output layer
output = Dense(1, activation='linear')(x)  # Assuming the output is continuous for recommendations

# Create the model
model = Model(inputs=input_layer, outputs=output)

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])  # Assuming mean squared error for regression

# Train the model
model.fit(X_train_final, y_train, epochs=10, batch_size=32, validation_data=(X_test_final, y_test))

# Evaluate the model
loss, mae = model.evaluate(X_test_final, y_test)

print(f'Mean Absolute Error: {mae}')
