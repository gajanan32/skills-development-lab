import pandas as pd

# Step 1: Load the first Excel file into a pandas DataFrame, specifying the 'openpyxl' engine
file1 = 'file1.xlsx'  # Path to the first Excel file
df1 = pd.read_excel(file1, engine='openpyxl')

# Step 2: Load the second Excel file into a pandas DataFrame, specifying the 'openpyxl' engine
file2 = 'file2.xlsx'  # Path to the second Excel file
df2 = pd.read_excel(file2, engine='openpyxl')

# Step 3: Merge the two DataFrames based on the common column 'Rollno'
merged_df = pd.merge(df1, df2, on='Rollno')

# Step 4: Save the merged data to a new Excel file
output_file = 'merged_output.xlsx'  # The name of the output file
merged_df.to_excel(output_file, index=False)

print(f"Files merged successfully! Output saved as {output_file}")
