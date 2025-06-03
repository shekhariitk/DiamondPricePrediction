# 💎 Diamond Price Prediction

A machine learning project to predict the price of diamonds based on key features such as carat, cut, color, clarity, and more. Built with Python, Scikit-learn, and Streamlit for deployment.

---

## 📑 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Dataset](#dataset)
- [EDA Summary](#eda-summary)
- [Modeling Pipeline](#modeling-pipeline)
- [Evaluation Metrics](#evaluation-metrics)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Deployment](#deployment)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

---

## 🔍 Overview

Diamonds are priced based on several categorical and numerical features. This project applies data science and machine learning to estimate the price of a diamond using features like:

- Carat
- Cut
- Color
- Clarity
- Depth
- Table
- Dimensions

---

## ✨ Features

- Predict diamond price instantly
- Handles both numerical and categorical data
- Interactive Streamlit UI
- Modularized ML pipeline
- Scalable and production-ready code
- Hyperparameter tuning and model selection
- Visual EDA using Seaborn

---

## ⚙️ Tech Stack

- Python 3.8+
- Pandas, NumPy
- Scikit-learn
- XGBoost, Random Forest
- Matplotlib, Seaborn,
- Flask
- Jupyter Notebook

---

## 📂 Dataset

- 📁 Source: [Kaggle Diamond Dataset](https://www.kaggle.com/datasets/shivam2503/diamonds)
- 🧮 1,93,940 rows × 10 columns
- 💠 Features:
  - `carat`: weight of the diamond
  - `cut`: quality of the cut (Fair, Good, Very Good, Premium, Ideal)
  - `color`: from D (best) to J (worst)
  - `clarity`: ranging from I1 (worst) to IF (best)
  - `depth`, `table`, `x`, `y`, `z`
  - `price`: target variable

---

## 📊 EDA Summary

- Carat is the most influential feature on price
- Ideal cut and better clarity significantly increase price
- Poor color grades (H, I, J) reduce price
- Diamonds with depth between 60–63% are optimally priced

Visualizations include:

- Correlation heatmaps
- Boxplots for categorical vs price
- Pairplots for continuous variables
- Histograms and KDE plots

---

## 🧠 Modeling Pipeline

- Label encoding for categorical features
- Outlier treatment using IQR and Z-score
- Feature scaling using StandardScaler
- Train-test split (80/20)
- Models evaluated:
  - Linear Regression
  - Decision Tree
  - Random Forest
- Hyperparameter tuning using GridSearchCV

---

## 📈 Evaluation Metrics

| Model            | R² Score | RMSE   | MAE    |
|------------------|----------|--------|--------|
| Linear Regression | 0.86     | 980    | 720    |
| Random Forest     | 0.97     | 550    | 390    |

---

## 🛠 Installation

Clone the repository and install dependencies:

```bash
git https://github.com/shekhariitk/DiamondPricePrediction.git
cd diamond-price-prediction
pip install --upgrade -r requirements.txt
