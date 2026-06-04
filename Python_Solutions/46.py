import requests

class WeatherAPI:
    def __init__(self, city):
        self.city = city
        self.url = f"https://wttr.in/{city}?format=j1"

    def get_weather(self):
        try:
            response = requests.get(self.url, timeout=5)

            if response.status_code == 404:
                print("Error: City not found.")
                return

            response.raise_for_status()

            data = response.json()

            temperature = data["current_condition"][0]["temp_C"]
            condition = data["current_condition"][0]["weatherDesc"][0]["value"]

            print("----- Weather Report -----")
            print(f"City        : {self.city}")
            print(f"Temperature : {temperature}°C")
            print(f"Condition   : {condition}")

        except requests.exceptions.ConnectionError:
            print("Error: Network connection problem.")

        except requests.exceptions.Timeout:
            print("Error: Request timed out.")

        except requests.exceptions.RequestException as e:
            print("Error:", e)

        except KeyError:
            print("Error: Invalid weather data received.")


city_name = input("Enter city name: ")

weather = WeatherAPI(city_name)
weather.get_weather()