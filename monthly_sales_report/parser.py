import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

df = pd.read_csv('sales_data.csv')

#print(df.head())
#print(df.describe())
#print(df.info())
df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].dt.to_period('M')
#sales_by_month = df.groupby('month').apply(lambda x: x['price']*x['quantity'].sum())
#type(sales_by_month)
df['total_sales'] = pd.to_numeric(df['quantity']) * df['price']
sales_by_month = df.groupby('month')['total_sales'].sum()
print('sales by month', sales_by_month.sort_index())
#print(sales_by_month.info())
#print(sales_by_month.head())
#type(sales_by_month)
#print(df.info())
#print(df)
best_selling_index = df['quantity'].idxmax()
print(f'The Best-Selling product is: {df.loc[best_selling_index, 'product']} with a quantity of: {df.loc[best_selling_index, 'quantity']}')
#print('most sold index: ', most_sold, 'product: ', df.loc[most_sold, 'product'], 'revenue: ', df.loc[most_sold, 'total_sales'])
highest_revenue_index = df['total_sales'].idxmax()
print(f'The Highest-Revenue product is: {df.loc[highest_revenue_index, 'product']} with a total sales of: {df.loc[highest_revenue_index, 'total_sales']}')
#print(f'the max revenue is: {df['total_sales'].max()}')
#print(f'the max revenue month is: {sales_by_month['total_sales'].max()}')
#sales_by_month.index = sales_by_month.index.astype(str)

plt.figure(figsize=(6,4))
sales_by_month.plot()
plt.title('Sales by Month')
plt.xlabel('Month')
plt.ylabel('Sales USD$')
plt.show()



