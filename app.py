# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.preprocessing import LabelEncoder, StandardScaler
# from sklearn.ensemble import RandomForestClassifier
# import pickle

# app = Flask(__name__)
# CORS(app)

# # Load and preprocess the dataset
# data = pd.read_csv('Disease_symptom_and_patient_profile_dataset.csv')

# # Define symptom columns (adjust column names if necessary)
# symptom_columns = ['Fever', 'Cough', 'Fatigue', 'Difficulty Breathing']

# # Convert categorical symptom values to numeric
# for col in symptom_columns:
#     data[col] = data[col].map({'Yes': 1, 'No': 0})

# # Encode other categorical features if any
# label_encoder = LabelEncoder()
# data['Disease'] = label_encoder.fit_transform(data['Disease'])

# # Split features and target
# X = data[symptom_columns]
# y = data['Disease']

# # Train-test split
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Apply scaling
# scaler = StandardScaler()
# X_train = scaler.fit_transform(X_train)
# X_test = scaler.transform(X_test)

# # Train the model
# model = RandomForestClassifier()  # Using RandomForest as an example, change as needed
# model.fit(X_train, y_train)

# # Save the model and the scaler
# with open('model.pkl', 'wb') as f:
#     pickle.dump(model, f)

# with open('scaler.pkl', 'wb') as f:
#     pickle.dump(scaler, f)

# # Define Flask routes
# @app.route('/predict', methods=['POST'])
# def predict():
#     data = request.json
#     symptoms = data.get('symptoms')
    
#     # Convert symptoms to DataFrame
#     input_data = pd.DataFrame([symptoms], columns=symptom_columns)
    
#     # Map 'Yes'/'No' in symptoms to numeric values
#     for col in symptom_columns:
#         input_data[col] = input_data[col].map({'Yes': 1, 'No': 0})
    
#     # Scale input data using the saved scaler
#     with open('scaler.pkl', 'rb') as f:
#         scaler = pickle.load(f)
#     input_data_scaled = scaler.transform(input_data)
    
#     # Load model and make prediction
#     with open('model.pkl', 'rb') as f:
#         model = pickle.load(f)
#     prediction = model.predict(input_data_scaled)
    
#     # Convert numeric prediction back to label
#     predicted_disease = label_encoder.inverse_transform(prediction)[0]
    
#     return jsonify({'disease': predicted_disease})

# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import pandas as pd
# from sklearn.preprocessing import LabelEncoder, StandardScaler
# from sklearn.ensemble import RandomForestClassifier
# import pickle

# app = Flask(__name__)
# CORS(app)

# # Load and preprocess the dataset
# data = pd.read_csv('Disease_symptom_and_patient_profile_dataset.csv')

# # Define symptom columns
# symptom_columns = ['Fever', 'Cough', 'Fatigue', 'Difficulty Breathing']

# # Convert categorical symptom values to numeric
# for col in symptom_columns:
#     data[col] = data[col].map({'Yes': 1, 'No': 0})

# # Encode the target variable
# label_encoder = LabelEncoder()
# data['Disease'] = label_encoder.fit_transform(data['Disease'])

# # Split features and target
# X = data[symptom_columns]
# y = data['Disease']

# # Train-test split and scaling
# scaler = StandardScaler()
# X_train = scaler.fit_transform(X)
# model = RandomForestClassifier()
# model.fit(X_train, y)

# # Save the model and the scaler
# with open('model.pkl', 'wb') as f:
#     pickle.dump(model, f)

# with open('scaler.pkl', 'wb') as f:
#     pickle.dump(scaler, f)

# @app.route('/predict', methods=['POST'])
# def predict():
#     data = request.json
#     symptoms = data.get('symptoms', {})
    
#     # Convert symptoms to DataFrame
#     input_data = pd.DataFrame([symptoms], columns=symptom_columns)
    
#     # Map 'Yes'/'No' in symptoms to numeric values
#     for col in symptom_columns:
#         input_data[col] = input_data[col].map({'Yes': 1, 'No': 0})
    
#     # Scale input data using the saved scaler
#     with open('scaler.pkl', 'rb') as f:
#         scaler = pickle.load(f)
#     input_data_scaled = scaler.transform(input_data)
    
#     # Load model and make prediction
#     with open('model.pkl', 'rb') as f:
#         model = pickle.load(f)
#     prediction = model.predict(input_data_scaled)
    
#     # Convert numeric prediction back to label
#     predicted_disease = label_encoder.inverse_transform(prediction)[0]
    
#     return jsonify({'disease': predicted_disease})

# if __name__ == '__main__':
#     app.run(debug=True)

# 

# 
# 
from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
import pickle

app = Flask(__name__)
CORS(app)

# Load and preprocess the dataset
data = pd.read_csv('Disease_symptom_and_patient_profile_dataset.csv')

# Define symptom columns
symptom_columns = ['Fever', 'Cough', 'Fatigue', 'Difficulty Breathing']

# Convert categorical symptom values to numeric
for col in symptom_columns:
    data[col] = data[col].map({'Yes': 1, 'No': 0})

# Encode the target variable
label_encoder = LabelEncoder()
data['Disease'] = label_encoder.fit_transform(data['Disease'])

# Split features and target
X = data[symptom_columns]
y = data['Disease']

# Train-test split and scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X)
model = RandomForestClassifier()
model.fit(X_train, y)

# Save the model and the scaler
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        symptoms = data.get('symptoms', {})
        
        # Convert symptoms to DataFrame
        input_data = pd.DataFrame([symptoms], columns=symptom_columns)
        
        # Map 'Yes'/'No' in symptoms to numeric values
        for col in symptom_columns:
            input_data[col] = input_data[col].map({'Yes': 1, 'No': 0})
        
        # Scale input data using the saved scaler
        with open('scaler.pkl', 'rb') as f:
            scaler = pickle.load(f)
        input_data_scaled = scaler.transform(input_data)
        
        # Load model and make prediction
        with open('model.pkl', 'rb') as f:
            model = pickle.load(f)
        prediction = model.predict(input_data_scaled)
        
        # Convert numeric prediction back to label
        predicted_disease = label_encoder.inverse_transform(prediction)[0]
        
        return jsonify({'disease': predicted_disease})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/submit_answers', methods=['POST'])
def submit_answers():
    try:
        data = request.json
        answers = data.get('answers', [])
        
        # Process the answers and generate recommendations
        recommendations = ["Stay hydrated", "Get plenty of rest", "Consult a doctor if symptoms persist"]
        
        return jsonify(recommendations)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)