# Text Analysis and Classification using ML

## 📌 Project Overview
This project consists of two main tasks:
1. Resume Information Extraction using Regular Expressions
2. Sentiment Classification using Machine Learning models

---

## 🧩 Task 1: Resume Information Extractor

A rule-based Python script that extracts:
- 📧 Email addresses
- 📱 Phone numbers

from resume text using regular expressions.

### 🔹 Output
- Extracted data is stored in a structured `output.json` file

---

## 🧠 Task 2: Sentiment Analysis

A machine learning-based system that classifies text into sentiments such as positive or negative.

### 🔹 Process
- Text preprocessing (cleaning, tokenization)
- Text vectorization using TF-IDF
- Model training and evaluation

### 🤖 Models Used
- Naive Bayes
- SVM (LinearSVC)
- Random Forest

---

## 🛠 Tools & Libraries
- Python
- scikit-learn
- nltk
- matplotlib
- textblob

---

## 📊 Evaluation Metrics
- Accuracy
- Precision
- Recall
- F1 Score

---

## 📈 Output
- Model comparison graph
- Sentiment predictions
- Extracted resume data in JSON format

---

## 📂 Dataset
The dataset used for sentiment analysis is not included in this repository due to its large size.

👉 Download it from here:
https://drive.google.com/file/d/1QtBFsKe13SzgKomT3RGjwKig80hHjGqD/view

After downloading, place it in the project folder as:
dataset.csv

---

## ▶️ How to Run

1. Install required libraries:
   pip install pandas scikit-learn nltk matplotlib seaborn textblob

2. Run Resume Extractor:
   python resume.py

3. Run Sentiment Analysis:
   Open textnalyser.ipynb and execute all cells

4. Ensure dataset.csv is in the same folder

---

## 📁 Project Structure

Text-Analysis-ML/
│── resume.py
│── output.json
│── textanalyser.ipynb
│── README.md

---

## 🎯 Conclusion
This project demonstrates both rule-based and machine learning approaches for text analysis. The resume extractor efficiently retrieves structured information, while the sentiment classifier shows how different ML models perform on textual data.
