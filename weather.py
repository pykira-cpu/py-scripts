import requests

while True:
    ''' I generated my own API key by signing in openweather website.
     Get your own API id and replace it with 'appid' value.
     Also, the last 3 characters in the api address should remain same which is '&q='. 
     q is the parameter for the city name in URL
     '''

    API_address = 'http://api.openweathermap.org/data/2.5/weather?appid=deb9681aedaab7e97e4bba271f6a9b7e&q='
    city = input("City: ")
    url = API_address + city.strip()

    json_data = requests.get(url).json()

    weather_description = json_data['weather'][0]['description']
    current_temperature = json_data['main']['temp']
    current_pressure = json_data['main']["pressure"]
    current_humidity = json_data['main']['humidity']

    print(" Temperature (in celsius unit): " +
          str(current_temperature-273)+" c" +
          "\n atmospheric pressure (in hPa unit): " +
          str(current_pressure) +
          "\n humidity (in percentage): " +
          str(current_humidity) +
          "\n description:  " +
          str(weather_description))

    choice = input("Choose 'y' to continue ")

    if choice != 'y':
        break
