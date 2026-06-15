import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.insert(0, project_root)

from src.skill_extractor.skill_extractor import extract_skills


sample_resume = """

Experienced Data Scientist

Skills

Python
SQL
Tensorflow
Machine Learning
Power BI

"""

Skills = extract_skills(sample_resume)

print(Skills)