import urllib.request
import ssl
import json
import datetime
import math
import pandas as pd
from itertools import count
from config import *

def get_request_url(url):
    request = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(request)
        if response.getcode() == 200:
            print('[%s] URL Request Success' %datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print('[%s] Error for URL : %s' %(datetiem.datetime.now(), url))

result = []

if __name__ == '__main__':
    searchBgnDe = '201601'
    searchEndDe = '202012'
    searchStatCd = 'US'
    numOfRows = '30'
    pageNo = '1'

    for pageNo in count():
        endPoint = 'http://openapi.customs.go.kr/openapi/service/newTradestatistics/getnationtradeList'
        parameter = '?_type=json&serviceKey=' + serviceKey
        parameter += '&searchBgnDe=' + searchBgnDe
        parameter += '&searchEndDe=' + searchEndDe
        parameter += '&searchStatCd=' + searchStatCd
        parameter += '&numOfRows=' + numOfRows
        parameter += '&pageNo=' + str(pageNo+1)
        url = endPoint + parameter
        
        resultData = get_request_url(url)
        jsonData = json.loads(resultData)

        isStop = False

        if jsonData['response']['header']['resultMsg'] == 'NORMAL SERVICE.':
            totalCount = jsonData['response']['body']['totalCount']
            if totalCount == 1:
                balPayments = jsonData['response']['body']['items']['item']['balPayments'] 
                expCnt = jsonData['response']['body']['items']['item']['expCnt'] 
                expDlr = jsonData['response']['body']['items']['item']['expDlr'] 
                impCnt = jsonData['response']['body']['items']['item']['impCnt'] 
                impDlr = jsonData['response']['body']['items']['item']['impDlr'] 
                statCd = jsonData['response']['body']['items']['item']['statCd'] 
                statCdCntnKor1 = jsonData['response']['body']['items']['item']['statCdCntnKor1'] 
                year = jsonData['response']['body']['items']['item']['year']
                year = str(year).replace('.','')
                result.append([year]+[statCdCntnKor1]+[statCd]+[impDlr]+[impCnt]+[expDlr]+[expCnt]+[balPayments])
            if totalCount > 1:
                for item in jsonData['response']['body']['items']['item']:
                    balPayments = item['balPayments'] 
                    expCnt = item['expCnt'] 
                    expDlr = item['expDlr'] 
                    impCnt = item['impCnt'] 
                    impDlr = item['impDlr'] 
                    statCd = item['statCd'] 
                    statCdCntnKor1 = item['statCdCntnKor1'] 
                    year = str(item['year']).replace('.','')
                    result.append([year]+[statCdCntnKor1]+[statCd]+[impDlr]+[impCnt]+[expDlr]+[expCnt]+[balPayments])
            if (pageNo+1) == math.ceil(int(totalCount)/int(numOfRows)):
                isStop = True
        if isStop : break   
    tradeList_table = pd.DataFrame(result, columns=('year','statCdCntnKor1','statCd','impDlr','impCnt','expDlr','expCnt','balPayments'))

    tradeList_table.to_csv('Multicampus/API/%s_%s_수출입실적(%s).csv' %(searchBgnDe, searchEndDe, statCd))
    print('테스트완료')



