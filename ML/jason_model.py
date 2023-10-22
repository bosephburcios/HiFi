#Jason's Factorization Machine Model 

from google.colab import files
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import torch
import torch.nn as nn

# CSV File
uploaded = files.upload()
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

for epoch in range(1000):
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