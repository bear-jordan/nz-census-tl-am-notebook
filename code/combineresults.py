import pandas as pd
import datetime

ID_NAME = "id"
DATE_NAME = "date"

def run():
    data = pd.read_csv("../data/dummy-data.csv")
    data[DATE_NAME] = pd.to_datetime(data[DATE_NAME], format="%Y-%m-%d", utc=False)
    
    sentiments = pd.read_csv("../result/sentiments-to-check.csv")
    changes = pd.read_csv("../result/changes-to-check.csv")
    
    results = pd.concat([sentiments, changes])
    results = results.drop_duplicates()
    results = results.reset_index(drop=True)
    
    filter = data[ID_NAME].isin(results[ID_NAME])
    userData = data[filter]
    
    filterDates = (userData[DATE_NAME] > datetime.datetime.now()-pd.to_timedelta("3day")) & (userData[DATE_NAME] <= datetime.datetime.now())
    relevantData = userData[filterDates]
    
    relevantData = relevantData.sort_values(by=ID_NAME)
    
    relevantData.to_csv("../result/to-check.csv", index=False)
    