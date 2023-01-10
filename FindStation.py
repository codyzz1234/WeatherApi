def getStationAirTemp(response):
    try:   
        timestamp = response['items'][0]["timestamp"]
        stations = response['items'][0]["readings"]
        stationValue = ""
        for station in stations:
            if(station["station_id"] == "S107"):
                stationValue = station["value"]
                break;
        response = {
        'StationId': "S107",
        'StationTemperature':stationValue
        }

    except Exception:
        print("Error parsing data")
        response = "error"
        
    return response;
    