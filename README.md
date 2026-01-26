# Semiconductor Sector Data Analysis

## Overview
This repository contains a **time-series data analysis project** focused on the **semiconductor sector**, using historical daily stock market data from **2015 to 2025**.

The objective of this project is to apply **statistical data analysis techniques** including exploratory data analysis, probability analysis, regression, dimensionality reduction, and hypothesis testing to study patterns and dynamics within the semiconductor industry over time.

This project is developed as part of a **Data Analysis course (Semester 1)** and emphasizes **methodology, interpretation, and reproducibility**, rather than financial forecasting.

---

## Dataset
The analysis is based on a publicly available dataset originally collected using the `yfinance` Python library and sourced from Kaggle.

Link to the dataset - https://www.kaggle.com/datasets/farukece/semiconductor-stocks-and-the-ai-surge

**Dataset characteristics:**
- Daily time-series data
- Time period: **2015–2025**
- Multiple semiconductor companies
- Variables include:
  - Open price
  - High price
  - Low price
  - Close price (adjusted)
  - Trading volume
  - Company name and stock ticker

To improve interpretability and reduce unnecessary complexity, a **subset of representative semiconductor companies** was selected.  
These companies cover different segments of the semiconductor value chain, such as:
- AI / data-center focused companies
- Automotive and industrial-focused companies
- Memory manufacturers
- Semiconductor equipment suppliers
- Foundries

The raw dataset is preserved, and all preprocessing steps are fully reproducible.





---

## Analysis Scope
The project includes the following analysis components:

### 1. Data Preprocessing & Quality Analysis
- Parsing and validating timestamps
- Filtering the time range
- Removing non-informative columns
- Checking data consistency and completeness

### 2. Exploratory Data Analysis (EDA)
- Time-series visualization
- Distribution analysis
- Rolling statistics
- Correlation analysis (Pearson and Spearman)

### 3. Probability & Event Analysis
- Definition of statistically meaningful events
- Empirical and conditional probability estimation

### 4. Statistical Theory Applications
- Demonstration of the Law of Large Numbers
- Illustration of the Central Limit Theorem using real data

### 5. Regression & Predictive Modeling
- Time-based regression models
- Feature engineering using historical values
- Residual analysis and model interpretation

### 6. Dimensionality Reduction & Hypothesis Testing
- Principal Component Analysis (PCA)
- Non-linear dimensionality reduction (t-SNE / UMAP)
- Statistical hypothesis tests to compare groups of companies

---



