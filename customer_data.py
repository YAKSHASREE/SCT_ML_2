import pandas as pd
data = {
    'customer_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'total_amount': [1500, 2800, 2000, 3200, 1200, 2900, 1600, 2100, 1800, 2400],
    'purchase_count': [20, 40, 25, 50, 15, 38, 22, 30, 28, 35],
    'avg_value': [75, 70, 80, 64, 80, 76, 73, 70, 64, 69]
}
df = pd.DataFrame(data)
df.to_csv('customer_data.csv', index=False)
print("CSV file 'customer_data.csv' created successfully!")