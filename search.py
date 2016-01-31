import sys
from dateutil.relativedelta import *
import requests,bs4
import datetime
import functions
from dateutil.parser import parse
link = 'https://kat.cr/usearch/'

http_proxy  = "http://10.10.1.10:3128"
https_proxy = "https://10.10.1.11:1080"
ftp_proxy   = "ftp://10.10.1.10:3128"
proxyDict = {
              "http"  : http_proxy,
              "https" : https_proxy,
              "ftp"   : ftp_proxy
            }



if (len(sys.argv)):

    args=sys.argv[1:]

    #url= link + '+'.join(list(map(str,args)))
    url='https://kat.cr/usearch/the%20big%20bang%20theory/'

    res=requests.get(url,proxies=proxyDict)
    try:
        res.raise_for_status()
    except Exception as exc:
        print('There was a problem: %s' % (exc))
    op= open("OutPut Page.txt",'wb')
    scrape= bs4.BeautifulSoup(res.text,"html.parser")
    x=str(scrape.find_all('h1'))
    #print(x.get('href'))

    path = x [ (x.find('href="') +6) :( x.find('/">'))]
    url='https://kat.cr'+path
    res=requests.get(url,proxies=proxyDict)
    fout = open("Result.html",'wb')
    for i in res.iter_content(2000):
        fout.write(i)

    fout.close()

    url='https://kat.cr'+path
    print(path)


    soup = bs4.BeautifulSoup(open("Result.html"), "html.parser")
    body= open("EpiDetails.txt",'w')
    epiName=soup.find_all('span', class_="versionsEpName")
    epiNo=soup.find_all('span', class_="versionsEpNo")
    epiDate=soup.find_all('span', class_="versionsEpDate")
    seasonNo= soup.find_all('h3')
    seasonNo=seasonNo[0].get_text()
    for x in range(5):
        body.write(epiDate[x].get_text().strip() +'-'+ epiNo[x].get_text().strip()+ '-'+epiName[x].get_text().strip())
        body.write('\n')
    body.close()
    body= open("EpiDetails.txt",'r')
    l=[body.readline().split('-')[0] for i in range(5)]
    temp=l
    l=list(map(parse,l))

    today=datetime.datetime.now()


    rel=[]
    for i in l:
        rel.append(str(relativedelta(today,i)))

    days=[]
    for i in rel:

        if (('month' or 'year') not in i):
            i=i[i.index("days=")+5:]
            day= i.split(',')[0]
            days.append(int(day))
    epDict={}
    for i in range(len(days)):
        epDict[days[i]]= temp[i]

    days=list(filter(lambda x :x >=0 , days))
    days.sort()
    reqEpiDate= epDict[days[0]]

    body.close()
    body= open("EpiDetails.txt",'r')
    for i in body.readlines():
        if( reqEpiDate in i):
            reqEpi = i
            break

    if(reqEpi):
        res=requests.get(url+'/torrents/')
        torrentPage = open("Torrent Page.html",'wb')
        for i in res.iter_content(1000):
            torrentPage.write(i)
        torrentPage.close()

    else:
        print("Sorry No Match Found")
    


    reqEpi=functions.findReducedEpi(seasonNo,reqEpi)

    shortlisted= functions.findShortList(reqEpi)

    finalUrl=functions.produceFinalUrl(functions.bestMatch(shortlisted)[0])
    functions.download(finalUrl)
