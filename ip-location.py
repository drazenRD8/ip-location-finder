import requests
import ipaddress
from functools import lru_cache

# Keširamo poslednjih 100 jedinstvenih IP adresa u memoriji radi štednje kvote
@lru_cache(maxsize=100)
def fetch_from_api(ip_address):
    # Jedinstven User-Agent identifikuje tvoju aplikaciju i smanjuje šansu za blokadu
    headers = {"User-Agent": "MySecureGeoApp/1.0 (Contact: admin@example.com)"}
    url = f"https://ipapi.co/{ip_address}/json/"

    response = requests.get(url, headers=headers, timeout=10)

    if response.status_code == 429:
        return {"error": "Dostignut limit upita na API servisu (Rate Limit). Pokušajte kasnije."}

    response.raise_for_status()
    return response.json()


def get_location(ip_address):
    try:
        ip_obj = ipaddress.ip_address(ip_address.strip())
        if ip_obj.is_private:
            return "Greška: Unijeli ste privatnu/lokalnu IP adresu."
    except ValueError:
        return "Nevalidna IP adresa."

    try:
        data = fetch_from_api(str(ip_obj))

        if "error" in data:
            return f"API greška: {data.get('error') if isinstance(data.get('error'), str) else data.get('reason', 'Nepoznat razlog')}"

        city = data.get("city", "Nepoznato")
        country = data.get("country_name", "Nepoznato")
        org = data.get("org", "Nepoznato")

        return f"Lokacija: {city}, {country} (Provajder: {org})"

    except requests.RequestException as e:
        return f"Greška u mreži: {e}"


if __name__ == "__main__":
    print("</> IP GEOLOCATION (PRO)")
    ip = input("Unesi IP adresu: ")
    print(get_location(ip))