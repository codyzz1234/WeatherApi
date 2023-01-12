from datetime import datetime
from CallApi import getTwoHourBroadcast
from CallApi import getAirTemperature
import requests
import json


def main():
    now = datetime.now()
    dateTime = now.strftime("%Y-%m-%dT%H:%M:%S")
    print("Dt string",dateTime)
    twoHourWeatherForeCast = getTwoHourBroadcast(dateTime)
    airTemperature = getAirTemperature(dateTime)
    dictionaryResponse = {
        'Two-Hour ForeCast':twoHourWeatherForeCast,
        'Air Temperature': airTemperature
    }
    stringConvert = json.dumps(dictionaryResponse,sort_keys=True,indent=4)
    print(stringConvert)

    
if __name__ == '__main__':
    main();