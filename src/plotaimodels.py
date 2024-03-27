

import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Get the current working directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Relative path to the Excel file
file_path = os.path.join(script_dir, 'precise.xlsx')

# Sheet name
sheet_name = 'ml'

# Load the Excel file
df = pd.read_excel(file_path, sheet_name=sheet_name, header=1)
df.sort_values(inplace=True, by='Mentions', ascending=False)

# Keep the top 7 rows
top_rows = df[:7]

# Calculate the sum of Mentions for the remaining rows
other_mentions = df[7:]['Mentions'].sum() - 1

# Create a new DataFrame for "Other" with the calculated Mentions
other_df = pd.DataFrame({'ML Technique': ['Other'], 'Mentions': [other_mentions]})

# Concatenate the top_rows DataFrame and the other_df DataFrame
new_df = pd.concat([top_rows, other_df])

# Create a bar plot using seaborn
plt.figure(figsize=(8, 14))
sns.set(style="whitegrid")
sns.set_color_codes("muted")
sns.set_theme(font='Verdana', font_scale=1.5)

# Use the modified DataFrame for plotting
p = sns.barplot(y=new_df['Mentions'], x=new_df['ML Technique'])

plt.setp(p.get_xticklabels(), rotation=45, horizontalalignment='right')

# Show the bar plot
plt.show()