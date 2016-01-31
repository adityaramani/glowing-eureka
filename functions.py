
import bs4 , requests
import webbrowser


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

def findShortList(reqEpi):

    soup = bs4.BeautifulSoup(open("Torrent Page.html") , "html.parser")
    x=soup.find_all('a', title= 'Torrent magnet link')

    shortlisted=[]
    for i in (x):
            if( reqEpi in i.get('href')):
                shortlisted.append(i.get('href'))

    return shortlisted

def bestMatch (shortlisted):
    shortlisted=sorted(shortlisted, key = key,  reverse=True)
    return (shortlisted)

def produceFinalUrl(relLink):
    
    return relLink

def download(url):

    webbrowser.open(url)
