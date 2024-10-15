import pandas as pd

# Load male and female datasets
male_df = pd.read_csv('FIT3179-A2/data/male-out-of-school.csv')
female_df = pd.read_csv('FIT3179-A2/data/female-out-of-school.csv')

# Melt the dataframes to long format to have years in one column
male_long = male_df.melt(id_vars=["Country Name", "Country Code", "Indicator Name", "Indicator Code"], 
                         var_name="Year", value_name="Male")
female_long = female_df.melt(id_vars=["Country Name", "Country Code", "Indicator Name", "Indicator Code"], 
                             var_name="Year", value_name="Female")

# Merge the two datasets on Country Name, Country Code, and Year
combined_df = pd.merge(male_long, female_long, 
                       on=["Country Name", "Country Code", "Year"], 
                       how='outer')

# Reshape data to have 'Gender' and 'Value' columns
combined_long = pd.melt(combined_df, 
                        id_vars=["Country Name", "Country Code", "Year"], 
                        value_vars=["Male", "Female"], 
                        var_name="Gender", value_name="Value")

# Save the combined data to a new CSV
combined_long.to_csv('combined_out_of_school.csv', index=False)
