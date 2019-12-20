import requests
import re
import pymysql
import os


def main():
    cookies = "30149280.1490161128.1576206569.1576206569.1576471522.2","30149280.5.10.1576471522","30149280","1","30149280.19907","30149280.1576471522.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic","tEd8dZXkrCpFSLWcBIzcN0E0x6mIixVJ","f05cd127d6ac6bce.1576474550.1.1576475408.1576474550.","[\"\",\"\",1576474550,\"https://movie.douban.com/top250?start=0\"]","*","D534194419FCA2BD4C1B09D0FA87334C9|37437f9bbf3fce60e61a9e04b5e1e378","0,6.0","gr5YcdfpSvk","\"199078573:aNfETjUyDN4\"","\"118146\"","0","0"
   # cookies = "think_language=zh-CN; kztoken=nJail6zJp6iXaJqWl29kYWRxYZib; his=a%3A2%3A%7Bi%3A0%3Bs%3A28%3A%22nJail6zJp6iXaJqWl29kYWRxYZeU%22%3Bi%3A1%3Bs%3A28%3A%22nJail6zJp6iXaJqWl29kYWRxYZib%22%3B%7D; _gat=1; MEIQIA_EXTRA_TRACK_ID=1NUcJTyLkJtGba7Zl9gVl45DnQb; expire=1562156326185; ypxs_show=true; _ga=GA1.3.1760558625.1562139044; MEIQIA_VISIT_ID=1NUcJTZyblUf2pyxxmXgCW2MuUW"
    # print(type(cookies))
    # cook_lst = cookies.split(";")
    # cook_dict = {}
    # print(type(cook_lst))
    # print(cook_lst)
    # for i in cook_lst:
    # kv = i.strip()
    # kv_lst = kv.split("=")
    # k = kv_lst[0]
    # v = kv_lst[1]
    # cook_dict[k] = v
    # print(cook_dict)


'''

db = pymysql.connect("127.0.0.1", "root", "123456", "fuhao", charset='utf8')
cursor = db.cursor()
sql1 = """INSERT INTO dianying
                 VALUES (%s,%s)"""
sql2 = """INSERT INTO dianshiju
                    VALUES (%s,%s)"""
sql3 = """INSERT INTO zongyi
                    VALUES (%s,%s)"""
sql4 = """INSERT INTO top250
                    VALUES (%s,%s)"""
'''
lst = []
for i in [0,25,50,75,100,125,150,175,200,225]:
    url = "https://movie.douban.com/top250?start={}".format(i)
    print(url)
    cookies = {
        "cookie": 'll="118146"; bid=gr5YcdfpSvk; __utma=30149280.1490161128.1576206569.1576206569.1576471522.2; __utmz=30149280.1576471522.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _vwo_uuid_v2=D534194419FCA2BD4C1B09D0FA87334C9|37437f9bbf3fce60e61a9e04b5e1e378; __utmb=30149280.10.10.1576471522; __utmc=30149280; ap_v=0,6.0; push_noty_num=0; push_doumail_num=0; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1576474550%2C%22https%3A%2F%2Fmovie.douban.com%2Ftop250%3Fstart%3D0%22%5D; _pk_id.100001.8cb4=f05cd127d6ac6bce.1576474550.1.1576476003.1576474550.; _pk_ses.100001.8cb4=*; __utmv=30149280.19907; __yadk_uid=tEd8dZXkrCpFSLWcBIzcN0E0x6mIixVJ; __utmt=1; ct=y; dbcl2="199078573:VnLOmbWTeEM"; ck=kJ3Y'
    }
    header = {
       # "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
         "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"

    }
    rets = []

    resp = requests.get(url, headers=header,cookies=cookies)
    # print(resp)
    # print(resp.status_code)
    data = resp.content.decode("utf-8")
    # print(data)
    with open("250.html", "w") as f:
        f.write(data)
    pattern0 = re.compile("""<span class="title">([\u4e00-\u9fa5]*)</span>""")
    #pattern1 = re.compile(
    #    """&nbsp;/&nbsp;([\u4e00-\u9fa5]*).*&nbsp;/&nbsp;""")
    # pattern0 = re.compile("""title="([\u4e00-\u9fa5]*)" target="_blank" data-aid=""")
    pattern1 = re.compile("""<span class="rating_num" property="v:average">(.*)</span>""")
    ret0 = pattern0.findall(data)
    ret1 = pattern1.findall(data)
    # ret = pattern1.findall(data)
    print(ret0)
    print(ret1)
    for q in range(0, 20):

        y = ret0[q]

        z = ret1[q]

        x = (y, z)

        lst.append(x)
'''
for w in lst:
    try:
        cursor.execute(sql4, w)
        db.commit()
    except:
        print("insert error")
        db.rollback()

print(lst)
'''
'''
    url1 = "http://top.iqiyi.com/dianshiju.html"
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    }
    rets = []
    lst1 = []




    resp = requests.get(url1, headers=header)
        #print(resp)
        #print(resp.status_code)
    data = resp.content.decode("utf-8")
        #print(data)
    with open("2.html", "w") as f:
        f.write(data)

    pattern0 = re.compile("""title="([\u4e00-\u9fa5]*)" target="_blank" data-aid=""")
    pattern1 = re.compile("""<em><i class="icon-fyb-hot"></i>热度&nbsp;(.*)</em>""")
    ret2 = pattern0.findall(data)
    ret3 = pattern1.findall(data)
    #ret = pattern1.findall(data)
    #print (ret0)
    #print(ret1)

    e=0
    for q in range(0,33):

            y = ret2[e]
            e=e+2
            z = ret3[q]

            x = (y,z)

            #print(x)
            lst1.append(x)
    for w in lst1:
        try:
            cursor.execute(sql2, w)
            db.commit()
        except:
            print("insert error")
            db.rollback()

    print(lst1)



    url2 = "http://top.iqiyi.com/zongyi.html"
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    }
    rets = []
    lst2 = []




    resp = requests.get(url2, headers=header)
        #print(resp)
        #print(resp.status_code)
    data = resp.content.decode("utf-8")
        #print(data)
    with open("3.html", "w") as f:
        f.write(data)

    pattern0 = re.compile("""title="([\u4e00-\u9fa5]*)" target="_blank" data-aid=""")
    pattern1 = re.compile("""<em><i class="icon-fyb-hot"></i>热度&nbsp;(.*)</em>""")
    ret4 = pattern0.findall(data)
    ret5 = pattern1.findall(data)
        #ret = pattern1.findall(data)
    #print (ret0)
    #print(ret1)

    e=0
    for q in range(0,20):

            y = ret4[e]
            e=e+2
            z = ret5[q]

            x = (y,z)

            #print(x)
            lst2.append(x)
    for w in lst2:
        try:
            cursor.execute(sql3, w)
            db.commit()
        except:
            print("insert error")
            db.rollback()

    print(lst2)

    '''
cursor.execute(sql4)

if __name__ == "__main__":
    main()