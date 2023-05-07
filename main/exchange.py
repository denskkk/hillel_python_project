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
        self.rates = {
            ("USD", "EUR"): 1.096,
            ("EUR", "USD"): 0.912,
            ("USD", "USD"): 1.0,
            ("EUR", "EUR"): 1.0,
            ("USD", "UAH"): 37.4,
            ("UAH", "USD"): 0.0267,
            ("EUR", "UAH"): 41.0,
            ("UAH", "EUR"): 0.0244,
        }
        ExchangeRates._initialized = True

    def get_exchange_rate(self, from_currency: str, to_currency: str) -> float:
        if from_currency == to_currency:
            return 1.0

        rate = self.rates.get((from_currency, to_currency))
        if rate is None:
            raise ValueError(
                f"No exchange rate found for {from_currency} to {to_currency}"
            )

        return rate


def convert_currency():
    er = ExchangeRates()
    while True:
        currency_from = input("Enter currency (UAH, EUR, USD): ")
        currency_to = input("Enter currency (UAH, USD, EUR): ")
        amount = float(input("Enter amount to convert: "))

        if currency_from == currency_to:
            converted_amount = amount
        elif currency_from == "USD":
            converted_amount = amount * \
                               er.get_exchange_rate(currency_from, currency_to)
        elif currency_to == "USD":
            converted_amount = amount / \
                               er.get_exchange_rate(currency_to, currency_from)
        else:
            converted_amount = amount * \
                               er.get_exchange_rate(currency_from, "USD")
            converted_amount /= er.get_exchange_rate(currency_to, "USD")

        print(f"{amount} {currency_from} is equivalent to "
              f"{converted_amount:.2f} {currency_to}")


if __name__ == "__main__":
    convert_currency()
