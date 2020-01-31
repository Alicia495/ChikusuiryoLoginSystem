import os
import sys
import getpass
import urllib.request
import time
import msvcrt
from tqdm import tqdm

def login():
    print("緊急用プロトコル実行開始")
    url = 'http://10.10.10.10/cgi-bin/Login.cgi'
    method = 'POST'
    payload = {
        'uid': 'a58040rm',
        'pwd': 'Iphone495',
    }
    data = urllib.parse.urlencode(payload).encode('utf-8')
    res = urllib.request.Request(url, data=data, method=method)
    with urllib.request.urlopen(res) as response:
        print(response.read().decode('utf-8'))
    del data
    del payload


def main():
    print("パーソナルデータ 級長 を読み込み中...")
    for i in tqdm(range(50)):
        time.sleep(0.1)
    print("パーソナルデータ照合完了")
    time.sleep(0.5)
    print("寮ネット自動ログインシステムVer2.0.3を起動します...")
    for i in tqdm(range(14)):
        time.sleep(0.3)
    count = 0
    while (1):
        count += 1
        url = 'http://10.10.10.10/cgi-bin/Login.cgi'
        method = 'POST'
        payload = {
            'uid': 'a58040rm',
            'pwd': 'Iphone495',
        }
        data = urllib.parse.urlencode(payload).encode('utf-8')
        res = urllib.request.Request(url, data=data, method=method)
        with urllib.request.urlopen(res) as response:
            print(response.read().decode('utf-8'))
        del data
        del payload
        print("寮ネットシステム認証成功")
        print("現在",count,"回目のログインです")
        time.sleep(0.5)
        print("システムクールダウンフェーズ開始(約10分)")
        print("緊急的にログインしたい場合は何かキーを押してください（非推奨）")
        for i in tqdm(range(6000)):
            time.sleep(0.1)
            if msvcrt.kbhit():
                login()
                print("認証成功")
                print("緊急的にログインしたい場合は何かキーを押してください（非推奨）")
                
        print("寮ネットシステム認証開始")
if __name__ == '__main__':
   sys.exit(main())