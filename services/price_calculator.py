msg = "welcome to 4. semester python - exercise 1"
print(msg)

def get_user_input():
    user_input_number = input("Please enter number of items:  ")
    user_input_price = input("Please enter price of item:  ")

    return user_input_price, user_input_number


def calculate_price(price, number):
    return float(price) * int(number)   


def get_vat_in_europe(country_code):
    """
    Get the Value-Added Tax (VAT) rate for European countries.

    Parameters:
    - country_code: The country code.

    Returns:
    - vat_rate: The VAT rate for the specified country in Europe.
    """
    european_vat_rates = {
        "AT": 20,  # Austria
        "BE": 21,  # Belgium
        "BG": 20,  # Bulgaria
        "HR": 25,  # Croatia
        "CY": 19,  # Cyprus
        "CZ": 21,  # Czech Republic
        "DK": 25,  # Denmark
        "EE": 20,  # Estonia
        "FI": 24,  # Finland
        "FR": 20,  # France
        "DE": 19,  # Germany
        "GR": 24,  # Greece
        "HU": 27,  # Hungary
        "IE": 23,  # Ireland
        "IT": 22,  # Italy
        "LV": 21,  # Latvia
        "LT": 21,  # Lithuania
        "LU": 17,  # Luxembourg
        "MT": 18,  # Malta
        "NL": 21,  # Netherlands
        "PL": 23,  # Poland
        "PT": 23,  # Portugal
        "RO": 19,  # Romania
        "SK": 20,  # Slovakia
        "SI": 22,  # Slovenia
        "ES": 21,  # Spain
        "SE": 25,  # Sweden
    }

    country_code = country_code.upper()  # Convert to uppercase for case-insensitivity

    if country_code in european_vat_rates:
        return european_vat_rates[country_code]
    else:
        return None  # Return None for non-European countries or invalid codes



if __name__ == "__main__":
    print(get_user_input())
    price, number = get_user_input()
    print("price without vat:")
    total_price = calculate_price(price, number)
    print(total_price)

    country_code_input = input("Enter the country code: ")
    vat_rate = get_vat_in_europe(country_code_input)

    if vat_rate is not None:
        print(f"The VAT rate for {country_code_input} in Europe is {vat_rate}%.")
    else:
        print("Invalid country code or not a European country.")

    print("price with vat:")
    total_price_with_vat = total_price * (1 + vat_rate / 100)
    print(total_price_with_vat)

    print(get_user_input())
    price, number = get_user_input()
    print("price without vat:")
    total_price = calculate_price(price, number)
    print(total_price)

    country_code_input = input("Enter the country code: ")
    vat_rate = get_vat_in_europe(country_code_input)

    if vat_rate is not None:
        print(f"The VAT rate for {country_code_input} in Europe is {vat_rate}%.")
    else:
        print("Invalid country code or not a European country.")

    print("price with vat:")
    total_price_with_vat = total_price * (1 + vat_rate / 100)
    print(total_price_with_vat)
