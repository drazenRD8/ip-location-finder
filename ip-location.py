import requests
import ipaddress

def get_location(ip_address):
    # 1. Validacija IP adrese
    try:
        ipObj = ipaddress.ip_address(ip_address)
        # Opciono: Možeš spriječiti pretragu za privatne/lokalne IP adrese
        if ipObj.is_private:
            return "Greška: Unijeli ste privatnu/lokalnu IP adresu."
    except ValueError:
        return "Nevalidna IP adresa."
    
    # 2. Timeout i User-Agent
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    url = f"https://ipapi.co/{ip_address}/json/"
    
    # 3. Hvatanje grešaka
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        # Provjera da li je API vratio logičku grešku (npr. limit ili nepoznata IP)
        if data.get("error"):
            return f"API greška: {data.get('reason', 'Nepoznat razlog')}"
        
        # 4. Sigurna obrada podataka
        city = data.get("city", "Nepoznato")
        country = data.get("country_name", "Nepoznato")
        org = data.get("org", "Nepoznato")
        
        return f"Lokacija: {city}, {country} (Provajder: {org})"
        
    except requests.RequestException as e:
        return f"Greška u mreži: {e}"

# 5. Glavni dio programa
if __name__ == "__main__":
    ip = input("Unesi IP adresu: ")
    print(get_location(ip))