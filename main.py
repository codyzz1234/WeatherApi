from datetime import datetime
from FindStation import getStationAirTemp
from CallApi import getAirTemperature
from CallApi import getRainfall
import requests


def main():
    now = datetime.now()
    dateTime = now.strftime("%Y-%m-%dT%H:%M:%S")
    print("Dt string",dateTime)
    # airTemperature = getAirTemperature(dateTime);
    rainFall = getRainfall(dateTime)
    print(rainFall)
    # dictionaryResponse = {
    #     'airTemperature':airTemperature
    # }
    # print(dictionaryResponse)

    
if __name__ == '__main__':
    main();