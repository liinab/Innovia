import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from joblib import dump


# Load your training dataset
df_train = pd.read_csv(r'C:\Users\bergs\Desktop\training_dataset(2016-2023).csv')
df_train['description'] = df_train['description'].fillna('')


# Split your training dataset into training and test datasets
X = df_train['description']
y = df_train['it_security']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Initialize the TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer(use_idf=True)


# Fit and transform the training data
X_train_tfidf = tfidf_vectorizer.fit_transform(X_train)


# Transform the test data
X_test_tfidf = tfidf_vectorizer.transform(X_test)


# Initialize the Logistic Regression model
model = LogisticRegression(max_iter=250)


# Train the model with the training data
model.fit(X_train_tfidf, y_train)


# Make predictions on the training data
y_train_pred = model.predict(X_train_tfidf)


# Calculate the accuracy on the training data
train_accuracy = accuracy_score(y_train, y_train_pred)
st.write(f'Training set accuracy: {train_accuracy}')


# Make predictions on the test data
y_test_pred = model.predict(X_test_tfidf)


# Calculate the accuracy on the test data
test_accuracy = accuracy_score(y_test, y_test_pred)
st.write(f'Test set accuracy: {test_accuracy}')


# Save the trained model
dump(model, 'job_classification_model.joblib')


# Save the fitted TF-IDF vectorizer
dump(tfidf_vectorizer, 'tfidf_vectorizer.joblib')


# Load your full dataset
df_full = pd.read_csv(r'C:\Users\bergs\Desktop\full_dataset(2016-2023).csv')
df_full['description'] = df_full['description'].fillna('')
X_full = df_full['description']


# Transform the full dataset
X_full_tfidf = tfidf_vectorizer.transform(X_full)


# Make predictions on the full dataset
y_full_pred = model.predict(X_full_tfidf)


# Save the predictions
df_full['it_security_prediction'] = y_full_pred


# Calculate the percentage of jobs classified as IT-security oriented
it_security_jobs_percentage = (y_full_pred.sum() / len(y_full_pred)) * 100
st.write(f"Percentage of jobs classified as IT-security oriented: {it_security_jobs_percentage}%")


# Calculate the percentage of IT-security jobs for each year
it_security_jobs_by_year = df_full.groupby('year')['it_security_prediction'].mean() * 100
st.write(it_security_jobs_by_year)


# Save the full dataset with predictions and percentages
df_full.to_csv('full_dataset_with_predictions.csv', index=False)