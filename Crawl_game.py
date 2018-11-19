from bs4 import BeautifulSoup
import requests

class Game:
    title = ''
    def __init__(self, tag):
        self.title = self.get_tag(tag, 'a.title')
        self.comp = self.get_attr(tag, 'a.title', 'title')
        rating_tag = self.ge
        self.rating 
    
    def get_text(self, parent_tag, selector):
        tag = self.get_tag(parent_tag, selector)
        return tag.text.strip()
        # return "" if t == None else t.text.strip
    
    def get_attr(self, parent_tag, selector, attr_name):
        tag = self.get_tag(parent_tag, selector)
        return tag.get(attr_name).strip()
        # return "" if t == None else t.text.strip

    def get_tag(self, parent_tag, selector):
        tag = parent_tag.select(selector)
        if tag == None or len(tag) == 0:
            return None
        else:            
            return [0]
    
    def __str__(self):
        return "{} \t {}".format(self.title, self.comp)



