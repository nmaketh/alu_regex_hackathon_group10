import re

TWITTER_USERNAME_PATTERN = r'@([a-zA-Z0-9_]+)'

def extract_twitter_usernames(text):
    return re.findall(TWITTER_USERNAME_PATTERN, text)

if __name__ == "__main__":
    test_text = "Hello , my name is Ucunguyabe ! follow to get best of stories on x @ucunguyabe  @user12 and follow @realman_user!"
    twitter_usernames = extract_twitter_usernames(test_text)
     # print found result
    print("Twitter Usernames found:", twitter_username
