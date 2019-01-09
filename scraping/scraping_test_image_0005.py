def get_true_url(url):
    from bs4 import BeautifulSoup
    import requests

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

    return origin_url

def getHostname(url, withProtocol = False):
    import urllib.parse as parse

    p = parse.urlparse(url)
    if withProtocol:
        return "{}://{}".format(p.scheme, p.hostname)
    else:
        return p.hostname

def urljoin(url, path):
    import urllib.parse as parse
    return parse.urljoin(url, path)

def get_post_title(url):
    from bs4 import BeautifulSoup
    import requests

    res = requests.get(url).text
    soup = BeautifulSoup(res, 'html.parser')

    sel = "div.se_editArea > div > div > div > h3"
    result = soup.select(sel)[0].text.strip()
    print(result)
    return result

def get_images(url):
    from bs4 import BeautifulSoup
    import requests
    import platform

    os = platform.system()

    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    sel = ".se_mediaImage.__se_img_el"

    imgs = soup.select(sel)
    print(imgs, len(imgs))

    if len(imgs) < 1:
        exit()

    print("--------------------------------------")
    for img in imgs:
        src = img.get('src')
        print("img>>", src)
        if os == "Windows":
            with open("d:/workspace/hello/scraping/results/scraping_test_image_" + getFileName(src), "wb") as file:
                file.write(requests.get(src).content)
        elif os == "Darwin":
            with open("./results/scraping_test_image_" + getFileName(src), "wb") as file:
                file.write(requests.get(src).content)

def getFileName(url) :
    import urllib.parse as parse
    import os.path as path

    p = parse.urlparse(url).path
    return path.basename(p)

url = "https://blog.naver.com/baekmg1988/221405485574"
origin_url = get_true_url(url)
get_post_title(origin_url)
# get_images(origin_url)