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



def getRequiredEpisode(name,url):
        epiList=[]
        isFound=False
        i=1
        while(isFound ==False):
            soup = bs4.BeautifulSoup(requests.get(url+'?page='+str(i),headers=headers), "html.parser")
            

        return (epiDetails , soup, ch)
