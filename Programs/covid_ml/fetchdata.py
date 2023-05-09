import pandas as pd
from datetime import datetime
from os.path import isfile
import time

baseURL = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/"
fileName = "project/media/India.csv"

def loadData(fileName, columnName): 
    data = pd.read_csv(baseURL + fileName) \
             .drop(['Lat', 'Long'], axis=1) \
             .melt(id_vars=['Province/State', 'Country/Region'], var_name='date', value_name=columnName) \
             .astype({'date':'datetime64[ns]', columnName:'Int64'}, errors='ignore')
    data['Province/State'].fillna('<all>', inplace=True)
    data[columnName].fillna(0, inplace=True)
    return data

def refreshData():
    allData = loadData("time_series_covid19_confirmed_global.csv", "CumConfirmed") \
        .merge(loadData("time_series_covid19_deaths_global.csv", "CumDeaths")) \
        .merge(loadData("time_series_covid19_recovered_global.csv", "CumRecovered"))
    
    allData = allData[allData['Country/Region'] == 'India'].drop(['Province/State'],axis=1)
    allData['Day'] = allData.reset_index().index
    allData.to_csv(fileName,index=False, encoding='utf-8')
    return allData

refreshData()


# while True:
#     refreshData()
#     # get the current time
#     current_time = datetime.now().time()

#     # check if the current time is 1 am
#     if current_time.hour == 1 and current_time.minute == 0:
#         # fetch the data
#         # your code to fetch the data goes here
#         refreshData()
#         # wait until 1:01 am before checking again
#         time.sleep(60)
#     else:
#         # wait for 1 minute before checking again
#         time.sleep(60)
