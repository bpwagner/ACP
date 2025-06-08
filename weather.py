import pyowm

owm = pyowm.OWM('978910f354606707ef717cdf3b483575')  # You MUST provide a valid API key

# Have a pro subscription? Then use:
# owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')

# Search for current weather in London (Great Britain)
observation = owm.weather_at_place('London,GB')
w = observation.get_weather()
print(w)                      # <Weather - reference time=2013-12-18 09:20,
                              # status=Clouds>

# Weather details
print(w.get_wind()   )               # {'speed': 4.6, 'deg': 330}
print(w.get_humidity()   )           # 87
print(w.get_temperature('celsius') ) # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}

# Search current weather observations in the surroundings of
# lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
observation_list = owm.weather_around_coords(-22.57, -43.12)

wind = w.get_wind()
print(wind['speed'])
