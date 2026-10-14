def format_weather(data):
    current = data.get("current", {})
    temperature = current.get("temperature_2m")
    wind = current.get("wind_speed_10m")
    if temperature is None or wind is None:
        return "Weather data incomplete"
    return f"Temperature: {temperature} C; wind: {wind} km/h"


def main():
    sample = {"current": {"temperature_2m": 21.5,
                          "wind_speed_10m": 8.0}}
    print(format_weather(sample))


if __name__ == "__main__":
    main()
