# SMS Spam Classifier

## Overview
This repository contains an SMS Spam Classifier developed using machine learning techniques. The system is designed to distinguish between spam and non-spam (ham) text messages, helping users filter unwanted SMS communications.

## Features
- **Spam Detection**: Classifies SMS messages as spam or non-spam.
- **User Interface**: Interactive web application built using Streamlit.
- **Efficient Models**: Utilizes multiple machine learning models for accurate predictions.

## Technologies Used
- Python
- Streamlit
- Pandas
- Scikit-learn
- NLTK (Natural Language Toolkit)
- Requests

## Screenshots
Here are some screenshots of the SMS Spam Classifier:

![Screenshot 1](screenshots/screenshot1.png)
*Screenshot of the Streamlit app main interface*

![Screenshot 2](screenshots/screenshot2.png)
*Screenshot showing classification results*

## How to Run the Project
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/radhatumbre/SMS-Spam-Classifier.git
   cd SMS-Spam-Classifier
   ```

2. **Install the Required Libraries**:
   Create a virtual environment and activate it (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

   Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Jupyter Notebook for Model Training**:
   Open and run `sms-spam-detection.ipynb` to train the model and save the necessary pickle files.

4. **Run the Streamlit App**:
   ```bash
   streamlit run main.py
   ```

5. **Usage**:
   - Open the Streamlit app in your web browser.
   - Select the type of SMS message (spam or ham) and enter the text.
   - Click the "Predict" button to see the classification result.

