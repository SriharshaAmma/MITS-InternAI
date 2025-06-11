import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
import os

# Load dataset
df = pd.read_csv('data/success.csv')

# Features and label
X = df[['CGPA', 'Projects', 'Internships', 'Participation']]
y = df['Success']

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Save model
os.makedirs('models', exist_ok=True)
with open('models/success_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Model trained and saved to models/success_model.pkl")
