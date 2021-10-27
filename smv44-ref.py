#!/usr/bin/python2.7
# -*- coding:utf-8 -*- 
import random
import sys
from random import randint
from time import sleep
import importlib
importlib.reload(sys)
import requests
from bs4 import BeautifulSoup
listeUserAgents = [ 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_5; fr-fr) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.2 Safari/525.20.1',
                                                'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.186 Safari/535.1',
                                                'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13\
',
                                                'Mozilla/5.0 (X11; U; Linux x86_64; en-us) AppleWebKit/528.5+ (KHTML, like Gecko, Safari/528.5+) midori',
                                                'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.107 Safari/535.1',
                                                'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-us) AppleWebKit/312.1 (KHTML, like Gecko) Safari/312',
                                                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11',
                                                'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.8 (KHTML, like Gecko) Chrome/17.0.940.0 Safari/535.8' ]

url = 'https://www.tesla.com/findus/list/superchargers/France'
bientot, cp, suc, sucv2, sucv3, nbsuc, bigv2, bigv3 = 0, 0, 0, 0, 0, 0, 0, 0
sitev2, sitev3, petitv2, petitv3, adrpetitv2, ardvpetitv3, adrgrosv2, adrgrosv3 = '', '', '', '', '', '', '', ''
smallv2, smallv3 = 10, 10
soon = {}
soonbis = {}
dep = {}

import re

def natural_sort(list, key=lambda s:s):
    """
    Sort the list into natural alphanumeric order.
    """
    def get_alphanum_key_func(key):
        convert = lambda text: int(text) if text.isdigit() else text 
        return lambda s: [convert(c) for c in re.split('([0-9]+)', key(s))]
    sort_key = get_alphanum_key_func(key)
    list.sort(key=sort_key)

if __name__ == "__main__":
    response = requests.get(url, headers={'user-agent': random.choice(listeUserAgents)})
    print((response.status_code))
    soup = BeautifulSoup(response.content, 'html.parser')
    for lien in soup.find_all('a'):
        if '/findus/location/supercharger' in lien['href']:
            if '(coming soon)' in lien.text:
           
                sitesoon = lien.text.split('(coming soon)')[0]
                bientot = bientot + 1
                print('il y a ',bientot,'SUC annonces ')
                print(lien.text)
                sleep(randint(3,5)) #pour éviter de se faire blacklister par les sites Tesla (erreur 403)
                print('numero ',cp)
                urlsuc = 'https://www.tesla.com/fr_FR' + lien['href']
                htmlsuc = requests.get(urlsuc, headers={'user-agent': random.choice(listeUserAgents)})
                if htmlsuc.ok:
                    soupsuc = BeautifulSoup(htmlsuc.content, 'html.parser')
                    target = soupsuc.findAll('strong')[0].text.split('Target opening in')[1].lstrip()
                    if 'Q' in target:
                        target1 = target.split(' ')[0]
                        target2 = target.split(' ')[1]
                        targ = target2 + ' ' + target1
                        adr = soupsuc.findAll("span",attrs={"class":"locality"})[0].text
                        print ('adr ',adr)
                        codps = [int(adr) for adr in adr.split() if adr.isdigit()]
                        soon[sitesoon] = targ
                    else:
                        targ = target + ' Q3'
                        soon[sitesoon] = targ
                    print(soon)
                    print('*' * 80)
            else:
                print(lien.text)
                cp = cp + 1
                sleep(randint(3,5)) #pour éviter de se faire blacklister par les sites Tesla (erreur 403)
                print('numero ',cp)
                urlsuc = 'https://www.tesla.com/fr_FR' + lien['href']
                htmlsuc = requests.get(urlsuc, headers={'user-agent': random.choice(listeUserAgents)})
                if htmlsuc.ok:
                    soupsuc = BeautifulSoup(htmlsuc.content, 'html.parser')
                    adr = soupsuc.findAll("span",attrs={"class":"locality"})[0].text
                    print ('adr ',adr)
                    vil = adr.split(' ')[1]
                    codps = adr.split(' ')[0]
                    dep[vil] = codps
#                    codps = [int(adr) for adr in adr.split() if adr.isdigit()]
                    print ('codps ',codps)
                    for infosuc in soupsuc.find(attrs={ "class":"vcard"}).findAll(text=True):
                        if 'upercharger' in  infosuc:
                            stalle = infosuc.split(' ')[0]
                            if '150' in infosuc:
                                sucv2 = sucv2 + int(stalle)
                                if  int(stalle) > bigv2:
                                    bigv2 = int(stalle)
                                    sitev2 = lien.text
                                    adrgrosv2 = soupsuc.findAll("span",attrs={ "class":"locality"})[0].findAll(text=True)[0]
                                if int(stalle) < smallv2:
                                    smallv2 = int(stalle)
                                    petitv2 = lien.text
                                    adrpetitv2 = soupsuc.findAll("span",attrs={ "class":"locality"})[0].findAll(text=True)[0]
                                print(stalle, ' SUC V2')
                            if '250' in infosuc:
                                sucv3 = sucv3 + int(stalle)
                                if int(stalle) > bigv3:
                                    bigv3 = int(stalle)
                                    sitev3 = lien.text
                                    adrgrosv3 = soupsuc.findAll("span",attrs={ "class":"locality"})[0].findAll(text=True)[0]
                                if int(stalle) < smallv3:
                                    smallv3 = int(stalle)
                                    petitv3 = lien.text
                                    adrpetitv3 = soupsuc.findAll("span",attrs={ "class":"locality"})[0].findAll(text=True)[0]
                                print(stalle, ' SUC V3')

                print('%s: %d' % ('nombre de stalles V2 ' , sucv2))
                print('%s: %d' % ('nombre de stalles V3 ' , sucv3))
                suc = suc + 1
                print('*' * 80)

    print('il y a ',bientot,'SUC annoncés ')
    print('les SUC annoncés')
    for v, k in sorted((v,k) for (k,v)in list(soon.items())):
        print(k," ouverture en ",v)
    print('il y a un total de ',suc, ' SUC operationnels')
    print('il y aura bientot ', suc + bientot, ' SUC')
    print('il y a ', sucv2, ' stalles à 150 kW')
    print('il y a ', sucv3, ' stalles à 250 kW')
    print('il y a un total de ', sucv2 + sucv3 , 'stalles')
    print('le plus grand V2 a',  bigv2, 'stalles à ', sitev2 , adrgrosv2)
    print('le plus grand V3 a',  bigv3, 'stalles à ', sitev3 , adrgrosv3)
    print('le plus petit V2 a', smallv2, 'stalles à ', petitv2, adrpetitv2)
    print('le plus petit V3 a', smallv3, 'stalles à ', petitv3, adrpetitv3)
    pass
 
