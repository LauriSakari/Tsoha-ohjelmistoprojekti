Ohjelma kiipeilyseuran löytämiseen ja viestittelyyn

Toimintoja:

- Käyttäjätunnuksen luonti ja kirjautuiminen
- Käyttäjä voi merkitä greidin mitä tykkää kiivetä
- Voi merkitä haluaako kiivetä kovaa tai rennosti tms.
- Käyttäjä näkee yleisen keskustelualueen mihin voi lähettää viestejä 
- Käyttäjä näkee muiden käyttäjien asettamia vapaita kiipeilyaikoja
- Käyttäjä voi rajata hakuja eri kriteerien mukaan
- Käyttäjä voi varata toisen käyttäjän asettaman ajan 
- Käyttäjä voi pyytää muita käyttäjiä kaveriksi ja lähettää sitten kaverille yksityisviestejä 


Tilanne 17.11.24:

- Kayttäjä voi luoda käyttäjätunnuksen ja kirjautua sisään
- Käyttäjä voi valita kirjautumisen yhteydessä mitä greidiä haluaa kiivetä
- Samalla voi valita haluaako yleensä kiivetä kovalla intesiteetillä vai rennommin 
- Käyttäjä näkee yleisen keskustelualueen jossa näkyy muiden lähettämät viestit
- Käyttäjä voi lähettää viestin joka näkyy keskustelualueella
- Käyttäjä voi kirjautua ulos
- Kirjautumisen tai rekisteröitymisen epäonnistuessa käyttäjälle näkyy virheviestit

Käynnistysohjeet:

Kloonaa tämä repositorio omalle koneellesi ja siirry sen juurikansioon. Luo kansioon .env-tiedosto ja määritä sen sisältö seuraavanlaiseksi:
    DATABASE_URL=<tietokannan-paikallinen-osoite>
    SECRET_KEY=<salainen-avain>

Seuraavaksi aktivoi virtuaaliympäristö ja asenna sovelluksen riippuvuudet komennoilla:
    $ python3 -m venv venv
    $ source venv/bin/activate
    $ pip install -r ./requirements.txt

Määritä vielä tietokannan skeema komennolla:
    $ psql < schema.sql

Nyt voit käynnistää sovelluksen komennolla:
    $ flask run
