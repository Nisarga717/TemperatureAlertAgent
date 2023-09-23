import requests
import twilio
from twilio.rest import Client
from uagents import Agent, Context



tapman = Agent(
    name="tapman",
    port=8000,
    seed="tapman secret phrase",
    endpoint=["http://127.0.0.1:8000/submit"],
)


#User Inputs the City
city = input('Enter the City : ')
api_id = '7e7336cb9462675b55fe1a9f51541907'

url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + api_id

# Taking the minimum and maximum Temperature from the user
min_temp = int(input('Enter the Minimum Temperature : '))
max_temp = int(input('Enter the Maximum Temperature : '))


try:
    # Sending request to fetch data from API
    response = requests.get(url)

    # Checking if the request is successful or not
    if response.status_code == 200:
        # storing data in json format
        data = response.json()

        # Extracting the Temperature from the Data
        Current_Temp = data['main']['temp']
        Temp_celicus = Current_Temp - 273.15  # Converting Kelvin to Celsius

    else:
        print(f"Request failed with status code {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Request error: {e}")

def check_Temperature():
    if Temp_celicus < min_temp:
        return (f"Temperature in {city} is below ({min_temp}°C).")
    elif Temp_celicus > max_temp:
        return (f"Temperature in {city} is above ({max_temp}°C).")
    else:
        return (f"Temperature in {city} is within ({min_temp}-{max_temp}°C).")
    
TWILIO_ACCOUNT_SID = "AC91933021855e8d8cf8b34935f2c0b02c"
TWILIO_AUTH_TOKEN = "0bcf8bb1c937390ccde7aaa880691d4c"
TWILIO_PHONE_NUMBER = "+12564484718"
TO_PHONE_NUMBER = "+919724879676"  # Replace with the recipient's phone number



def alert_message(message):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    client.messages.create(
        to=TO_PHONE_NUMBER,
        from_=TWILIO_PHONE_NUMBER,
        body=message
    )
        

@tapman.on_interval(period=900.0) #checking every 15 minutes
async def Temperature_alert(ctx:Context):
    temperature = check_Temperature()
    ctx.logger.info(temperature)
    if "below" in temperature or "above" in temperature :
        await alert_message(temperature)

if __name__ == "__main__":
    tapman.run()






        


    

    