import sys
from dateutil.relativedelta import *
import requests,bs4
from datetime import *
from dateutil.parser import parse
link = 'https://kat.cr/usearch/'
if (len(sys.argv)):
    '''
    args=sys.argv[1:]

    #url= link + '+'.join(list(map(str,args)))
    url='https://kat.cr/usearch/the%20big%20bang%20theory/'

    res=requests.get(url)
    try:
        res.raise_for_status()
    except Exception as exc:
        print('There was a problem: %s' % (exc))
    op= open("OutPut Page.txt",'wb')
    scrape= bs4.BeautifulSoup(res.text,"html.parser")
    x=str(scrape.find_all('h1'))

    path = x [ (x.find('href="') +6) :( x.find('/">'))]
    url='https://kat.cr'+path
    res=requests.get(url)
    fout = open("Result.html",'wb')
    for i in res.iter_content(2000):
        fout.write(i)

    fout.close()
    '''
    soup = bs4.BeautifulSoup(open("Result.html"), "html.parser")
    body= open("EpiDetails.txt",'w')
    epiName=soup.find_all('span', class_="versionsEpName")
    epiNo=soup.find_all('span', class_="versionsEpNo")
    epiDate=soup.find_all('span', class_="versionsEpDate")

    for x in range(15):
        body.write(epiDate[x].get_text() +' -'+ epiName[x].get_text()+ '-'+epiName[x].get_text())
        #body.write(str((x).get_text()))
        body.write('\n')
    body.close()
    body= open("EpiDetails.txt",'r')
    l=[body.readline().split('-')[0] for i in range(15)]
    l=list(map(parse,l))
    today=date.fromtimestamp(time.time())
    #today = now
    print(today)
