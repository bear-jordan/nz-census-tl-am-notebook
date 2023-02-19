import pandas as pd
from detecta import detect_cusum
import datetime

ID_NAME = "id"
SIGNAL_NAMES = ["rating"]
DATE_NAME = "date"

def select_user(data, uid=1):
    filter = data[ID_NAME] == uid
    return data[filter]

def get_yesterday():
    return datetime.date.today()-datetime.timedelta(days = 1)

def unique_users(data):
    return data[ID_NAME].unique()

def change_detection(user_data, signalName):
    signal = user_data[signalName].to_numpy()
    change, _, _, _ = detect_cusum(signal, threshold=.8, drift=1, ending=False, show=False, ax=None)
    
    resultDf = user_data.loc[:, [ID_NAME, DATE_NAME]].iloc[change]    
    filter = resultDf[DATE_NAME].dt.date == get_yesterday()
    
    if not resultDf[filter].empty:
        return resultDf.loc[filter]

def run():
    data = pd.read_csv("../data/dummy-data.csv")
    data[DATE_NAME] = pd.to_datetime(data[DATE_NAME], format="%Y-%m-%d", utc=False)
    
    users = unique_users(data)
    todaysResults = []
    for user in users:
        for signal in SIGNAL_NAMES:
            todaysResults.append(change_detection(select_user(data, user), signal))
        
    finalIDs = pd.concat(todaysResults).loc[:, [ID_NAME]]
    finalIDs.to_csv("../result/changes-to-check.csv", index=False)
