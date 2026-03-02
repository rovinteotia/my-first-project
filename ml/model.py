import numpy as np
from sklearn.linear_model import LinearRegression

# Sample historical cloud usage data
usage = np.array([[100], [200], [300], [400], [500]])
cost = np.array([1000, 2000, 3000, 4000, 5000])

# Train model
model = LinearRegression()
model.fit(usage, cost)

def predict_cost(new_usage):
    prediction = model.predict([[new_usage]])
    return float(prediction[0])
