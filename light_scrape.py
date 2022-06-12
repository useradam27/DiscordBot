import requests
from bs4 import BeautifulSoup

class LightNews:
    def __init__(self):
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'}
        self.url = 'https://www.light.gg/db/all?f=12'
        
    
    #seaches for specific search link on light.gg with the item's name as keyword    
    def search_link(self, keyword):

        response = requests.get(self.url + '(' + keyword + ')', headers = self.headers)
        content = response.content

        soup = BeautifulSoup(content, 'html.parser')
        
        #returns all hyperlinks with class atribute 'text-exotic'
        result_links = soup.findAll('a', {"class": "text-exotic"})

        return result_links
    
    def send_link(self, result_links): 
        send_link = set()
        for link in result_links:
            #adds href attribute to base link
            send_link.add('https://www.light.gg' + link.get('href'))
            break

        return send_link