import re

# Sample string containing jokes
string = "Why you like jokes? Because it's fun"

 Regular expression pattern for extracting jokes
pattern = r"Why you like (.*?)\? Because(.*?)"

# Extract jokes using regex
match = re.search(pattern, string)

# Print the match
if match:
    print("Joke Setup:", match.group(10))
    print("Joke Punchline:", match.group(2))
