Walmart Weekly Sales Forecasting

End-to-end Machine Learning project to predict weekly sales for Walmart stores using historical, economic, and promotional data to support inventory planning and demand forecasting.

🔹 Problem Statement

Retail chains struggle to accurately forecast weekly demand because sales depend on multiple dynamic factors:

Seasonality & holidays

Promotional markdowns

Store size and type

Economic indicators (fuel price, CPI, unemployment)

The goal of this project was to build an accurate ML model that predicts weekly sales at Store–Department level to improve:

✅ Inventory forecasting
✅ Promotion planning
✅ Workforce scheduling

🔹 Dataset

Source: Kaggle – Walmart Store Sales Forecasting

Merged 3 datasets:

train.csv → sales history

features.csv → economic + promotion data

stores.csv → store metadata

📊 Total Records: 421,570 rows

🔹 Data Preprocessing & Feature Engineering
✅ Data Preparation

Merged all datasets on Store and Date

Filled missing promotional markdown values with 0

Converted Date column to datetime format

✅ Feature Engineering

Created new features:

Year, Month, Week, DayOfWeek

IsWeekend

SalesPerSize (normalized sales by store size)

Label encoding for categorical variables

🔹 Exploratory Data Analysis (EDA)

Key insights from the data:

📈 Holiday weeks show large sales spikes
🏬 Type A stores consistently sell more than Types B & C
📦 Larger store size correlates positively with sales
💸 Markdown promotions (especially MarkDown1 & MarkDown2) boost revenue
🛢 Fuel price & unemployment have weak negative correlations
📊 Certain departments outperform consistently across stores

🔹 Modeling
Models Tested

Linear Regression (baseline)

Random Forest Regressor ✅ (Best performer)

XGBoost Regressor

Hyperparameters tuned using RandomizedSearchCV.

✅ Final Model Performance
Metric	Random Forest
R² Score	0.9995
RMSE	511.40
MAE	187.58

✅ Random Forest showed the lowest prediction error and highest accuracy, making it the final model choice.

🔹 Technology Stack

Python

pandas, numpy

scikit-learn

XGBoost

matplotlib, seaborn

Joblib (model export)

🔹 Model Deployment

The trained Random Forest model is saved as:

final_rf_model.pkl


🔜 Deployment Plan:
Build a Streamlit Web App where users input store details and receive real-time sales predictions.

🔹 Business Impact

This project demonstrates how machine learning can be used to:

✅ Forecast inventory demand
✅ Optimize promotions & staffing
✅ Improve profitability through data-driven decisions

👨‍💻 Author

Varun B
Aspiring Data Scientist

🌐 GitHub: https://github.com/
<varun539>
📁 Portfolio: <your_portfolio_link>
