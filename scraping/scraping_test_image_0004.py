from bs4 import BeautifulSoup
import requests

def getFileName(url) :
    import urllib.parse as parse
    import os.path as path

    p = parse.urlparse(url).path
    return path.basename(p)

def get_host(url):
    from urllib.parse import urlparse
    # from urlparse import urlparse  # Python 2
    parsed_uri = urlparse(url)
    result = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    return result


def get_true_url(url):
    import requests
    # import urllib.parse as parse
    # import os.path as path

    # print(">>>>>>>>>>>>>>>>>>>", parse.urlparse(url).hostname)
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    sel = "iframe#mainFrame"
    iframe = soup.select(sel)

    print(iframe, len(iframe))
    print("---------------------------")
    host = get_host(url)
    uri = iframe[0].get("src")
    print("origin url :  ", host + uri)
    return host + uri
    


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
    


# url = "https://blog.naver.com/baekmg1988/221405485574"
# origin_url = get_true_url(url)
# get_images(origin_url)


