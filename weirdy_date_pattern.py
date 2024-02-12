import re

def Weirdly_formatted_date(text):
    date_pattern = r'^\d{2}-[a-zA-Z]{3}-\d{4}$'
    return re.findall(date_pattern, text)

# Test the Regular Expression
if __name__ == "__main__":
    test_text = "12-Jan-2021"
    date_pattern = Weirdly_formatted_date(test_text)
     # print found result
    print("Weirdly formatted date found:", date_pattern)
