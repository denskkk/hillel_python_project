from pprint import pprint as print
import httpx
import asyncio


class ExchangeRates:
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self) -> None:
        if ExchangeRates._initialized:
            return

        self.data: dict = asyncio.run(self._fetch_from_api())

        ExchangeRates._initialized = True

    @staticmethod
    async def _fetch_from_api() -> dict:
        url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=UAH&apikey=3B5LR2VELU7SHVL7"

        async with httpx.AsyncClient() as client:
            response = await client.get(url)

        return response.json()


er = ExchangeRates()

print(er.data)
