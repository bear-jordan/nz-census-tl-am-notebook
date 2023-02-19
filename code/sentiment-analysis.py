import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import datetime

ID_NAME = "id"
SIGNAL_NAME = "rating"
TEXT_NAME = "sentiment"
DATE_NAME = "date"
SCORE_THRESHOLD = 0.5

def get_yesterday():
    return datetime.date.today()-datetime.timedelta(days = 1)

def select_user(todaysData, uid=1):
    filter = todaysData[ID_NAME] == uid
    return todaysData[filter]

def unique_users(data):
    return data[ID_NAME].unique()

def load_text(userData):
    return userData[TEXT_NAME]
    
def get_sentiment(text):
    sentiment = SentimentIntensityAnalyzer()
    return sentiment.polarity_scores(text)
    
def main(data):
    filterToday = data[DATE_NAME].dt.date == get_yesterday()
    todaysData = data[filterToday]
    users = unique_users(todaysData)
    results = []
    for user in users:
        userData = select_user(todaysData, user)
        text = load_text(userData)
        score = get_sentiment(text)["neg"]
        if score > SCORE_THRESHOLD:
            results.append([user])
        
    pd.DataFrame(results, columns=[ID_NAME]).to_csv("sentiments-to-check.csv", index=False)
        
if __name__ == "__main__":
    DATA = pd.read_csv("dummy-data.csv")
    DATA[DATE_NAME] = pd.to_datetime(DATA[DATE_NAME], format="%Y-%m-%d", utc=False)
    
    main(DATA)