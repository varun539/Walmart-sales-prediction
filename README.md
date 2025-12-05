# 🛒 Walmart Weekly Sales Prediction

Predict weekly sales for Walmart stores using **Machine Learning**. This project combines historical sales, store info, and economic indicators to help Walmart optimize inventory, plan promotions, and maximize revenue.  

---

## 🎯 Business Objective

- Forecast **weekly sales** for each store and department.  
- Identify **high-performing stores/departments** and seasonal trends.  
- Provide actionable insights to **increase profitability** and reduce overstock/understock situations.  
- Support decision-making for **marketing promotions** and **holiday planning**.  

---

## 📂 Dataset

The data is from the **Kaggle Walmart Sales Forecasting competition**:

| File | Description |
|------|-------------|
| `train.csv` | Historical weekly sales per store & department |
| `features.csv` | Store-level features: fuel price, markdowns, CPI, unemployment, holidays |
| `stores.csv` | Store type & size information |
| `test.csv` | Test data for prediction |

---

## 🔍 Exploratory Data Analysis (EDA) & Insights

- **Sales Distribution:** Outliers detected, overall weekly trends analyzed.  
- **Holiday Impact:** Sales spike during Thanksgiving & Christmas.  
- **Store Type:** Type A stores have highest average sales.  
- **Department Performance:** Certain departments consistently outperform others.  
- **Correlation:** Store size positively correlates with sales, markdown promotions slightly boost revenue, fuel price and unemployment have weak negative impact.  

💡 **Business Insight:** Understanding these patterns helps Walmart **allocate inventory, plan promotions, and optimize revenue per store**.

---

## 🛠️ Feature Engineering

- Extracted **Year, Month, Week, DayOfWeek** from `Date`.  
- Created **IsWeekend** to capture weekend sales trends.  
- Normalized sales using **SalesPerSize** for fair comparison across stores.  
- Filled missing markdown values with 0.  
- Label encoded categorical variables like **Type**.  

---

## 💻 Modeling & Results

We trained multiple models and compared performance:

| Model | R² Score | RMSE | MAE | Business Impact |
|-------|----------|------|-----|----------------|
| Random Forest | 0.9995 | 511.40 | 187.58 | Highly accurate predictions → can optimize stock and promotions |
| XGBoost | 0.9938 | 1794.26 | 601.00 | Good, but less accurate → slightly higher risk of misforecast |
| Linear Regression | Baseline | - | - | For comparison, simple trends capture only basic patterns |

✅ **Conclusion:** Random Forest is selected for production-level prediction.

---

## 📈 Business Impact / Actionable Insights

1. **Inventory Optimization:** Accurate sales forecast reduces overstock and stockouts.  
2. **Promotion Planning:** Identify which markdowns actually boost sales.  
3. **Holiday Strategy:** Prepare for spikes during holidays to maximize revenue.  
4. **Store Expansion & Layout Decisions:** Insights from Type & Size correlation help strategic decisions.  
5. **Department Focus:** Allocate resources to consistently high-performing departments.  

---

## 🚀 Next Steps

- Deploy as a **Streamlit Web App** for Walmart managers.  
- Extend forecasting to multiple years & integrate real-time data.  
- Experiment with **time series models** (Prophet, LSTM) for advanced forecasting.  
- Include **interactive dashboards** for business stakeholders.  

---

## 📦 Project Files

- `sales_py.py` → Data preprocessing, EDA, feature engineering, and modeling.  
- `final_rf_model.pkl` → Trained Random Forest model for prediction.  
- `README.md` → Project documentation.  

---

## 🔗 References

- [Kaggle Walmart Sales Forecasting](https://www.kaggle.com/c/walmart-recruiting-store-sales-forecasting)  
- Python libraries: `pandas`, `numpy`, `scikit-learn`, `xgboost`, `matplotlib`, `seaborn`, `joblib`  

---

