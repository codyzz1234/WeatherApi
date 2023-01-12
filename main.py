from datetime import datetime
from CallApi import getTwoHourBroadcast
from CallApi import getAirTemperature
import requests
import json

apiToken = '';
chatID = '';
apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

def sendToTelegram(message):
    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        print(response.text)   
    except Exception as e:
        print(e)
    
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
    sendToTelegram(stringConvert)


    
if __name__ == '__main__':
    main();