import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    'Phase': ['Requirements', 'Analysis/Design', 'Development', 'Testing', 'Deployment'],
    'Environmental': [1, 4, 5, 0, 7],
    'Technical': [3, 0, 3, 3, 1],
    'Economic': [4, 2, 1, 5, 2],
    'Social': [6, 1, 0, 0, 0]
}

# Create DataFrame
df = pd.DataFrame(data)
pastel_palette = sns.color_palette("muted")
# Create Stacked Bar Chart
sns.set(style="whitegrid")
sns.set_theme(font='Verdana', font_scale=2)
plt.figure(figsize=(10, 6))
sns.barplot(x="Phase", y="Environmental", data=df, color=pastel_palette[2], label="Environmental")
sns.barplot(x="Phase", y="Technical", data=df, color=pastel_palette[0], bottom=df["Environmental"], label="Technical")
sns.barplot(x="Phase", y="Economic", data=df, color=pastel_palette[1], bottom=df["Technical"] + df["Environmental"], label="Economic")
p = sns.barplot(x="Phase", y="Social", data=df, color=pastel_palette[3], bottom=df["Economic"] + df["Technical"] + df["Environmental"], label="Social")

# Customize the plot
# plt.title('Distribution of SDLC Phases')
plt.xlabel('SDLC Phase')
plt.ylabel('Mentions')
plt.setp(p.get_xticklabels(), rotation=35, horizontalalignment='right')
plt.legend()

# Show the plot
plt.show()
