import pandas as pd

df = pd.read_csv("data//processed//resume_with_skills.csv")

print(sorted(df['Category'].unique()))