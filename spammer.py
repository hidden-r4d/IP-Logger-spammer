import random
import requests
from proxyscrape import create_collector
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore

collector = create_collector('my-collector', 'https')
executor = ThreadPoolExecutor(max_workers=1000)

# Replace these with whatever you want (Maybe a little message for someone who thinks they're grabbing your IP ;)
agents = ["replace me", "example value", "test"]
referers = ["replace me", "example value", "test"]

print(Fore.GREEN+"IP LOGGER SPAMMER")
url = input(Fore.BLUE+"IP grabber: ")

def send_request(url,proxy):
    headers = {
            "user-agent": random.choice(agents),
            "referer": random.choice(referers)
        }
    try:
        req = requests.get(url, proxies={"http":proxy,"https":proxy}, headers=headers, timeout=15)
        status = req.status_code
        if status == 200:
            print(Fore.GREEN+"200: Successful."+"\n")
        elif status == 429:
            print(Fore.RED+"429: Too many requests."+"\n")
        elif status == 404:
            print(Fore.RED+"404: Not Found."+"\n")
        elif status == 403:
            print(Fore.RED+"403: Permission Denied."+"\n")
        else:
            print(Fore.RED+"Status Code: ",status)
    except IOError:
        print(Fore.RED+"Connection error - Bad Proxy."+"\n")
    except Exception:
        pass


while True:
    proxy = collector.get_proxy()
    port = proxy[1]
    proxy = proxy[0]
    proxy = proxy + ":" + port
    executor.submit(send_request, url, proxy)
