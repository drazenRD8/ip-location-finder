# IP Location Finder

Mali Python alat koji pronalazi približnu lokaciju IP adrese koristeći [ipapi.co](https://ipapi.co/).

## Instalacija

pip install -r requirements.txt

## Pokretanje

python ip_location.py

## Primer

</> IP GEOLOCATION (PRO)
Unesi IP adresu: 8.8.8.8
Lokacija: Mountain View, United States (Provajder: Google LLC)

## Funkcije

- **Keširanje**: Poslednjih 100 IP adresa se čuva u memoriji (štedi API kvotu).
- **Rate limit handling**: Hvata `429` grešku i obaveštava korisnika.
- **User-Agent**: Jedinstven identifikator aplikacije.
- **Validacija**: Proverava da li je IP validna i da li je privatna.
- **HTTPS**: Sigurna veza sa API servisom.

## Napomena

Ovaj alat je napravljen za edukaciju i OSINT vežbe.
