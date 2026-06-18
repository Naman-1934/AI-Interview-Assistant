import os
import pandas as pd

_HERE = os.path.dirname(os.path.abspath(__file__))
_SKILLS_CSV = os.path.join(_HERE, "..", "..", "data", "master", "skills_master.csv")

skills_df = pd.read_csv(_SKILLS_CSV)

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