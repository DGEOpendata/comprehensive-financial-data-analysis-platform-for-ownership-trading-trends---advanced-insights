python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_excel('Ownership_Trading_Summary_FEB.xlsx')

# Filter data based on trader category
def filter_data_by_category(data, category):
    return data[data['Trader Category'] == category]

# Calculate net buy-sell value
def calculate_net_values(data):
    data['Net Value'] = data['Buy Value (AED)'] - data['Sell Value (AED)']
    return data

# Visualize data
def visualize_trading_trends(data, category):
    filtered_data = filter_data_by_category(data, category)
    filtered_data = calculate_net_values(filtered_data)

    plt.figure(figsize=(10, 6))
    sns.lineplot(data=filtered_data, x='Date', y='Net Value', label=f'Net Value ({category})')
    plt.title(f'Trading Trends for {category} Category')
    plt.xlabel('Date')
    plt.ylabel('Net Value (AED)')
    plt.legend()
    plt.show()

# Example usage
category = 'Foreign'
visualize_trading_trends(data, category)
