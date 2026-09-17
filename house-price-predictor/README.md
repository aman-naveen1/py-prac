# 🏠 House Price Predictor

An end-to-end machine learning project that predicts median house values using the California Housing dataset.

The project is designed as a practical data-science portfolio piece: it includes data loading, exploratory analysis, model comparison, evaluation, feature importance, and an interactive Streamlit prediction app.

## Tech Stack

- Python
- Pandas / NumPy
- Scikit-learn
- Matplotlib
- Streamlit

## ML Workflow

```text
California Housing Dataset
        ↓
Data validation & exploration
        ↓
Train / test split
        ↓
Baseline: Linear Regression
        ↓
Random Forest Regression
        ↓
Cross-validation & evaluation
        ↓
Feature importance analysis
        ↓
Interactive Streamlit app
```

## Features

The model uses eight numerical features from the California Housing dataset:

| Feature | Description |
|---|---|
| MedInc | Median income in the block group |
| HouseAge | Median house age |
| AveRooms | Average number of rooms |
| AveBedrms | Average number of bedrooms |
| Population | Block-group population |
| AveOccup | Average household occupancy |
| Latitude | Geographic latitude |
| Longitude | Geographic longitude |

The target is **MedHouseVal**, the median house value for a block group, represented in units of $100,000.

## Models

Two regression models are compared:

1. **Linear Regression** — simple, interpretable baseline.
2. **Random Forest Regressor** — nonlinear ensemble model used for the final predictor.

Evaluation uses:

- MAE — Mean Absolute Error
- RMSE — Root Mean Squared Error
- R² — coefficient of determination
- 5-fold cross-validation for the Random Forest

## Run locally

### 1. Clone the repository

```bash
git clone https://github.com/aman-naveen1/py-prac.git
cd py-prac/house-price-predictor
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run model analysis

```bash
python train_model.py
```

This downloads the dataset through scikit-learn, trains both models, prints evaluation metrics, and saves feature-importance and prediction-vs-actual plots to `artifacts/`.

### 4. Launch the app

```bash
streamlit run app.py
```

## Project Structure

```text
house-price-predictor/
├── app.py
├── train_model.py
├── requirements.txt
├── .gitignore
├── README.md
└── artifacts/
    └── .gitkeep
```

## Why this project matters

Rather than only fitting a model, this project demonstrates a complete beginner data-science workflow: understanding the data, establishing a baseline, comparing models, using appropriate regression metrics, inspecting model behavior, and exposing the final model through a small application.

## Future Improvements

- Add hyperparameter tuning with `RandomizedSearchCV`
- Add SHAP-based model explanations
- Add a larger dashboard for exploratory analysis
- Package the trained model with joblib for faster app startup
- Add automated tests and GitHub Actions CI
