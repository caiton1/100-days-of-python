import requests
from twilio.rest import Client
import os

# storing endpoint and authentication in variables
owm_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ("OWM_KEY")
twilio_account = "ACe1f7a1ffda429261f74fdb0c538c016e"
twilio_token = os.environ("OWM_TOKEN")

# dictionary that will be passed in the request parameters
weather_params = {
    "lat": 33.661481,
    "lon": 112.011890,
    "exclude": "current,minute,daily",
    "appid": api_key
}

# get api response
response = requests.get(owm_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

# prime check variable
will_rain = False

# loop through response data to check for rain ID
for hour_data in weather_slice:
    if int(hour_data["weather"][0]["id"]) <= 700:
        will_rain = True

# check if rain ID exists
if will_rain:
    client = Client(twilio_account, twilio_token)
    message=client.messages.create(
        body="its gonna rain",
        from_="+18339092852",
        to="+14805594255"
    )

# debug
print(message.status)