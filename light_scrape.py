import requests
from bs4 import BeautifulSoup

class LightNews:
    def __init__(self):
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'}
        self.url = 'https://www.light.gg/db/all?f=12'
        
        
    def search_link(self, keyword):

        response = requests.get(self.url + '(' + keyword + ')', headers = self.headers)
        content = response.content

        soup = BeautifulSoup(content, 'html.parser')
        
        result_links = soup.findAll('a', {"class": "text-exotic"})
        print(result_links)
        return result_links
    
    def send_link(self, result_links): 
        print("start")
        send_link = set()
        for link in result_links:
            text = link.text.lower()
            print(text)
            send_link.add('https://www.light.gg' + link.get('href'))
            break

        return send_link