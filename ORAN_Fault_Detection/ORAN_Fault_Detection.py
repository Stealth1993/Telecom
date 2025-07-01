from sklearn.ensamble import IsolationForest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sample Data
data = pd.DataFramame({
    'feature1': np.random.normal(0, 1, 100),
    'feature2': np.random.normal(0, 1, 100)
})

# Introduce some anomalies
data.loc[5, 'feature1'] = 10
data.loc[15, 'feature2'] = -10

# Isolation Forest Model
model = IsolationForest(contamination=0.1, random_state=42)
# Fit the model
model.fit(data)
# Predict anomalies
predictions = model.predict(data)
# Convert predictions to a more interpretable format
data['anomaly'] = predictions
data['anomaly'] = data['anomaly'].map({1: 0, -1: 1})  # 0 for normal, 1 for anomaly
# Visualize the results
plt.figure(figsize=(10, 6))
plt.scatter(data['feature1'], data['feature2'], c=data['anomaly'], cmap='coolwarm', marker='o')
plt.title('Anomaly Detection using Isolation Forest')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.colorbar(label='Anomaly')
plt.show()