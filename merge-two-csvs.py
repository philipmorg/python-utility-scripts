import pandas as pd

# read in the two CSV files
df1 = pd.read_csv("bizdev-1-a-page1thru96.csv")
df2 = pd.read_csv("bizdev-global-1-a-csv.csv")

merged_df = pd.concat([df1, df2], ignore_index=True)

print(merged_df[['first_name', 'last_name', 'position', 'company_name']].head())


# remove duplicate rows
merged_df.drop_duplicates(subset=['first_name', 'last_name', 'position'], keep='first', inplace=True)

print(merged_df[['first_name', 'last_name', 'position', 'company_name']].head())


# write the resulting DataFrame to a new CSV file
merged_df.to_csv("bizdev.csv", index=False)