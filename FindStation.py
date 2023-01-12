import numpy as np

def getAirTemperatureStation(response):
    responseStations = []
    try:
        timeStamp = response["items"][0]["timestamp"]
        stations = response["items"][0]["readings"]
        for station in stations:
            if(station["station_id"] == "S100" or station["station_id"] == "S104"):
                responseStations.append(station)
        responseStations.insert(0,timeStamp)
    except Exception as e:
        print("Error parsing data")
        responseStations = "error parsing temperature stations"
    return responseStations

def getTwoHourForeCastArea(response):
    responseForeCasts = []
    try: 
        validPeroid = response['items'][0]["valid_period"]
        foreCasts = response['items'][0]["forecasts"]
        for foreCast in foreCasts:
            if(foreCast['area'] == "Sembawang" or foreCast['area'] == "Woodlands"):
                responseForeCasts.append(foreCast)
        responseForeCasts.insert(0,validPeroid)
    except Exception as e:
        print("Error parsing data")
        print(e)
    return responseForeCasts
        

