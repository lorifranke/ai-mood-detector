import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Step 1: Load the synthetic data
data = pd.read_csv('training_data.csv')

# Step 2: Prepare features and labels
X = data['text']
y = data['mood']

# Step 3: Vectorize the text (convert words to numbers)
vectorizer = TfidfVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Step 4: Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)

# Step 5: Train the model
model = LogisticRegression()
model.fit(X_train, y_train)

# Step 6: Evaluate the model
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"Model Accuracy: {accuracy:.2f}")

# Step 7: Make a prediction on new text
new_text = ["I feel great today", "This is disappointing", "It's just average"]
new_vectorized = vectorizer.transform(new_text)
new_predictions = model.predict(new_vectorized)

mood_map = {0: "Negative", 1: "Neutral", 2: "Positive"}
for text, pred in zip(new_text, new_predictions):
    print(f"Predicted Mood for '{text}': {mood_map[pred]}")
