# beverage_price_prediction

## Problem Statement
To predict the price range of energy drinks typically purchased by consumers based on their demographic details, consumption habits, preferences, and other behavioral factors. Developing a predictive model that uses respondent data (e.g., age, gender, income level, consumption frequency, brand awareness, and other attributes) to accurately categorize the energy drink price range into predefined categories.

## Project Structure

- **artifacts/**: Contains models joblib files.
- **main**: Contains actual streamlit codes.
- **prediction_helper**: contains methods used to load models and predict the output and display it in frontend
- **requirements.txt**: Lists the required Python packages.
- **README.md**: Provides an overview and instructions for the project.

## Skills gained
- **Machine learning**
- **Data cleaning**
- **EDA**
- **Data preprocessing**


## Project Explanation

These are the steps I followed during this project:
1. Data cleaning
2. EDA (exploratory data analysis)
3. Feature Engineering
4. Hyper parameter tuning
5. Model training and evaluation
6. Streamlit Deployment


🔍 Key Steps I Followed

1️⃣ Data Cleaning:

1. Removed duplicates and outliers
2. Handled missing values and corrected categorical data

2️⃣ Feature Engineering:

1. Created new features like Age Groups, Brand Awareness Score, and Zone Affluence Score
2. Added a Brand Switching Indicator to enhance prediction accuracy

3️⃣ Predictive Modeling:

4. Tested models like Logistic Regression, Random Forest, XGBoost, and more
5. Selected XGBoost as the best-performing model

4️⃣ Experiment Tracking with MLflow:

Tracked experiments, logged parameters and metrics, and compared model performance using MLflow

5️⃣ Web App Deployment with Streamlit:

Built a user-friendly interface where users can input data and get real-time predictions
Leveraged Streamlit for interactive web app deployment


## Demo

[https://ml-project-credit-risk-modeling.streamlit.app/](https://beveragepriceprediction.streamlit.app/)


## Screenshots
![Screenshot 2024-12-28 172905](https://github.com/user-attachments/assets/7a3f665f-d9f5-4b16-8235-8133be940aad)

## Demo video
https://github.com/user-attachments/assets/11f2dd94-3dcf-4d33-b16a-97b24b330f36


## Setup Instructions

1. **Clone the repository**:
   ```bash
   https://github.com/siddu28/beverage_price_prediction.git

1. **Install dependencies:**:   
   ```commandline
    pip install -r requirements.txt
   ```

1. **Run the Streamlit app:**:   
   ```commandline
    streamlit run main.py
   ```
    
