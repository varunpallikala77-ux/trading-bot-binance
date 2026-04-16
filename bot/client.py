from binance.client import Client
import os
from dotenv import load_dotenv
import time

load_dotenv()

def get_client():
    api_key = os.getenv("API_KEY")
    api_secret = os.getenv("API_SECRET")

    if not api_key or not api_secret:
        raise Exception("API keys not found. Check .env file")

    client = Client(api_key, api_secret)
    client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    # Time sync fix
    server_time = client.futures_time()
    local_time = int(time.time() * 1000)
    time_offset = server_time['serverTime'] - local_time
    client.timestamp_offset = time_offset

    return client
