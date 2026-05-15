import requests
from typing import Dict, Any

class FinancialDataModule:
    def __init__(self):
        """
        Fetches real-time financial and cryptocurrency data from the CoinGecko API.
        """
        self.base_url = "https://api.coingecko.com/api/v3"

    def fetch_market_data(self, crypto_id: str, vs_currency: str = "usd") -> Dict[str, Any]:
        """
        Retrieves market data (current price, market cap) for a given identifier.
        """
        endpoint = f"{self.base_url}/simple/price"
        params = {
            "ids": crypto_id.lower(),
            "vs_currencies": vs_currency.lower(),
            "include_market_cap": "true",
            "include_24hr_change": "true"
        }

        try:
            response = requests.get(endpoint, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()

            if crypto_id.lower() in data:
                result = data[crypto_id.lower()]
                return {
                    "success": True,
                    "id": crypto_id,
                    "price": result.get(vs_currency.lower()),
                    "market_cap": result.get(f"{vs_currency.lower()}_market_cap"),
                    "change_24h": result.get(f"{vs_currency.lower()}_24h_change"),
                    "currency": vs_currency.upper()
                }
            else:
                return {"success": False, "error": f"Asset '{crypto_id}' not found."}

        except requests.exceptions.RequestException as e:
            return {
                "success": False,
                "error": "API Connection Error",
                "details": str(e)
            }