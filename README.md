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

Tilanne 01.12.24 edellisten toimitojen lisäksi

- Tietoturvaa parannettu validointien ja paranneltujen virheilmoitusten avulla
- Yksi taulu poistettu
- Käyttäjänimen on oltava minimissään 4 merkkiä pitkä ja salasanan 8
- Käyttäjä voi lisätä ajan jolloin hän olisi vapaa kiipeilelmään klikkaamalla
- Käyttäjä näkee listan vapaista ajoista 
- Käyttäjä voi varata toisen käyttäjän lisäämän vapaan ajan
- Käyttäjälle näytetään vahvistussivu jossa näkyy myös kaikki käyttäjän varaamat ajat
- Käyttäjä voi palata takaisin päänäkymään klikkaamalla paluulinkkiä
- Tämän jälkeen kaikki on vielä kesken eikä toimi oikein.

Tilanne 15.12.24 edellisten toimitojen lisäksi
 - tietoturvvaa parannettu lisäämällä csrf_token
 - Ulkonäköä parannettu ja selkeytetty
 - Koodi refaktoroitu käyttämään block contentia rakenteena
 - Käyttäjä pääsee sisäänkirjautuessa näkemään linkit joiden takaa löytyy seuraavat toiminnot:
    - voi nähdä ja kirjoittaa viestejä toisille käyttäjille ja poistaa omia viestejä.
    - voi ilmoittaa aikoja jolloin on vapaana kiipeämään 
    - voi nähdä listan muiden käyttämien ilmoittamia aikoja ja varata sieltä aikoja
    - voi nähdä listan omista varatuista ajoista  

Käynnistysohjeet:

Kloonaa tämä repositorio omalle koneellesi ja siirry sen juurikansioon. Luo kansioon .env-tiedosto ja määritä sen sisältö seuraavanlaiseksi:
```
    DATABASE_URL=<tietokannan-paikallinen-osoite>
    SECRET_KEY=<salainen-avain>
```
Seuraavaksi aktivoi virtuaaliympäristö ja asenna sovelluksen riippuvuudet komennoilla:
```
    $ python3 -m venv venv
    $ source venv/bin/activate
    $ pip install -r ./requirements.txt
```
Määritä vielä tietokannan skeema komennolla:
```
    $ psql < schema.sql
```
Nyt voit käynnistää sovelluksen komennolla:
```
    $ flask run
```