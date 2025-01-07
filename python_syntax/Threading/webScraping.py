#multithreading for webscraping 
#it fetched multiple resource in the web and try to get o/p

import threading 
import requests
from bs4 import BeautifulSoup

urls = ['https://python.langchain.com/docs/concepts/',

'https://python.langchain.com/docs/introduction/',

'https://python.langchain.com/docs/versions/v0_2/deprecations/']


#webscraping 
def fetch_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content , 'html.parser')
    print(f"fetched {len(soup.text)} chracters from the {url}")
    
threads = []

for url in urls :
    thread = threading.Thread(target = fetch_content , args = (url , ))
    threads.append(thread)
    thread.start()
    
for thread in threads:
    thread.join()
    
print("All webpages fetched")
    