from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

weather_data = {
    "Mumbai": {
        "temperature": "30°C",
        "condition": "Partly Cloudy",
        "humidity": "75%"
    },
    "Delhi": {
        "temperature": "34°C",
        "condition": "Sunny",
        "humidity": "45%"
    },
    "Pune": {
        "temperature": "28°C",
        "condition": "Cloudy",
        "humidity": "65%"
    }
}


@app.route("/")
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Weather Information Dashboard</title>
    </head>
    <body>
        <h1>Weather Information Dashboard</h1>
        <p>Simple weather information for selected cities.</p>

        <h2>Available Cities</h2>

        <ul>
            <li><a href="/weather/Mumbai">Mumbai</a></li>
            <li><a href="/weather/Delhi">Delhi</a></li>
            <li><a href="/weather/Pune">Pune</a></li>
        </ul>

        <p><a href="/health">Check Application Health</a></p>
    </body>
    </html>
    """)


@app.route("/weather/<city>")
def weather(city):
    city_name = city.title()

    if city_name not in weather_data:
        return "City not found", 404

    data = weather_data[city_name]

    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Weather - {{ city }}</title>
    </head>
    <body>
        <h1>Weather Information</h1>

        <h2>{{ city }}</h2>

        <p>Temperature: {{ temperature }}</p>
        <p>Condition: {{ condition }}</p>
        <p>Humidity: {{ humidity }}</p>

        <p><a href="/">Back to Dashboard</a></p>
    </body>
    </html>
    """,
    city=city_name,
    temperature=data["temperature"],
    condition=data["condition"],
    humidity=data["humidity"])


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)