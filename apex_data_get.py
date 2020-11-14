#30 requests per 60 seconds.


#from pprint import pprint
import os
import sys
import json
import requests
base_url = 'https://public-api.tracker.gg/v2/apex/standard/'


api_key = 'your APIkey'
username = 'username you want to know'
#Platforms: 1 = XBOX 2 = PSN 5 = Origin / PC
platform = '5'


"""
ファイルに保存
"""
def write_data(json_data,filename):
    with open(filename + '.json', 'w') as f:
            json.dump(json_data, f, indent=4)

"""
プロファイルを取得
"""
def get_profile():
    params = {'TRN-Api-Key':api_key}
    endpoint = ('profile/{0}/{1}' .format(platform,username))
    session = requests.Session()
    res = session.get(base_url+endpoint,params=params)
    print(res.status_code)
    if res.status_code == 200:       
        json_data = res.json()
        res.close()
        write_data(json_data,'getprofile')
        #pprint(json_data) #ゲットしたデータを見たいときはコメントアウトを外す
        return json_data
    else:
        print('Error')
        sys.exit()


"""
プレイヤーを探す
"""
def search_profile():
    endpoint = 'search'
    params = {'TRN-Api-Key':api_key,
            'platform':platform,
            'query':username}

    session = requests.Session()
    res = session.get(base_url+endpoint,params=params)
    print(res.status_code)
    if res.status_code == 200:       
        json_data = res.json()
        res.close()
        write_data(json_data,'searchprofile')
        #pprint(json_data) #ゲットしたデータを見たいときはコメントアウトを外す
        return json_data
    else:
        print('Error')
        sys.exit()


"""
試合履歴を取得
"""
def get_history():
    endpoint = ('profile/{0}/{1}/sessions'.format(platform,username))
    params = {'TRN-Api-Key':api_key}

    session = requests.Session()
    res = session.get(base_url+endpoint,params=params)
    print(res.status_code)
    if res.status_code == 200:       
        json_data = res.json()
        res.close()
        write_data(json_data,'gethistory')
        #pprint(json_data) #ゲットしたデータを見たいときはコメントアウトを外す
        return json_data
    else:
        print('Error')
        sys.exit()
    

"""
メイン関数
"""
if __name__ == '__main__':
#
    json_data = get_profile()
    level = json_data['data']['segments'][0]['stats']['level']['value']
    kills = json_data['data']['segments'][0]['stats']['kills']['value']
    rankScore = json_data['data']['segments'][0]['stats']['rankScore']['value']
    activelegendName = json_data['data']['metadata']['activeLegendName']
    print('level:{}'.format(level))
    print('kills:{}'.format(kills))
    print('rankScore:{}'.format(rankScore))
    print('activelegendName:{}'.format(activelegendName))

#
    json_data = search_profile()
    platformUserHandle = json_data['data'][0]['platformUserHandle']
    print(platformUserHandle)

#
    json_data = get_history()
    i=0
    for x in json_data['data']['items'][0]['matches']:
        rankScore = json_data['data']['items'][0]['matches'][i]['stats']['rankScore']['value']
        i = i+1
        print('{}個目 score:{}'.format(i,rankScore))
