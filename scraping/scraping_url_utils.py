import urllib.parse as parse
import os.path as path
from bs4 import BeautifulSoup
import requests

def getFileName(url) :
    p = parse.urlparse(url).path
    return path.basename(p)

def getHostname(url, withProtocol = False):
    p = parse.urlparse(url)
    if withProtocol:
        return "{}://{}".format(p.scheme, p.hostname)
    else:
        return p.hostname

def get_true_url(url):
    # import urllib.parse as parse
    # import os.path as path

    # print(">>>>>>>>>>>>>>>>>>>", parse.urlparse(url).hostname)
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    sel = "iframe#mainFrame"
    iframe = soup.select(sel)

    print(iframe, len(iframe))
    print("---------------------------")
    host = getHostname(url)
    uri = iframe[0].get("src")
    print("origin url :  ", host + uri)

    origin_url = urljoin(getHostname(url, True), uri)
    print(origin_url)

    return host + uri

def urljoin(url, path):
    return parse.urljoin(url, path)
    
def get_iframe_src(url):

    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')

    selector = "iframe[src]"
    sss = soup.select_one(selector)
    path = sss.get("src")       
    host = getHostname(url)

    origin_url = "https://" + host + "/" + path
    print(origin_url)
    return origin_url

# url = "https://blog.naver.com/baekmg1988/221405485574"
# origin_url = get_true_url(url)


# if __name__ == '__main__':

#     print(getFileName(url))
#     print(getHostname(url))
#     print(getHostname(url, true))