# Final Davletaliyev Podcast listening time predictions

## Overview
A basic solution for the Kaggl competition: Predicting Podcast Listening Time.
Goal: Predict how many minutes users will listen to podcast episodes.

## Implementation Steps

### 1. Data Loading
Load training data  and test data .

### 2. Feature Identification
Automatically separates features into two types:
- Categorical: Text/category columns for example Genre, Host, Day
- Numerical: Number columns dor example Episode_Length, Rating

### 3. Data Preprocessing
Label Encoding converts categorical variables to numbers. 

### 4. Model Training
Random Forest Regressor is  100 decision trees in this case. Each tree votes on the prediction, and the average of all votes becomes the final prediction. It does non-linear relationships well.

Parameters:
- n_estimators=100: Number of trees
- random_state=42: For reproducibility
- n_jobs=-1: Use all CPU cores(looked it up online,for me still took a while)

### 5. Prediction & Submission
Predict listening time for test set and create submission file in Kaggle format.

## Evaluation

### Strengths
- Simple and fast, is what i wanted to say ,but not only the RandomForest loaded for good 3 min it also crashed my pc once
- No overfitting risk with single model and no tuning
- Clear logic flow, easy to understand


### Weaknesses
- Can't check results before submitting to kaggle
- Default parameters not optimized for this specific problem
- It doesn't handle extreme values 

### Expected Performance
Didn't expect much got around 1300 out of 3500 submissions

## Potential Improvements

1. For kaggle it is not needed, but could check results yourself
2. Use other tools beside RandomForest
3. Ability to handle outliers

### Sources 

1.https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html
2.https://www.kaggle.com/learn/intro-to-machine-learning
3.https://www.kaggle.com/learn/feature-engineering

