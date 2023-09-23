
# Temperature Alert Agent




## Overview

This is a Temperature Alert Agent, a Python script that monitors temperature conditions and triggers alerts when specific thresholds are met or exceeded. It can be used in various applications like server room temperature monitoring, greenhouse control, or any scenario where temperature regulation is critical.
## Features

Monitors temperature from one or more sensors.

Sends alerts via email/SMS when the temperature crosses predefined thresholds.

Supports configuration of alert thresholds and notification settings.

Logs temperature readings for historical analysis.


## Installation

On your computer, you may need to install:

Python 3.8, 3.9 or 3.10.

PIP (Python Installs Packages).

Poetry for virtual environments (optional).

uAgents framework 

Twilio for Sending Notifications

for more info visit:
(https://fetch.ai/docs/guides/agents/installing-uagent)
## API Reference

we have used a free to use API in order to fetch the weather details for any given Location.

API site:
(https://openweathermap.org/api)

Here's a basic outline of how to use the OpenWeatherMap API within your Python script:

1. *Sign Up for an API Key*:

   You'll need to sign up for a free API key on the OpenWeatherMap website. Once you have your API key, you can use it to access weather data.

2. *Install the Requests Library*:

   You'll need the `requests` library to make HTTP requests to the OpenWeatherMap API. You can install it using `pip`:

   bash
   pip install requests

3. *Make API Requests*:

   Use the `requests` library to make GET requests to the OpenWeatherMap API and retrieve weather data. You can specify the location (latitude and longitude) or city name to get weather information for a specific location.

   Here's a basic example of how to retrieve the current weather for a city:

    import requests

api_key = 'YOUR_API_KEY'
city_name = 'CityName'
base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'

response = requests.get(base_url)

if response.status_code == 200:
    data = response.json()





## Notification

This Temperature Alert Agent utilizes the Twilio API to send SMS notifications when exchange rates cross the specified thresholds. Follow these steps to configure and use Twilio for sending notifications:

1. *Twilio Account Setup:*

   - If you don't already have one, sign up for a Twilio account at [Twilio](https://www.twilio.com/).
   - Once registered, you'll need to obtain the following credentials:
     - Twilio Account SID
     - Twilio Auth Token
     - Twilio Phone Number (a phone number you've purchased or received from Twilio)
     - Recipient Phone Number (the phone number where you want to receive notifications)

2. *Configuration in the Script:*

   Open the Python script (`Temperature.py`) and replace the following placeholders with your Twilio credentials:

   
    Twilio credentials (replace with your actual    Twilio credentials)
   TWILIO_ACCOUNT_SID = 'YOUR_TWILIO_ACCOUNT_SID'
   TWILIO_AUTH_TOKEN = 'YOUR_TWILIO_AUTH_TOKEN'
   TWILIO_PHONE_NUMBER = 'YOUR_TWILIO_PHONE_NUMBER'
   TO_PHONE_NUMBER = 'RECIPIENT_PHONE_NUMBER'

3. *Sending SMS Alerts:*

   The script includes a function called `alert_message` that uses the Twilio API to send SMS messages. Here's how it works:

   python
   def send_sms_alert(message):
       client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
       client.messages.create(
           to=TO_PHONE_NUMBER,
           from_=TWILIO_PHONE_NUMBER,
           body=message
       )





## Source Code

The Source Code for this Program : 
(https://github.com/Nisarga717/TemperatureAlertAgent.git)