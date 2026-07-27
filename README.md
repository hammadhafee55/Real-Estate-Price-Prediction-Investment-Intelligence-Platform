## Real Estate Price Prediction & Investment Intelligence Platform

End-to-end machine learning platform designed to predict real estate property prices and evaluate investment potential using property, location, market, and financial features.

The platform combines machine learning models with a Flask API and an interactive web interface to provide property price predictions, investment scores, investment ratings, and recommended investment strategies.

---

## Key Features

### Property Price Prediction

Predicts the estimated market price of a property based on:

* City and neighbourhood type
* Property type
* Number of bedrooms and bathrooms
* Property area
* Property age
* Property condition
* Furnishing status
* Parking availability
* Pool and garden availability
* Distance from city centre
* Distance from schools and hospitals
* Crime rate
* School rating
* Local amenities
* Days on market

---

### Investment Intelligence

The platform evaluates the investment potential of a property using:

* Market growth rate
* Gross rental yield
* Location quality
* Crime rate
* School rating
* Local amenities
* Property characteristics
* Market demand indicators

The system generates an investment score from:

```text
0 - 100
```

---

### Investment Rating Classification

Properties are classified into different investment categories:

| Score Range | Rating    |
| ----------- | --------- |
| 0–40        | Low       |
| 40–60       | Moderate  |
| 60–75       | Good      |
| 75–100      | Excellent |

---

### Recommended Investment Strategy

Based on the predicted investment score, the system provides a recommendation:

* Buy & Rent / Strong Investment
* Buy for Appreciation
* Evaluate Carefully
* Avoid / High Risk

---

## Machine Learning Models

### 1. Property Price Prediction

Model:

```text
XGBoost Regressor
```

Target:

```text
Property_Price
```

Evaluation metrics:

* Mean Absolute Error
* Root Mean Squared Error
* R² Score

---

### 2. Investment Score Prediction

Model:

```text
XGBoost Regressor
```

Target:

```text
Investment_Score
```

The model predicts the investment potential of a property on a scale of 0 to 100.

---

### 3. Investment Rating Classification

Model:

```text
Random Forest Classifier
```

Target:

```text
Investment_Rating
```

Classes:

```text
Low
Moderate
Good
Excellent
```

---

## Project Architecture

```text
                  ┌────────────────────┐
                  │   Property Input   │
                  └──────────┬─────────┘
                             │
                             ▼
                  ┌────────────────────┐
                  │  Data Preprocessing │
                  └──────────┬─────────┘
                             │
             ┌───────────────┼───────────────┐
             │               │               │
             ▼               ▼               ▼
      Price Prediction  Investment Score  Rating Classifier
       XGBoost Model    XGBoost Model    Random Forest
             │               │               │
             └───────────────┼───────────────┘
                             │
                             ▼
                  ┌────────────────────┐
                  │   Flask REST API   │
                  └──────────┬─────────┘
                             │
                             ▼
                  ┌────────────────────┐
                  │   Web Application  │
                  └────────────────────┘
```

---

## Technology Stack

### Programming Language

* Python

### Data Science

* Pandas
* NumPy
* Scikit-learn

### Machine Learning

* XGBoost
* Random Forest

### Backend

* Flask
* Flask-CORS

### Frontend

* HTML
* JavaScript
* Tailwind CSS

### Model Deployment

* Joblib
* Gunicorn
* Docker
* Render

---

## Project Structure

```text
propintel-ai/
│
├── app.py
├── requirements.txt
├── Procfile
├── Dockerfile
│
├── models/
│   ├── price_model.pkl
│   ├── investment_model.pkl
│   ├── rating_model.pkl
│   └── model_features.json
│
├── templates/
│   └── index.html
│
└── README.md
```

---

## Dataset

The project uses a synthetic real estate dataset containing 500 property records.

### Dataset Features

#### Property Information

* Property ID
* City
* Neighbourhood Type
* Property Type
* Bedrooms
* Bathrooms
* Area in Square Feet
* Year Built
* Property Age

#### Property Condition

* Condition
* Furnishing Status
* Parking Spaces
* Swimming Pool
* Garden

#### Location Intelligence

* Distance to City Centre
* Distance to School
* Distance to Hospital
* Crime Rate Index
* School Rating
* Local Amenities Score

#### Market Data

* Average Monthly Rent
* Annual Property Tax
* Estimated Monthly Maintenance
* Days on Market
* Price per Square Foot
* Market Growth Rate

#### Investment Analytics

* Property Price
* Annual Rental Income
* Gross Rental Yield
* Estimated Annual Expenses
* Net Annual Rental Income
* Five-Year Investment Return
* Investment Score
* Investment Rating
* Price Trend
* Recommended Investment Strategy

---

## API Endpoints

### Health Check

```text
GET /api/health
```

Example response:

```json
{
  "status": "online",
  "message": "Real Estate AI API is running"
}
```

---

### Property Prediction

```text
POST /api/predict
```

Example request:

```json
{
  "City": "New York",
  "Neighborhood_Type": "Downtown",
  "Property_Type": "Apartment",
  "Bedrooms": 3,
  "Bathrooms": 2,
  "Area_SqFt": 1800,
  "Year_Built": 2015,
  "Property_Age": 11,
  "Condition": "Good",
  "Furnished": "Furnished",
  "Parking_Spaces": 2,
  "Has_Pool": "No",
  "Has_Garden": "Yes",
  "Distance_to_City_Center_Miles": 5,
  "Distance_to_School_Miles": 2,
  "Distance_to_Hospital_Miles": 3,
  "Crime_Rate_Index": 35,
  "School_Rating": 8,
  "Local_Amenities_Score": 80,
  "Market_Growth_Rate_Percent": 5,
  "Gross_Rental_Yield_Percent": 6,
  "Days_on_Market": 60
}
```

Example response:

```json
{
  "success": true,
  "predicted_price": 482500.0,
  "investment_score": 82.4,
  "investment_rating": "Excellent",
  "recommended_strategy": "Buy & Rent / Strong Investment"
}
```

---

## Local Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/propintel-ai.git
```

```bash
cd propintel-ai
```

---

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Activate it on macOS/Linux:

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run the Application

```bash
python app.py
```

Open:

```text
http://localhost:5000
```

---

## Docker Deployment

Build the Docker image:

```bash
docker build -t propintel-ai .
```

Run the container:

```bash
docker run -p 5000:5000 propintel-ai
```

Open:

```text
http://localhost:5000
```

---

## Deployment

The application can be deployed using:

* Render
* Docker-based cloud platforms
* Other Flask-compatible hosting platforms

### Build Command

```bash
pip install -r requirements.txt
```

### Start Command

```bash
gunicorn app:app
```

---

## Model Workflow

```text
1. Load Dataset
       ↓
2. Data Exploration
       ↓
3. Feature Selection
       ↓
4. Missing Value Handling
       ↓
5. Categorical Encoding
       ↓
6. Train Machine Learning Models
       ↓
7. Evaluate Models
       ↓
8. Save Trained Models
       ↓
9. Create Flask API
       ↓
10. Connect Web Frontend
       ↓
11. Deploy Application
```

---

## Example Prediction Workflow

A user enters property information:

```text
City: New York
Property Type: Apartment
Bedrooms: 3
Bathrooms: 2
Area: 1,800 Sq Ft
School Rating: 8.0
Market Growth: 5%
Rental Yield: 6%
```

The system generates:

```text
Estimated Property Price: $482,500
Investment Score: 82/100
Investment Rating: Excellent
Strategy: Buy & Rent / Strong Investment
```

---

## Future Improvements

* SHAP-based prediction explanations
* Interactive Plotly dashboards
* Property comparison system
* Real-time market data integration
* Interactive property maps
* User authentication
* Saved property analysis
* CSV and Excel upload
* Automated investment reports
* Advanced time-series market forecasting
* Property recommendation engine
* Real estate market trend analysis

---

## Disclaimer

This project is designed for educational and portfolio purposes. The predictions are generated using a synthetic dataset and should not be considered professional financial, investment, or real estate advice.

---

## Author

**Muhammad Hammad Hafeez**

Data Science Student | Machine Learning | Python | Data Analytics

---

## Project

**Real Estate Price Prediction & Investment Intelligence Platform**

