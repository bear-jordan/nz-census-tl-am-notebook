import random
import datetime
import pandas as pd

NUM_DAYS = 30
NUM_USERS = 3

def gen_user(n=NUM_USERS):
    return random.randint(100000, 999999)
    
def gen_sentiment():
    rand_score = random.randint(0, 1)
    
    if rand_score == 1:
        return "happy"
    else:
        return "sad"
    
def gen_rating():
    return random.randint(0, 5)
    
def gen_date(day=1):
    return datetime.datetime(2023, 1, day)

def gen_entry(user=1, date=1):
    return [user, date, gen_sentiment(), gen_rating()]
    
def gen_entries():
    users = [gen_user() for i in range(NUM_DAYS)]
    dates = [gen_date(i) for i in range(1,NUM_DAYS+1)]
    
    entries = []
    
    for user in users:
        for date in dates:
            entries.append(gen_entry(user, date))
            
    data = pd.DataFrame(entries, columns=["id", "date", "sentiment", "rating"])
    data.to_csv("dummy-data.csv", index=False)

if __name__ == "__main__":
    gen_entries()
