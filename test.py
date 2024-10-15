import pandas as pd

# Load the CSV data into a DataFrame
df = pd.read_csv('FIT3179-A2\data\literacy-rate-of-young-men-and-women.csv')

# Drop rows where either Youth Male or Female Literacy Rate is null
df_filtered = df.dropna(subset=['Youth Male Literacy Rate', 'Youth Female Literacy Rate'])

# Sort by Entity (country) and Year in descending order
df_filtered = df_filtered.sort_values(by=['Entity', 'Year'], ascending=[True, False])

# Keep only the last year of data for each country
df_last_year = df_filtered.drop_duplicates(subset=['Entity'], keep='first')

# Display the filtered data
print(df_last_year)

# Save the filtered data to a new CSV file if needed
df_last_year.to_csv('filtered_literacy_data.csv', index=False)
