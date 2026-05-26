"""
projekt_3.py: třetí projekt
author: Valeriia Miller
email: miller.lero4ka@gmail.com
"""

import csv
import requests
from bs4 import BeautifulSoup

ODKAZ = "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103"
VYSTUP = "vysledky_prostejov.csv"
ZAKLAD = "https://volby.cz/pls/ps2017nss/"


def nacti_stranku(url):
    odpoved = requests.get(url, timeout=10)
    odpoved.encoding = "utf-8"
    return BeautifulSoup(odpoved.text, "html.parser")


def ziskej_obce():
    soup = nacti_stranku(ODKAZ)
    kody = [td.text for td in soup.find_all("td", "cislo")]
    nazvy = [td.text for td in soup.find_all("td", "overflow_name")]
    url_obce = [ZAKLAD + td.find("a")["href"] for td in soup.find_all("td", "cislo") if td.find("a")]
    return list(zip(kody, nazvy, url_obce))


def ziskej_strany(url):
    soup = nacti_stranku(url)
    return [td.text for td in soup.find_all("td", "overflow_name")]


def zpracuj_obec(url):
    soup = nacti_stranku(url)
    volici = soup.find("td", headers="sa2").text.replace("\xa0", "")
    obalky = soup.find("td", headers="sa3").text.replace("\xa0", "")
    hlasy = soup.find("td", headers="sa6").text.replace("\xa0", "")
    vysledky = [td.text.replace("\xa0", "").replace("\u00a0", "") for td in soup.find_all("td", headers=["t1sb3", "t2sb3"])]
    return volici, obalky, hlasy, vysledky


def uloz_csv(radky, strany):
    hlavicka = ["code", "location", "registered", "envelopes", "valid"] + strany
    with open(VYSTUP, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(hlavicka)
        writer.writerows(radky)
    print(f"Hotovo! Výsledky uloženy do: {VYSTUP} ({len(radky)} obcí)")


def main():
    print("Stahuji seznam obcí...")
    obce = ziskej_obce()
    print(f"Počet obcí: {len(obce)}")

    strany = ziskej_strany(obce[0][2])
    print(f"Počet stran: {len(strany)}")

    radky = []
    for i, (kod, nazev, url) in enumerate(obce, 1):
        print(f"  [{i}/{len(obce)}] {nazev}", end="\r")
        volici, obalky, hlasy, vysledky = zpracuj_obec(url)
        radky.append([kod, nazev, volici, obalky, hlasy] + vysledky)
    print()

    uloz_csv(radky, strany)


main()
