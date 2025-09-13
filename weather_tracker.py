import requests

api_key = 'fa3083078c3cd1712c78a7aa434c84ad'

while True:
    user_input = input("Enter city name: ")

    weather_data = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={user_input}&appid={api_key}&units=metric').json()

    if weather_data['cod'] == '404':
        print("City not found, please check the city name and try again.")
    else:
        wd = weather_data
        city = wd['name']
        weather = wd['weather'][0]['main']
        description = wd['weather'][0]['description']
        temperature = wd['main']['temp']
        print(f"Current weather in {city}: {weather}")
        print(f"Weather description: {description}")
        print(f"Temperature: {temperature}°C")

    next_weather_input = input("Do you want to check the weather at another city? (yes/no): ")
    if next_weather_input.lower() != 'yes':
        print("Thank you for using the weather fetcher. Goodbye!")
        break