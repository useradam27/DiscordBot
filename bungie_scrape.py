import requests
from bs4 import BeautifulSoup

class BungieNews:
    def __init__(self):
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'}
        self.url = 'https://www.bungie.net/en/News'
        
        
    def search_link(self):

        response = requests.get(self.url, headers = self.headers)
        content = response.content

        soup = BeautifulSoup(content, 'html.parser')
        
        #returns all hyperlinks with class atribute 'news-item'
        result_links = soup.findAll('a', {"class": "news-item"})
        return result_links
    
    #returns news links
    def send_link(self, result_links, type): 
        send_link = set()
        for link in result_links:
            text = link.text.lower()
            
            #checks if type to see if we are looking for current twab or hotfix
            if type == 1:
                if 'this week at bungie'in text:  
                    send_link.add('https://www.bungie.net' + link.get('href'))
                    break 
            if type == 2:
                if 'destiny 2 hotfix' in text:  
                    send_link.add('https://www.bungie.net' + link.get('href'))
                    break 
        return send_link