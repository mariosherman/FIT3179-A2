import pandas as pd

# Load the original CSV content from the user's data
file_path = 'FIT3179-A2\data\global-education.csv'
df = pd.read_csv(file_path)

# Create separate rows for male and female data
males = df.copy()
females = df.copy()

# Modify male rows
males['Gender'] = 'Male'
males = males.rename(columns={
    "OOSR_Pre0Primary_Age_Male": "OOSR_Pre0Primary_Age",
    "OOSR_Primary_Age_Male": "OOSR_Primary_Age",
    "OOSR_Lower_Secondary_Age_Male": "OOSR_Lower_Secondary_Age",
    "OOSR_Upper_Secondary_Age_Male": "OOSR_Upper_Secondary_Age",
    "Completion_Rate_Primary_Male": "Completion_Rate_Primary",
    "Completion_Rate_Lower_Secondary_Male": "Completion_Rate_Lower_Secondary",
    "Completion_Rate_Upper_Secondary_Male": "Completion_Rate_Upper_Secondary",
    "Youth_15_24_Literacy_Rate_Male": "Youth_15_24_Literacy_Rate"
})

# Modify female rows
females['Gender'] = 'Female'
females = females.rename(columns={
    "OOSR_Pre0Primary_Age_Female": "OOSR_Pre0Primary_Age",
    "OOSR_Primary_Age_Female": "OOSR_Primary_Age",
    "OOSR_Lower_Secondary_Age_Female": "OOSR_Lower_Secondary_Age",
    "OOSR_Upper_Secondary_Age_Female": "OOSR_Upper_Secondary_Age",
    "Completion_Rate_Primary_Female": "Completion_Rate_Primary",
    "Completion_Rate_Lower_Secondary_Female": "Completion_Rate_Lower_Secondary",
    "Completion_Rate_Upper_Secondary_Female": "Completion_Rate_Upper_Secondary",
    "Youth_15_24_Literacy_Rate_Female": "Youth_15_24_Literacy_Rate"
})

# Remove old columns from both datasets
columns_to_remove = [
    "OOSR_Pre0Primary_Age_Female", "OOSR_Primary_Age_Female", "OOSR_Lower_Secondary_Age_Female", 
    "OOSR_Upper_Secondary_Age_Female", "Completion_Rate_Primary_Female", 
    "Completion_Rate_Lower_Secondary_Female", "Completion_Rate_Upper_Secondary_Female", 
    "Youth_15_24_Literacy_Rate_Female", "OOSR_Pre0Primary_Age_Male", 
    "OOSR_Primary_Age_Male", "OOSR_Lower_Secondary_Age_Male", "OOSR_Upper_Secondary_Age_Male", 
    "Completion_Rate_Primary_Male", "Completion_Rate_Lower_Secondary_Male", 
    "Completion_Rate_Upper_Secondary_Male", "Youth_15_24_Literacy_Rate_Male"
]

males = males.drop(columns=columns_to_remove)
females = females.drop(columns=columns_to_remove)

# Concatenate the two datasets
final_df = pd.concat([males, females], ignore_index=True)

# Save the modified CSV
output_file_path = 'data/modified_countries_and_areas.csv'
final_df.to_csv(output_file_path, index=False)

# Display the dataframe to the user
import ace_tools as tools; tools.display_dataframe_to_user(name="Modified Education Dataset", dataframe=final_df)
