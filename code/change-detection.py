import pandas as pd
from detecta import detect_cusum
import datetime

DATA = pd.read_csv("dummy-data.csv")
TEST_ID = DATA.iloc[0, 0]
ID_NAME = "id"
SIGNAL_NAME = "rating"
DATE_NAME = "date"

DATA[DATE_NAME] = pd.to_datetime(DATA[DATE_NAME], format="%Y-%m-%d", utc=False)

def select_user(data, uid=1):
    filter = data[ID_NAME] == uid
    return data[filter]

def unique_users(data):
    return data[ID_NAME].unique()

def change_detection(user_data):
    signal = user_data[SIGNAL_NAME].to_numpy()
    change, _, _, _ = detect_cusum(signal, threshold=.8, drift=1, ending=False, show=False, ax=None)
    
    resultDf = user_data.loc[:, [ID_NAME, DATE_NAME]].iloc[change]    
    filter = resultDf[DATE_NAME].dt.date == datetime.date.today()
    
    if not resultDf[filter].empty:
        return resultDf.loc[filter]

def main(data):
    users = unique_users(data)
    todaysResults = []
    for user in users:
        todaysResults.append(change_detection(select_user(data, user)))
        
    finalIDs = pd.concat(todaysResults).loc[:, [ID_NAME]]
    finalIDs.to_csv("to_check.csv", index=False)
    
if __name__ == "__main__":
    main(DATA)