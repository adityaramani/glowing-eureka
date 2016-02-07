import sys
from time import sleep
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
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


if (len(sys.argv)):

    args=sys.argv[1:]
    url= link + '+'.join(list(map(str,args)))
    name=' '.join(args)
    option = int(input("Enter Your Option : \n 1) Download Latest Episode \n 2) Choose From List"))
    while(option not in range(1,3)):
        option =int(input(" Wrong Choice Please Enter Correct Option as Shown Above : "))

    path=functions.findInitialPage(url,name)
    seriesLink="https://kat.cr"+path+'/torrents/'
    if(option == 1):
        seasonNo=functions.getEpisodeList(name)
        reqEpi= functions.calulations(name)
        print("donr 1 \n\n\n")
        if(reqEpi):
            sleep(10)

            res=requests.get(seriesLink,headers=headers)

            torrentPage = open(name+"Torrent Page.html",'wb')
            for i in res.iter_content(1000):
                torrentPage.write(i)
            torrentPage.close()
            reqEpi=functions.findReducedEpi(seasonNo,reqEpi)
            shortlisted= functions.findShortList(reqEpi,name)
            if(len(shortlisted) >0):
                finalUrl=functions.produceFinalUrl(functions.bestMatch(shortlisted)[0])
                functions.download(finalUrl)
            else:
                    print(" Sorry The Latest Episode Couldnt Be Found , Please try Option 2 ")
        else:
            print("Sorry No Match Found")
    else:
        fin = open(name+"Torrent Page.html" ,'r')
        if(fin):
            res= requests.get("https://kat.cr"+path+'/torrents/',headers=headers)
            for i in res.iter_content(1000):
                fin.write(i)
            fin.close()
        elif( properties(fin)):
            res= requests.get("https://kat.cr"+path+'/torrents/',headers=headers)
            for i in res.iter_content(1000):
                fin.write(i)
            fin.close()
        req=  addons.getRequiredEpisode(name,seriesLink)
