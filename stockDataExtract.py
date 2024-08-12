import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Create a Ticker object for Apple stock
apple = yf.Ticker("AAPL")

# Fetch and display Apple stock info
apple_info = apple.info

# Extract and format stock info
country = apple_info.get('country', 'N/A')
sector = apple_info.get('sector', 'N/A')

print(f"Apple Stock Information:")
print(f"{'Country:':<20} {country}")
print(f"{'Sector:':<20} {sector}")
print()

# Extract Apple share price data
apple_share_price_data = apple.history(period="max")

# Reset index for better manipulation
apple_share_price_data.reset_index(inplace=True)

# Display the first few rows of share price data
print("Apple Share Price Data (Sample):")
print(apple_share_price_data.head())
print()

# Plot the Open price against the Date
plt.figure(figsize=(10, 6))
plt.plot(apple_share_price_data['Date'], apple_share_price_data['Open'], label='Open Price')
plt.xlabel('Date')
plt.ylabel('Open Price (USD)')
plt.title('Apple Stock Open Price Over Time')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Extract and format dividends data
dividends = apple.dividends
print("Apple Dividends Data:")
print(dividends)

# Plot dividends data
plt.figure(figsize=(10, 6))
plt.plot(dividends.index, dividends, marker='o', linestyle='-', color='b', label='Dividends')
plt.xlabel('Date')
plt.ylabel('Dividends (USD)')
plt.title('Apple Stock Dividends Over Time')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
