html = '''
<table>
    <tr>
        <th>회사</th>
        <th>A사</th>
        <th>B사</th>
        <th>C사</th>
    </tr>
    <tr>
        <th>주소</th>
        <td>서울</td>
        <td>강원도</td>
        <td>부산</td>
    </tr>
    <tr>
        <th>직원수</th>
        <td>30명</td>
        <td>55명</td>
        <td>200명</td>
    </tr>
    <tr>
        <th>전화번호</th>
        <td>02-2345-2323</td>
        <td>033-223-2323</td>
        <td>051-121-1212</td>
    </tr>
    <tr>
        <th>대표메일</th>
        <td>a@a.com</td>
        <td>b@b.com</td>
        <td>c@c.com</td>
    </tr>
</table>
'''

# [] company_infos
# {} company_info
# database = { '회사' : [ { 'A' : {} },
#                        { 'B' : {} },
#                        { 'C' : {} }
#                      ]
#             }

def Company_DB(html):
    ## first row of the html table must be th.
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html, 'html.parser')
    selector = 'tr'
    re = soup.select(selector)
    database = {}
    company_names = {}
    yy = 0
    for rere in re:
        if yy == 0:
            rerere = rere.select_one('th:nth-of-type(1)').text
            database[rerere] = []
            comapany_cnt = len(rere.select('th'))
            for ii in range(comapany_cnt):
                if ii == 0:
                    continue           
                else:
                    selector = 'th:nth-of-type({})'.format(ii + 1)
                    aaa1 = rere.select_one(selector).text
                    database[rerere].append({aaa1 : {}})
                    company_names[aaa1] = ii - 1
        else:
            i = 1
            for company_name in company_names:
                selector = 'td:nth-of-type({})'.format(i)
                ddd = rere.select_one('th:nth-of-type(1)').text
                ddd1 = rere.select_one(selector).text
                database[rerere][i-1][company_name][ddd] = ddd1
                i += 1
        yy += 1
    print(database)
    print(company_names)
    # {'회사': [{'A사': {'주소': '서울', '직원수': '30명', '전화번호': '02-2345-2323', '대표메일': 'a@a.com'}}, {'B사': {'주소': '강원도', '직원수': '55명', '전화번호': '033-223-2323', '대표메일': 'b@b.com'}}, {'C사': {'주소': '부산', '직원수': '200명', '전화번호': '051-121-1212', '대표메일': 'c@c.com'}}]}
    # {'A사': 0, 'B사': 1, 'C사': 2}    
    return (database, company_names)
    
def get_value(db, company_name, attr, value, condition):
    ## condition 'f' is find, 'u' update, 'd' delete.
    company_index = db[1][company_name]

    if condition == 'f':
        db[0]['회사'][company_index][company_name][attr]

    elif condition == 'u':
        db[0]['회사'][company_index][company_name][attr] = value

    elif condition == 'd':
        del db[0]['회사'][company_index][company_name][attr]

    return db[0]['회사'][company_index][company_name][attr]   

if __name__ == "__main__": 
    db = Company_DB(html)
    result = get_value(db, 'B사', '전화번호', '033-223-2323', 'u')
    print(result)
 

