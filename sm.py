#!/usr/bin/python2.7
# -*- coding:utf-8 -*- 
import requests
from bs4 import BeautifulSoup
import random
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from random import randint
from time import sleep
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
bientot = 0
cp = 0
suc = 0
sucv2 = 0
sucv3 = 0
nbsuc = 0
bigv2 = 0
bigv3 = 0
sitev2 = ''
sitev3 = ''
response = requests.get(url, headers={'user-agent': random.choice(listeUserAgents)})
print response.status_code
soup = BeautifulSoup(response.content, 'html.parser')
for x in soup.find_all('a'):
    if '/findus/location/supercharger' in x['href']:
        if '(coming soon)' in x.text:
            bientot = bientot + 1
            print 'il y a ',bientot,'SUC annonces '
            print x.text
            print '*' * 80
        else:
            print x.text
            print x['href']
            cp = cp + 1
            sleep(randint(3,12)) #pour éviter de se faire blacklister par les sites Tesla (erreur 403)
            print 'numero ',cp
            urlsuc = 'https://www.tesla.com/fr_FR' + x['href']
            print 'le site local ',urlsuc
            htmlsuc = requests.get(urlsuc, headers={'user-agent': random.choice(listeUserAgents)})
            print htmlsuc.ok
            if htmlsuc.ok:
                soupsuc = BeautifulSoup(htmlsuc.content, 'html.parser')
                for y in soupsuc.find(attrs={ "class":"vcard"}).findAll(text=True):
                    if 'upercharger' in  y:
                        print y.split(' ')[0], y.split(' ')[-1]
                        print 'nombre de stalles ', y.split(' ')[0]
                        if '150' in y:
                            sucv2 = sucv2 + int(y.split(' ')[0])
                            if  int(y.split(' ')[0]) > bigv2:
                                bigv2 = int(y.split(' ')[0])
                                sitev2 = x.text
                            print y.split(' ')[0], ' SUC V2'
                        if '250' in y:
                            sucv3 = sucv3 + int(y.split(' ')[0])
                            if int(y.split(' ')[0]) > bigv3:
                                bigv3 = int(y.split(' ')[0])
                                sitev3 = x.text
                            print y.split(' ')[0], ' SUC V3'

            print '%s: %d' % ('nombre de stalles V2 ' , sucv2)
            print '%s: %d' % ('nombre de stalles V3 ' , sucv3)
            suc = suc + 1
            print '*' * 80
                
print 'il y a ',bientot,'SUC annoncés '
print 'il y a un total de ',suc, ' SUC operationnels'
print 'il y aura bientot ', suc + bientot, ' SUC'
print 'il y a ', sucv2, ' stalles à 150 kW'
print 'il y a ', sucv3, ' stalles à 250 kW'
print 'il y a un total de ', sucv2 + sucv3 , 'stalles'
print 'le plus grand V2 a',  bigv2, 'stalles à ', sitev2
print 'le plus grand V3 a',  bigv3, 'stalles à ', sitev3