#!/usr/bin/python3.9
# -*- coding:utf-8 -*-
import random
import sys
from random import randint
from time import sleep
import importlib

importlib.reload(sys)
import requests
from bs4 import BeautifulSoup
from collections import Counter
from pprint import pprint


def displayinfo(infosuc):
    global bigv2, bigv3, sucv2, sucv3, petitv2, petitv3, ouvv2, ouvv3, smallv2, smallv3, adrpetitv2, adrpetitv3, adrgrosv2, adrgrosv3, sitev2, sitev3
    if "upercharge" not in infosuc:
        return
    stalle = infosuc.lstrip().split(" ")[0]
    if len(stalle) > 3:
        stalle = stalle[:2]
    if "150" in infosuc:
        sucv2 = sucv2 + int(stalle)
        statv2[lien.text] = int(stalle)
        print ('statv2 ',statv2)
        if nt == True :
            ouvv2 = ouvv2 + int(stalle)
            print ('ouvv2 ',ouvv2)
        if int(stalle) > bigv2:
            bigv2 = int(stalle)
            sitev2 = lien.text
            adrgrosv2 = soupsuc.findAll("span", attrs={"class": "locality"})[0].findAll(
                text=True
            )[0]
        if int(stalle) < smallv2:
            smallv2 = int(stalle)
            petitv2 = lien.text
            adrpetitv2 = soupsuc.findAll("span", attrs={"class": "locality"})[
                0
            ].findAll(text=True)[0]
        print(stalle, " SUC V2")
    if "250" in infosuc:
        sucv3 = sucv3 + int(stalle)
        statv3[lien.text] = int(stalle)
        print ('statv3 ',statv3)

        if nt ==True:
            ouvv3 = ouvv3 + int(stalle)
            print ('ouvv3 ',ouvv3)
        if int(stalle) > bigv3:
            bigv3 = int(stalle)
            sitev3 = lien.text
            adrgrosv3 = soupsuc.findAll("span", attrs={"class": "locality"})[0].findAll(
                text=True
            )[0]
        if int(stalle) < smallv3:
            smallv3 = int(stalle)
            petitv3 = lien.text
            adrpetitv3 = soupsuc.findAll("span", attrs={"class": "locality"})[
                0
            ].findAll(text=True)[0]
        print(stalle, " SUC V3")
        print (statv2)
        print (statv3)
        

listeUserAgents = [
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_5; fr-fr) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.186 Safari/535.1",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13\
",
    "Mozilla/5.0 (X11; U; Linux x86_64; en-us) AppleWebKit/528.5+ (KHTML, like Gecko, Safari/528.5+) midori",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.107 Safari/535.1",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-us) AppleWebKit/312.1 (KHTML, like Gecko) Safari/312",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.8 (KHTML, like Gecko) Chrome/17.0.940.0 Safari/535.8",
]

url = "https://www.tesla.com/findus/list/superchargers/France"
url = "https://www.tesla.com/findus/list/superchargers/France"
#      https://www.tesla.com/findus/list/superchargers/France
bientot, cp, suc, sucv2, sucv3, nbsuc, bigv2, bigv3, ouvv2, ouvv3, nontesla = (
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
)
sitev2, sitev3, petitv2, petitv3, adrpetitv2, ardvpetitv3, adrgrosv2, adrgrosv3 = (
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
)
nt = False
smallv2, smallv3 = 10, 10
soon = {}
soonbis = {}
statv2 = {}
statv3 = {}
dep = {}
ntesla = []
if __name__ == "__main__":
    print (url)
    sleep(4)
    response = requests.get(url, headers={"user-agent": random.choice(listeUserAgents)})
    print((response.status_code))
    soup = BeautifulSoup(response.content, "html.parser")
    #while True:
    #    if 'Supercharger' in soup.title:
    #        print ("le titre ",soup.title)
    #        continue
    
    for lien in soup.find_all("a"):
        print ("lien ",lien)
        if "/findus/location/supercharger" in lien["href"]:
            if "(coming soon)" in lien.text:
                cp = cp + 1
                print("numero ", cp)
                sitesoon = lien.text.split("(coming soon)")[0]
                bientot = bientot + 1
                print("il y a ", bientot, "SUC annoncés ")
                print(lien.text)
                sleep(randint(2, 3))
                # pour éviter de se faire blacklister par les sites Tesla (erreur 403)
#https://www.tesla.com/findus/location/supercharger/airedurvillerssupercharger
                urlsuc = "https://www.tesla.com/findus/location/supercharger/" + lien["href"]
                htmlsuc = requests.get(
                    urlsuc, headers={"user-agent": random.choice(listeUserAgents)}
                )
                if htmlsuc.ok:
                    soupsuc = BeautifulSoup(htmlsuc.content, "html.parser")
                    target = (
                        soupsuc.findAll("strong")[0]
                        .text.split("Target opening")[1]
                        .lstrip()
                    )
                    adr = " ".join(
                        soupsuc.findAll("span", attrs={"class": "locality"})[0].findAll(
                            text=True
                        )
                    ).lstrip()
                    print(adr)
                    print(target)
                    soon[sitesoon] = target
                    print(soon)
                    print("*" * 80)
            else:
                print(lien.text.replace(" Supercharger-",""))
                cp = cp + 1
                sleep(randint(2, 3))  # pour éviter de se faire blacklister par les sites Tesla (erreur 403)
                print("numero ", cp)
                urlsuc = "https://www.tesla.com/fr_FR" + lien["href"]
                print(urlsuc)
                htmlsuc = requests.get(
                    urlsuc, headers={"user-agent": random.choice(listeUserAgents)}
                )
                if htmlsuc.ok:
                    nt = False
                    soupsuc = BeautifulSoup(htmlsuc.content, "html.parser")
                    for x in soupsuc.findAll("i"):
                        if "on-Tesla" in x.text:
                            nt = True
                            print(x.text)
                            nontesla = nontesla + 1
                            ntesla.append(lien.text)
                            print(ntesla)
                    adr = " ".join(
                        soupsuc.findAll("span", attrs={"class": "locality"})[0].findAll(
                            text=True
                        )
                    ).lstrip()
                    print(adr)
                    # print (soupsuc.findAll("section",attrs={"class":"find-us-list-details"})[0].findAll(text=True))
                    infosuc = (
                        soupsuc.findAll(
                            "section", attrs={"class": "find-us-list-details"}
                        )[0]
                        .findAll("strong")[0]
                        .nextSibling.nextSibling
                    )
                    # print (infosuc)
                    infosuclst = (
                        soupsuc.findAll(
                            "section", attrs={"class": "find-us-list-details"}
                        )[0]
                        .findAll("p")[1]
                        .findAll(text=True)
                    )
                    for infosuc in infosuclst:
                        displayinfo(infosuc)
                print("%s: %d" % ("nombre de stalles V2 ", sucv2))
                print("%s: %d" % ("nombre de stalles V3 ", sucv3))
                suc = suc + 1
                print("*" * 80)
    c = Counter(soon.values())
    print("nombre de sites Tesla ouverts aux non-Tesla : ", nontesla)
    for v in ntesla:
        print("\t",v)
    print("représentant ", ouvv2 + ouvv3, " stalles")
    print(ouvv2, "stalles V2")
    print(ouvv3, "stalles V3")
    for elon in c.keys():
        print("ouverture prévue en ", elon, " de ", c[elon], "SUCs")
    print("il y a ", bientot, "SUC annoncés ")
    print("les SUC annoncés")
    for v, k in sorted((v, k) for (k, v) in list(soon.items())):
        print("%30s ouverture en %12s" % (k, v))
    print("il y a un total de ", suc, " SUC opérationnels")
    print("il y aura bientot ", suc + bientot, " SUC")
    print("il y a ", sucv2, " stalles à 150 kW")
    print("il y a ", sucv3, " stalles à 250 kW")
    print("il y a un total de ", sucv2 + sucv3, "stalles")
    print(
        "le plus grand V2 a %3s stalles à %-50s%-30s"
        % (int(bigv2), sitev2.lstrip().rstrip(), adrgrosv2.lstrip().rstrip())
    )
    print(
        "le plus grand V3 a %3s stalles à %-50s%-30s"
        % (int(bigv3), sitev3.lstrip().rstrip(), adrgrosv3.lstrip().rstrip())
    )
    print(
        "le plus petit V2 a %3s stalles à %-50s%-30s"
        % (int(smallv2), petitv2.lstrip().rstrip(), adrpetitv2.lstrip().rstrip())
    )
    print(
        "le plus petit V3 a %3s stalles à %-50s%-30s"
        % (int(smallv3), petitv3.lstrip().rstrip(), adrpetitv3.lstrip().rstrip())
    )
    pass
print ('les v2')
for v,k  in sorted((v,k) for (k,v) in list(statv2.items())) :
    print("%60s-%4s" % (k.replace(" Supercharger",""),v))
# Iterate over the sorted sequence
print ('les v3')
for v,k in sorted((v,k) for (k,v) in list(statv3.items())) :
    print("%60s-%4s" % (k.replace(" Supercharger",""),v))    
