#Jason's Factorization Machine Model (99.2% Accurate on 8000 Epochs, but run at 500 for time)
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import torch
import torch.nn as nn

# CSV File
data = pd.read_csv('synthetic_data.csv')

# prepare Data for FM, use label encoder for any value that can be interpreted

label_encoder_location = LabelEncoder()
label_encoder_weather = LabelEncoder()

data['Location'] = label_encoder_location.fit_transform(data['Location'])
data['Weather'] = label_encoder_weather.fit_transform(data['Weather'])

X = data[['Heartbeat', 'Hours_Worked', 'Weather', 'Location']].values.astype(np.float32)

label_encoder_recommendation = LabelEncoder()
y = label_encoder_recommendation.fit_transform(data['Recommendation'])



# define the Factorization Machine Model

class FactorizationMachine(nn.Module):
    def __init__(self, input_dim, factor_dim, num_classes):
        super(FactorizationMachine, self).__init__()
        self.linear = nn.Linear(input_dim, num_classes, bias=True)
        self.v = nn.Parameter(torch.randn((input_dim, factor_dim)))

    def forward(self, x):
        linear_term = self.linear(x)
        interaction_term = 0.5 * torch.sum((torch.mm(x, self.v) ** 2) - torch.mm(x ** 2, self.v ** 2), dim=1, keepdim=True)
        output = linear_term + interaction_term
        return output

input_dim = X.shape[1]
num_classes = len(label_encoder_recommendation.classes_)
factor_dim = 10
fm_model = FactorizationMachine(input_dim, factor_dim, num_classes)

# Step 7: Train the Factorization Machine
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(fm_model.parameters(), lr=0.001)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train = torch.tensor(X_train, dtype=torch.float32)
y_train = torch.tensor(y_train, dtype=torch.long)

for epoch in range(500):
    optimizer.zero_grad()
    output = fm_model(X_train)
    loss = criterion(output, y_train)
    loss.backward()
    optimizer.step()
    print(f'Epoch {epoch+1}, Loss: {loss.item():.4f}')


# Step 8: Make Recommendations
def recommend(user_input):
    user_input[2] = label_encoder_weather.transform([user_input[2]])[0]  # Encode weather
    user_input[3] = label_encoder_location.transform([user_input[3]])[0]  # Encode location
    x = torch.tensor([user_input], dtype=torch.float32)
    output = fm_model(x)
    recommendations = output.detach().numpy().flatten()
    return recommendations

# test
user_input = [89, 12, 'Snowy', 'Suburban']
recommendations = recommend(user_input)

predicted_class_index = recommendations.argmax()

decoded_recommendation = label_encoder_recommendation.inverse_transform([predicted_class_index])[0]
print("Recommendations:", decoded_recommendation)


#model save time
torch.save(fm_model.state_dict(), 'jason_model.pth')

"""
import joblib
from my_factorization_machine_model import FactorizationMachine

# Assuming 'fm_model' is your PyTorch model
torch.save(fm_model.state_dict(), 'fm_model_state.pth')
joblib.dump(label_encoder_weather, 'label_encoder_weather.joblib')
joblib.dump(label_encoder_location, 'label_encoder_location.joblib')
joblib.dump(label_encoder_recommendation, 'label_encoder_recommendation.joblib')

# Load label encoders
label_encoder_weather = joblib.load('label_encoder_weather.joblib')
label_encoder_location = joblib.load('label_encoder_location.joblib')
label_encoder_recommendation = joblib.load('label_encoder_recommendation.joblib')

# Initialize model
input_dim = X.shape[1]
num_classes = len(label_encoder_recommendation.classes_)
factor_dim = 10
fm_model = FactorizationMachine(input_dim, factor_dim, num_classes)

# Load model state dictionary
fm_model.load_state_dict(torch.load('fm_model_state.pth'))
fm_model.eval()  # Set the model to evaluation mode

def recommend(user_input):
    # Encode weather and location
    user_input[2] = label_encoder_weather.transform([user_input[2]])[0]
    user_input[3] = label_encoder_location.transform([user_input[3]])[0]

    # Prepare input tensor
    x = torch.tensor([user_input], dtype=torch.float32)

    # Get prediction
    with torch.no_grad():
        output = fm_model(x)
        recommendations = output.detach().numpy().flatten()

    # Decode recommendation
    predicted_class_index = recommendations.argmax()
    decoded_recommendation = label_encoder_recommendation.inverse_transform([predicted_class_index])[0]
    return decoded_recommendation

# Test
user_input = [89, 12, 'Snowy', 'Suburban']
recommendations = recommend(user_input)

print("Recommendations:", recommendations)
"""