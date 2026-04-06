import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

np.random.seed(0)

brands = ['Toyota','Honda','BMW','Audi','Ford','Hyundai']
fuel_types = ['Petrol','Diesel','Electric']

data = {
    'Brand': np.random.choice(brands, 200),
    'Mileage': np.random.randint(10, 30, 200),
    'Fuel_Type': np.random.choice(fuel_types, 200)
}

df = pd.DataFrame(data)

price_map = {'Toyota':20000,'Honda':22000,'BMW':50000,'Audi':48000,'Ford':25000,'Hyundai':18000}
fuel_map = {'Petrol':1.0,'Diesel':1.1,'Electric':1.3}

df['Price'] = df['Brand'].map(price_map) * df['Fuel_Type'].map(fuel_map) - df['Mileage']*300 + np.random.randint(-2000,2000,200)

plt.figure()
sns.scatterplot(x='Mileage', y='Price', data=df)
plt.title('Price vs Mileage')
plt.show()

plt.figure()
brand_avg = df.groupby('Brand')['Price'].mean().sort_values(ascending=False)
sns.barplot(x=brand_avg.index, y=brand_avg.values)
plt.xticks(rotation=45)
plt.title('Brand-wise Price Comparison')
plt.show()

plt.figure()
fuel_avg = df.groupby('Fuel_Type')['Price'].mean()
sns.barplot(x=fuel_avg.index, y=fuel_avg.values)
plt.title('Fuel Type Price Trends')
plt.show()