# -*- coding: utf-8 -*-
"""Email_Spam_Identification_1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1asbOKii9ev4PC1zBSn3xEHidp5bMV9Bu
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn. linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

encodings = ['utf-8', 'latin','ISO-8859-1', 'Cp1252']
file_path = 'https://raw.githubusercontent.com/kapilpoonia05/Oasis-task/main/Email%20Spam%20Identification/spam.csv'

for encoding in encodings:
    try:
        raw_email_data = pd.read_csv(file_path, encoding=encoding)
        print(f"File successfully read with encoding: {encoding}")
        break
    except UnicodeDecodeError:
        print(f"Failed to read with encoding: {encoding}")
        continue

if 'raw_email_data' in locals():
    print("Csv file has been successfully loaded.")
else:
    print("All encoding attempts failed. Unable to read the Csv file.")

raw_email_data

email_data = raw_email_data.where((pd.notnull (raw_email_data)),' ')
email_data.head()

email_data.drop(columns=['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], inplace=True)

email_data.head()

email_data.shape

email_data.replace({'v1': {'spam':0, 'ham': 1}}, inplace=True)

email_data.head()

X = email_data['v2']
Y = email_data['v1']

X

Y

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2, random_state=3)

X.shape

X_train

print(X.shape, X_train.shape, X_test.shape)

# transform the text data to feature vectors that can be used as input to the Logistic regression
feature_extraction = TfidfVectorizer(min_df = 1, stop_words='english', lowercase=True )

X_train_features = feature_extraction.fit_transform(X_train)
X_test_features = feature_extraction.transform(X_test)
# convert Y_train and Y_test values as integers
Y_train = Y_train.astype('int')
Y_test = Y_test.astype('int')

"""**Logistic Regression**"""

model = LogisticRegression()

model.fit(X_train_features, Y_train)

prediction_on_training_data =model.predict(X_train_features)

accuracy_on_training_data = accuracy_score(Y_train, prediction_on_training_data)
accuracy_on_training_data

# prediction on test data
prediction_on_test_data = model.predict(X_test_features)
accuracy_on_test_data = accuracy_score(Y_test,prediction_on_test_data)
accuracy_on_test_data

input_sms=["Nah I don't think he goes to usf, he lives around here though"]
#convert text to feature vectors
input_data_features =feature_extraction.transform(input_sms)
# making prediction
prediction = model.predict (input_data_features)
print (prediction)
if (prediction[0]==1):
  print ('Ham sms')
else:
  print ('Spam sms')