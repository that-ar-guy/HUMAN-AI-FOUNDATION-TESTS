# **Task 2: Sentiment and Crisis Risk Classification (NLP and Text Processing)**

## **Overview**
This project applies **Natural Language Processing (NLP)** techniques to classify Reddit posts based on **sentiment** and **crisis risk levels**. The goal is to analyze user-generated text to identify **high-risk, moderate concern, and low concern** discussions related to mental health.

## **Methodology**
We employ the following approaches:

### **1️⃣ Sentiment Analysis (VADER)**
- **Tool Used:** `SentimentIntensityAnalyzer` from NLTK.
- **Labels:**
  - **Positive** (Score ≥ 0.05)
  - **Neutral** (Score between -0.05 and 0.05)
  - **Negative** (Score ≤ -0.05)
- Each post’s sentiment is determined using **VADER** (designed for social media text).

### **2️⃣ Crisis Risk Classification (TF-IDF + ML)**
- **Feature Extraction:**
  - `TfidfVectorizer` with `stop_words='english'` to remove noise.
- **Risk Level Categorization:**
  - **High-Risk:** Contains direct crisis terms (e.g., "I don't want to be here," "suicide").
  - **Moderate Concern:** Indicates struggles (e.g., "I feel lost," "depressed").
  - **Low Concern:** General mental health discussions (e.g., "self-care," "therapy").
- **Classification Model:**
  - `RandomForestClassifier` is used for classification.
  - `Pipeline` integrates preprocessing (TF-IDF) and modeling.
  - Model is trained on labeled data and evaluated using **accuracy, precision, recall, and F1-score**.

## **Implementation**
### **🔹 Data Preprocessing**
- Reddit dataset is loaded from a CSV file.
- **Cleaned text** is used from task 1(no additional cleaning required).
- Sentiment labels and risk levels are assigned to each post.

### **🔹 Machine Learning Model**
- TF-IDF vectorization extracts text features.
- A **RandomForestClassifier** is trained to predict crisis risk levels.
- Model is evaluated using a train-test split.

### **🔹 Visualization**
- **Sentiment Distribution:** A bar plot shows the proportion of **positive, neutral, and negative** posts.
- **Crisis Risk Level Distribution:** A bar plot visualizes the classification into **high-risk, moderate, and low concern**.

## **Results & Performance**
- **Classification Report** provides model accuracy and performance metrics.
- **Exported Dataset:** Final results, including sentiment and predicted risk levels, are saved as `classified_reddit_posts.csv`.

## **Future Improvements**
- Implement **BERT embeddings** for better text representation.
- Fine-tune **hyperparameters** to improve classification accuracy.
- Expand **high-risk keyword detection** using similarity-based matching.

---