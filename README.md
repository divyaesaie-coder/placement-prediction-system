# placement-prediction-system
Machine learning web application that predicts student placement status using Random Forest, KNN, and Logistic Regression with Flask deployment.
# Placement Prediction System

## Overview
A machine learning web application that predicts whether a student will be placed based on academic performance, technical skills, and profile data.

## Problem Statement
Can student placement status be predicted using student academic and skill-related factors?

## Dataset
- Source: Kaggle Student Placement Dataset
- Records: 45,000+
- Features:
  - Age
  - CGPA
  - Internships
  - Projects
  - Coding Skills
  - Communication Skills
  - Aptitude Test Score
  - Soft Skills Rating
  - Certifications
  - Backlogs
  - Gender
  - Degree
  - Branch

## Preprocessing
- Removed unnecessary columns (Student_ID)
- One-Hot Encoding
- Dummy Variable Trap handling
- Feature Scaling using StandardScaler
- Train-Test Split

## Machine Learning Models Used
- Logistic Regression
- K-Nearest Neighbors (KNN)
- Random Forest

## Model Evaluation
- Accuracy Score
- Cross Validation
- Model Comparison
- Feature Importance Analysis

## Results
- Logistic Regression: 86.46%
- KNN: 90.94%
- Random Forest: 100%
- Cross Validation Average: 100%

Random Forest performed best and was selected for deployment.

## Deployment
Built a Flask web application where users can:
- Enter student details
- Select profile information
- Predict placement status

## Tech Stack
- Python
- Pandas
- NumPy
- Scikit-learn
- Flask
- HTML
- CSS

## Workflow
Dataset Collection
→ Data Understanding
→ Data Preprocessing
→ Feature Engineering
→ Model Training
→ Model Comparison
→ Model Selection
→ Model Saving using Pickle
→ Flask Deployment
