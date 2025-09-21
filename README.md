# Makuja
## Sovelluksen toiminnot:
- Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen. (TEHTY)
- Käyttäjä pystyy lisäämään sovellukseen ravintoloita. (TEHTY) Lisäksi käyttäjä pystyy muokkaamaan ja poistamaan lisäämiään ravintoloita. (EI TEHTY)
- Käyttäjä näkee sovellukseen lisätyt ravintolat. Käyttäjä näkee sekä itse lisäämänsä että muiden käyttäjien lisäämät ravintolat (TEHTY)
- Käyttäjä pystyy etsimään ravintoloita hakusanalla tai muulla perusteella. Käyttäjä pystyy hakemaan sekä itse lisäämiään että muiden käyttäjien lisäämiä ravintoloita.
- Sovelluksessa on käyttäjäsivut, jotka näyttävät jokaisesta käyttäjästä tilastoja ja käyttäjän lisäämät ravintolat
- Käyttäjä pystyy valitsemaan ravintolalle yhden tai useamman luokittelun. Mahdolliset luokat ovat tietokannassa.
- Sovelluksessa on pääasiallisen tietokohteen, eli ravintoloiden, lisäksi toissijainen tietokohde, eli arvostelut, jotka täydentävät pääasiallista tietokohdetta. Käyttäjä pystyy lisäämään arvosteluja itse lisäämiinsä ja muiden käyttäjien lisäämiin ravintoloihin. Arvosteluihin sisältyy numeroarvosana ja myös mahdollisuus kirjoittaa tekstimuotoinen kommentti.

## Sovelluksen asennus:
Kloonaa GitHub-repositorio omalle tietokoneellesi.
```
$ git clone https://github.com/oljn/makuja.git
```
Siirry lataamaasi kansioon.
```
$ cd makuja
```
Luo virtuaaliympäristö.
```
$ python3 -m venv venv
```
Aktivoi virtuaaliympäristö.
```
$ source venv/bin/activate
```
Asenna flask-kirjasto.
```
$ pip install flask
```
Luo tietokanta.
```
$ sqlite3 database.db < schema.sql
```
Voit nyt käynnistää sovelluksen.
```
$ flask run
```
