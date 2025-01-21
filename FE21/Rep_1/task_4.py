def currency_converter(src: str, dst: str, rate: float):
    # The function currency_converter, should return a function that takes the desired amount in the source currency as the only parameter and returns a string like X SRC is Y DST. The converted value should be rounded to two decimal places. Consider the assertions given below as examples for using currency_converter.

    def converter(amount=1):
        return f"{amount} {src} is {round(amount * rate, 2)} {dst}"

    return converter


# DO NOT SUBMIT THE LINES BELOW!
print(currency_converter("EUR", "CHF", 1.1)(5) == "5 EUR is 5.5 CHF")
chf_to_jpy = currency_converter("CHF", "JPY", 123)
print(chf_to_jpy(1) == "1 CHF is 123 JPY")
print(chf_to_jpy(2) == "2 CHF is 246 JPY")
print(currency_converter("Peanuts", "Pinecones", 0.2)
      (50) == "50 Peanuts is 10.0 Pinecones")
print(currency_converter("Blemflarcks", "Coins", 0.0021)
      (333.3) == "333.3 Blemflarcks is 0.7 Coins")
