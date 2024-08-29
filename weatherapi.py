import requests

# Replace with your own API key
api_key = "d1bb067f227391f80404e48c793bbf0d"

base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Get user input for the city name
city = input("Enter the city name: ")

# Construct final URL
complete_url = f"{base_url}q={city}&appid={api_key}"

# Send request and get response
response = requests.get(complete_url)

# Convert response to JSON
data = response.json()

# Process and display the data
if data["cod"] != "404":
    main = data["main"]
    weather_description = data["weather"][0]["description"]
    print(f"Temperature: {main['temp']} K")
    print(f"Weather description: {weather_description}")
else:
    print("City not found.")