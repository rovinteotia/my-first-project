import numpy as np
from sklearn.linear_model import LinearRegression

# Simulated historical cost trend
current_cost = np.array([[1000], [2000], [3000], [4000], [5000]])
next_month_cost = np.array([1080, 2150, 3150, 4300, 5500])

model = LinearRegression()
model.fit(current_cost, next_month_cost)

def predict_cost(new_cost):
    prediction = model.predict([[new_cost]])
    return float(prediction[0])
