
from selenium import webdriver
import os
from bs4 import BeautifulSoup
import urllib
import urllib.request
import pandas
import re

#test

class Scrapewebsite():



    def __init__(self,url):
        self.url = url





    def get_data(self,url):
        # Instantiate Chrome Browser Command
        driverLocation = "C:/chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.maximize_window()
        driver.get(url)

        #html content



        elementByClassname = driver.find_element_by_class_name('text')
        text = elementByClassname.text




        # wegschrijven
        dest = "C:\\Users\\Dennis.Pieruschka\\Documents\\Scraper\\Links"
        txt = ".txt"
        brackets = "\\"
        encoded_url = url[5:]
        encoded_url = encoded_url.replace('/','-') # replace / with -
        string = dest + brackets + encoded_url + txt
        with open(string, 'w') as f:
            f.write(text)
            f.close()







    def get_links_visservanbaars(self,url):
        global DeUrl
        pagina = urllib.request.urlopen(self.url)
        data = BeautifulSoup(pagina, "html.parser")
        rawlinks = []
        Links = []


        #######################################################
        # loop om alle links uit de html te halen

        def Linksophalen1():
            for rawlink in data.find_all('a'):
                rawlinks.append(rawlink.get('href'))


        Linksophalen1()




        #loop om alle links op te halen
        for link in rawlinks:
            if self.url == "http://www.visservanbaars.nl/vacatures?take=50&query=&criteria=" or self.url == "http://www.visservanbaars.nl/vacatures?page=2&take=50&query=&criteria=":
                link = re.findall(r'/\w{9}/\w.*', link) #regular expression voor /vacatures/functie
                Links.append(link)
            elif self.url == "https://www.bonque.nl/rss/4094174b-e2f9-4378-8ce5-7452d9b0e1e9":
                link = re.findall(r'/\w{8}/\w.*', link) #regular expression voor /vacatures/functie
                Links.append(link)
            elif self.url == "http://www.sourcepower.nl/index.php/page/adv_rss/command/getfeed/feed/5598198d7709029830b43f2a9e2019ec":
                link = re.findall(r'/\w{9}/.*', link) #regular expression voor /vacatures/functie
                Links.append(link)




        #filteren van de dataframe
        RawRegularExpressionsOutput = list(filter(len, Links)) # converting
        Dataframe = list(set(tuple(x) for x in RawRegularExpressionsOutput)) #for the nice dataframe
        vacatureLinks = list(map(list, Dataframe)) # for the links operations

        DataFrame = pandas.DataFrame(Dataframe) #TheDataframe

        if pandas.DataFrame(vacatureLinks) is not None:
            print(DataFrame)

        aantalLinks = len(vacatureLinks)
        print("Aantallinks zijn")
        print(aantalLinks)


        if self.url == "http://www.visservanbaars.nl/vacatures?take=50&query=&criteria=":
            DeUrl = "http://www.visservanbaars.nl"

        elif self.url == "http://www.visservanbaars.nl/vacatures?page=2&take=50&query=&criteria=":
            DeUrl = "http://www.visservanbaars.nl"




        teller = 0
        while teller < aantalLinks:
            firsthand = vacatureLinks[teller]
            firsthand.insert(0,DeUrl)
            link = firsthand[0] + firsthand[1]
            self.get_data(link)
            teller = teller + 1

        if teller > aantalLinks:
            print("scrapen is voltooid")



if __name__ == '__main__':
    #Invoer

    def Keuzemenu():
        global keuze
        Visservanbaars_pagina1 = "http://www.visservanbaars.nl/vacatures?take=50&query=&criteria="
        Visservanbaars_pagina2 = "http://www.visservanbaars.nl/vacatures?page=2&take=50&query=&criteria="
        bonque = "https://www.bonque.nl/vacatures"
        sourcepower = "http://www.sourcepower.nl/index.php/page/adv_rss/command/getfeed/feed/5598198d7709029830b43f2a9e2019ec"
        # Scraper object word aangemaakt
        # Navigatorfunctie word uitgevoerd
        keuze = int(input("Welkom bij de scraper vul 1 voor visser van baars vul 2 in voor visser van baars pagina 2 vul 3 in om Bonque te scrapen of vul 4 in op sourcepower op te halen:   "))
        if keuze == 1:
            keuze = Visservanbaars_pagina1
            Scraper = Scrapewebsite(keuze)
            Scraper.get_links_visservanbaars(keuze)
        elif keuze == 2:
            keuze = Visservanbaars_pagina2
            Scraper = Scrapewebsite(keuze)
            Scraper.get_links_visservanbaars(keuze)
        elif keuze == 3:
            keuze = bonque
            Scraper = Scrapewebsite(keuze)
            Scraper.get_links_visservanbaars(keuze)
        elif keuze == 4:
            keuze = sourcepower
            Scraper = Scrapewebsite(keuze)
            Scraper.get_links_visservanbaars(keuze)

    Keuzemenu()



















