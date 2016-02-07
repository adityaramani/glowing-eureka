
import bs4 , requests
import webbrowser
from time import sleep
import sys
from time import sleep
from dateutil.relativedelta import *
import requests,bs4
import datetime
import functions
from dateutil.parser import parse

http_proxy  = "http://10.10.1.10:3128"
https_proxy = "https://10.10.1.11:1080"
ftp_proxy   = "ftp://10.10.1.10:3128"
proxyDict = {
              "http"  : http_proxy,
              "https" : https_proxy,
              "ftp"   : ftp_proxy
            }
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def calulations(name):

        body= open(name+"EpiDetails.txt",'r')
        #body=open("suitsEpiDetails.txt",'r')
        l=[body.readline().split('-')[0] for i in range(10)]
        temp=l
        l=list(map(parse,l))
        today=datetime.datetime.now()
        rel=[]
        for i in l:
            rel.append(str(relativedelta(today,i)))
        days=[]
        print(rel)
        for i in rel:
            if (('month' or 'year') not in i):
                day= i.split(',')[0]
                day=day[day.index("=")+1:]
                days.append(int(day))
        epDict={}
        print("\n\n",days)
        for i in range(len(days)):
            epDict[days[i]]= temp[i]
        days=list(filter(lambda x :x >=0 , days))
        days.sort()
        print(epDict)
        print(days)
        reqEpiDate= epDict[days[0]]
        body.close()
        body= open(name+"EpiDetails.txt",'r')
        for i in body.readlines():
            if( reqEpiDate in i):
                reqEpi = i
                break
        return reqEpi


def getEpisodeList(name):

        soup = bs4.BeautifulSoup(open(name+".html"), "html.parser")
        body= open(name+ "EpiDetails.txt",'w')
        epiName=soup.find_all('span', class_="versionsEpName")
        epiNo=soup.find_all('span', class_="versionsEpNo")
        epiDate=soup.find_all('span', class_="versionsEpDate")
        seasonNo= soup.find_all('h3')
        seasonNo=seasonNo[0].get_text()
        for x in range(10):
            print(x,"\n")
            body.write(epiDate[x].get_text().strip() +'-'+ epiNo[x].get_text().strip()+ '-'+epiName[x].get_text().strip())
            body.write('\n')
        body.close()
        return seasonNo

def findInitialPage(url,name):
        sleep(20)
        res=requests.get(url,timeout=20,headers=headers)
        try:
            res.raise_for_status()
        except Exception as exc:
            print('There was a problem: %s' % (exc))

        name=' '.join([name])

        scrape= bs4.BeautifulSoup(res.text,"html.parser")
        x=str(scrape.find_all('h1'))
        path = x [ (x.find('href="') +6) :( x.find('/">'))]
        url='https://kat.cr'+path
        sleep(20)
        #INsert Sleep Here??
        res=requests.get(url,timeout=20,headers=headers)
        fout = open(name+".html",'wb')
        for i in res.iter_content(2000):
            fout.write(i)

        fout.close()
        print("path== ",path)
        return path

def key(arg):
    score=0
    if('hdtv' in arg):
        score+=1
    if('ettv' in arg):
        score+=1
    if('720' in arg):
        score-=1
    elif ('1080' in arg):
        score -=2

    return score

def findReducedEpi(seasonNo,reqEpi):
    sNo= seasonNo.strip()[-1:-3:-1][::-1]
    reqEpi = reqEpi.split('-')[1]
    reqEpi= reqEpi[-1:-3:-1] [::-1]
    return 's'+sNo+'e'+reqEpi

def findShortList(reqEpi,name):
    x=open(name+"Torrent Page.html", 'r')
    soup = bs4.BeautifulSoup(x, "html.parser")
    x=soup.find_all('a', title= 'Torrent magnet link')

    shortlisted=[]
    for i in (x):
            print(type(i.get('href')), i.get('href'))
            print(reqEpi , type(reqEpi))
            if( reqEpi in i.get('href')):
                shortlisted.append((i.get('href')))

    print(shortlisted)

    return shortlisted

def bestMatch (shortlisted):
    shortlisted=sorted(shortlisted, key = key,  reverse=True)
    return (shortlisted)

def produceFinalUrl(relLink):

    return relLink

def download(url):

    webbrowser.open(url)
