import streamlit as st
import nltk
from nltk.corpus import stopwords
import string
from nltk.stem.porter import PorterStemmer
import pickle

ps = PorterStemmer()
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)



tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))
# print("helloo")

st.title("Email/SMS Spam Classifier")

input_sns = st.text_input("Enter the message")

if st.button('Predict'):
    # Step 1: preprocess
    transform_sns = transform_text(input_sns)

    # Step 2: vectorize
    vector_input = tfidf.transform([transform_sns])

    # Step 3: predict
    result = model.predict(vector_input)

    # Step 4: display
    if result==1:
        st.header("SPAM")
    else:
        st.header("NOT SPAM")


