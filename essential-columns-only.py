import pandas as pd

# Import CSV file into a DataFrame
df = pd.read_csv('filtered.csv')

# Select columns to export
columns_to_export = ['first_name', 'last_name', 'linkedin', 'position', 'websites', 'company_name']
df_export = df[columns_to_export]

# Export selected columns to new CSV file
df_export.to_csv('dev shops-10to500heads-nobizdev.csv', index=False)
