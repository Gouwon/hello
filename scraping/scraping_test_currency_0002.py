import scraping_url_utils as uu

## naver financial currency exchange scraping : 각 국가의 매매기준율과 현금에 대한 살때와 팔때의 차액.

def get_iframe_src(url):
    from bs4 import BeautifulSoup
    import requests

    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')

    selector = "iframe[src]"
    sss = soup.select_one(selector)
    path = sss.get("src")       
    host = uu.getHostname(url)

    origin_url = "https://" + host + "/" + path
    print(origin_url)
    return origin_url

def get_data(url):
    from bs4 import BeautifulSoup
    import requests

    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')

    selector = "tr"
    tags = soup.select(selector)

    print(type(tags))

    for tag in tags:
        print("__________________________")
        # print(tag)

        s_title = "td.tit"
        if tag.select_one(s_title) == None:
            continue
        country_name = tag.select_one(s_title).text.strip()

        s_ratio = "td.sale"
        country_ratio = float(tag.select_one(s_ratio).text.strip().replace(',',''))

        s_buy = "td:nth-of-type(3)"
        country_buying = float(tag.select_one(s_buy).text.strip().replace(',',''))

        s_sell = "td:nth-of-type(4)"
        country_selling = float(tag.select_one(s_sell).text.strip().replace(',',''))

        margin = country_buying - country_selling
        print("{},{},{}".format(country_name, country_ratio, margin))


url = "https://finance.naver.com/marketindex/"
origin_url = get_iframe_src(url)
get_data(origin_url)
