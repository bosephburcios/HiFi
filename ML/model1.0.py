import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
import joblib


# 1. Preprocessing function
def preprocess_input_data(heartbeat, hours_worked, weather, location):
    # Create a DataFrame from the inputs
    input_data = pd.DataFrame({
        'Heartbeat': [heartbeat],
        'Hours_Worked': [hours_worked],
        'Weather': [weather],
        'Location': [location]
    })
    
    # Normalize the numerical columns
    scaler = joblib.load('saved_scaler.pkl')
    input_data[['Heartbeat', 'Hours_Worked']] = scaler.fit_transform(input_data[['Heartbeat', 'Hours_Worked']])

    # One-Hot Encode the categorical columns
    
    input_data = pd.get_dummies(input_data, columns=['Weather', 'Location'])

    # Handle case where some columns might be missing after one-hot encoding
    expected_columns = ['Heartbeat', 'Hours_Worked', 'Weather_Sunny', 'Weather_Rainy', 'Weather_Cloudy', 'Weather_Snowy', 'Location_Urban', 'Location_Suburban', 'Location_Rural']
    for col in expected_columns:
        if col not in input_data.columns:
            input_data[col] = 0

    return input_data[expected_columns]

# 2. Load the model
loaded_model = tf.keras.models.load_model('my_model.h5')

# 3. Take user input
heartbeat = float(input("Enter Heartbeat (e.g., 85): "))
hours_worked = float(input("Enter Hours Worked (e.g., 9): "))
weather = input("Enter Weather (Sunny, Rainy, Cloudy, Snowy): ")
location = input("Enter Location (Urban, Suburban, Rural): ")

# 4. Preprocess the data

processed_data = preprocess_input_data(heartbeat, hours_worked, weather, location)
processed_data = processed_data.astype('float32')

# 5. Make predictions
label_encoder = joblib.load('label_encoder.pkl')
predictions = loaded_model.predict(processed_data)

# 6. Display the prediction (assuming it's a classification problem)
predicted_class_index = np.argmax(predictions, axis=1)
predicted_label = label_encoder.inverse_transform(predicted_class_index)
print(predicted_label)

# If you also need to reverse transform the predicted class to its label:
# label_encoder = LabelEncoder() # you would ideally save & load the encoder, not fit it anew
# label_encoder.fit(your_original_data['Recommendation'])
# predicted_label = label_encoder.inverse_transform([predicted_class])
# print(f"Predicted Recommendation: {predicted_label[0]}")
