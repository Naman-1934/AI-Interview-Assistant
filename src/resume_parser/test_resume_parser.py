from src.resume_parser.resume_parser import parse_resume

# We check it returns a string
# We check the string has meaningful content — more than 100 characters means it actually extracted something and didn't return empty
# We print the first 500 characters so you can visually verify it looks like resume text

def test_parse_resume():
    text = parse_resume("data//sample//NAMAN_SHAH.pdf")

    assert isinstance(text, str)
    assert len(text) > 100

    print(text[:500])