from src.resume_parser.resume_parser import parse_resume
from src.skill_extractor.skill_extractor import extract_skills
from src.profile_builder.profile_builders import detect_role

def test_detect_role_from_resume():
    text = parse_resume("data//sample//NAMAN_SHAH.pdf")

    skills = extract_skills(text)

    profile = detect_role(skills)

    assert "role" in profile
    assert "confidence" in profile
    assert profile["confidence"] > 0

    print("Detected Role:", profile["role"])
    print("Confidence:", profile["confidence"])
    print("All Scores:", profile["scores"])

