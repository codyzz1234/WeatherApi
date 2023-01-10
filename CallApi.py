import requests
from FindStation import getStationAirTemp
def getAirTemperature(dateTime):
    params = {'date_time':dateTime}
    url = 'https://api.data.gov.sg/v1/environment/air-temperature'
    try:
        data = requests.get(url=url,params=params)
    except Exception:
        check = False
    
    if(check == False):
        response = "Error calling api"
    else:
        response = data.json();
        response = getStationAirTemp(response)
        
    return response

def getRainfall(dateTime):
    check = True;
    params = {'date_time':dateTime}
    url = "https://api.data.gov.sg/v1/environment/rainfall"
    try:
        data = requests.get(url=url,params=params)
    except Exception:
        check = False;
        data = "error getting request"
        
    if(check == False):
        response = "Error calling api"
    else:
        response = data.json()
    return response 