import sys
import requests,bs4
import webbrowser
link = 'https://kat.cr/usearch/'
if (len(sys.argv)):
    args=sys.argv[1:]

    url= link + '+'.join(list(map(str,args)))
    url='https://kat.cr/usearch/the%20big%20bang%20theory/'

    res=requests.get(url)
    try:
        res.raise_for_status()
    except Exception as exc:
        print('There was a problem: %s' % (exc))
    op= open("OutPut Page.txt",'wb')
    scrape= bs4.BeautifulSoup(res.text,"html.parser")
    x=str(scrape.find_all('h1'))

    path = x[ (x.find('href="') +6) :( x.find('/">'))]
    url='https://kat.cr'+path
    print(url)
    webbrowser.open(url)
