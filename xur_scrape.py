import requests
from bs4 import BeautifulSoup

class XurNews:
    def __init__(self):
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'}
        self.url = 'https://whereisxur.com/'
        
        
    def search_inventory(self):

        response = requests.get(self.url, headers = self.headers)
        content = response.content

        soup = BeautifulSoup(content, 'html.parser')
        
        result_links = soup.findAll('h4', {"class": "et_pb_module_header"})
        return result_links
    
    def send_inventory(self, result_links): 
        print("start")
        send_link = set()
        for link in result_links:
            text = link.text.lower()
            print(text)
            send_link.add(text)
        return send_link
    
    def search_location(self):
    
        response = requests.get(self.url, headers = self.headers)
        content = response.content

        soup = BeautifulSoup(content, 'html.parser')
        
        result_links = soup.findAll('h4', {"class": "title"})
        return result_links
    
    def send_location(self, result_links): 
        print("start")
        send_link = set()
        for link in result_links:
            text = link.text.lower()
            print(text)
            send_link.add(text)
        return send_link