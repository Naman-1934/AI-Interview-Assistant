import pandas as pd

skills_df = pd.read_csv("data//master//skills_master.csv")

skills_list = (

    # .tolist() converts a collection of data into a standard List data type.
    skills_df["Skill"].str.lower().tolist()
)

def extract_skills(text):
    text = str(text).lower()

    found_skills = set()

    for skill in skills_list:
        if skill in text:
            found_skills.add(skill)

    return sorted(
        list(found_skills)
    )