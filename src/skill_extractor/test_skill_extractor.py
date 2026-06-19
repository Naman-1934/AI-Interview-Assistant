import sys
import os
from src.resume_parser.resume_parser import parse_resume
from src.skill_extractor.skill_extractor import extract_skills


def test_extract_skills_from_resume():
    text = parse_resume("data//sample//NAMAN_SHAH.pdf")

    skills = extract_skills(text)

    assert isinstance(skills, list)
    assert len(skills) > 0

    print("Extracted Skills:", skills)