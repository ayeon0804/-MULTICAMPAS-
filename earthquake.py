import urllib.request
import ssl

import datetime
import pandas as pd
from itertools import count

context = ssl._create_unverified_context()

def get_request_url(url):
    request = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(request)
        if response.getcode() == 200:
            print('[%s] URL Request Success' %datetime.datetime.now())
            return response.read().decode('cp949')
    except Exception as e:
        print(e)
        print('[%s] Error for URL : %s' %(datetiem.datetime.now(), url))

if __name__ == "__main__":
    eq_list = []

    for page in count():
        endpoint = 'https://www.weather.go.kr/weather/earthquake_volcano/domesticlist.jsp?'
        params = 'startSize=2&endSize=999&schOption=T'
        params += '&startTm=' + '2020-01-01'
        params += '&endTm=' + '2021-01-28'
        params += '&pNo='+str(page+1)
        url = endpoint + params
        
        response = get_request_url(url)
        
        soupDate = BeautifulSoup(response, 'html.parser')
        table = soupDate.find('table', {'id':'excel_body'})
        tbody = table.find('tbody')
        trlist = tbody.find_all('tr')
        del trlist[-1]
        isStop = False
        for tr in trlist:
            tr = list(tr.strings)
    
            if tr[0] == '1':
                isStop = True
            # 발생시각, 규모, 깊이(km), 최대지도, 위도, 경도, 위치
            eq_info = {}
            eq_info['timestamp'] = tr[1]
            eq_info['magnitude'] = tr[2]
            eq_info['depth'] = tr[3]
            eq_info['mmi_scale'] = tr[4]
            eq_info['lat'] = tr[5]
            eq_info['lon'] = tr[6]
            eq_info['location'] = tr[7]
            eq_list.append(eq_info)
        if isStop == True:
            break;

    df = pd.DataFrame(eq_list)
    df = df[['timestamp','magnitude','depth','mmi_scale','lat','lon','location']]
    df.to_csv('Multicampus/API/earthquaketest.csv', encoding='utf-8')
    print('완료')


