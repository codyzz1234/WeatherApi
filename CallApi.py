import requests
from FindStation import getAirTemperatureStation
from FindStation import getTwoHourForeCastArea

def getAirTemperature(dateTime):
    check = True;
    params = {'date_time':dateTime}
    url = "https://api.data.gov.sg/v1/environment/air-temperature"
    try:
        data = requests.get(url=url,params=params)
    except Exception:
        check = False;
        data = "error getting request"
        
    if(check == False):
        response = "Error calling Air Temperature API"
    else:
        response = data.json()
        response = getAirTemperatureStation(response)
    return response 
    

def getTwoHourBroadcast(dateTime):
    check = True;
    params = {'date_time':dateTime}
    url = "https://api.data.gov.sg/v1/environment/2-hour-weather-forecast"
    try:
        data = requests.get(url=url,params=params)
    except Exception:
        check = False;
        data = "error getting request"
        
    if(check == False):
        response = "Error calling Two Hour Broadcast API"
    else:
        response = data.json()
        response = getTwoHourForeCastArea(response)
    return response 
    