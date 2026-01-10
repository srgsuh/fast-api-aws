from fastapi import FastAPI
from services.weather import get_weather
from services.exchange_rates import get_exchange_rate

app = FastAPI()

@app.get("/health")
async def health_check() -> dict:
    """
    Health check endpoint to verify the service is running.
    """
    return {"status": "healthy"}


@app.get("/info")
async def info_process(message: str, value: int = 0) -> dict:
    """
    Process the input message and value, returning a formatted response.
    """
    processed_message = f"Processed message: {message.upper()}"
    processed_value = value * 2
    return {
        "original_message": message,
        "processed_message": processed_message,
        "original_value": value,
        "processed_value": processed_value,
    }

@app.get("/weather")
async def weather_process(city: str) -> dict:
    """
    Retrieve weather information for the specified city.
    """
    weather_info = get_weather(city)
    return {
        "status": "OK",
        "city": city,
        "weather": weather_info
    }

@app.get("/currency")
async def process_currency(currency_from: str, currency_to: str, full_names: bool = False) -> dict:
    """
    Get the exchange rate between two currencies.
    """
    exchange_info = get_exchange_rate(currency_from, currency_to, full_names)
    return {
        "status": "OK",
        "exchange_info": exchange_info
    }

@app.post("/mirror")
async def process_mirror(body: dict) -> dict:
    """
    Mirror the input JSON body back to the caller.
    """
    return {
        "status": "OK",
        "mirrored_body": body
    }
