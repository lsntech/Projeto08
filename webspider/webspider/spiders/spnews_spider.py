import scrapy

from webspider.items import WebspiderItem
from pymongo import MongoClient


def linear_search(lista, value):
        for i in range(len(lista)):
            if lista[i] == value:
                return True
        return False


class SPNewsSpider(scrapy.Spider):
    name = "spnews_spider"
    item = WebspiderItem()
    maxpagination = 1
    pagecounter = 1
    newRegistros = 0
    
    start_urls = ["http://www.saopaulo.sp.gov.br/ultimas-noticias"]


    client = MongoClient()
    query = client.noticias.artigos.find()
    lista_etags = []
    lista_titulos = []

    
    
    

    def parse(self, response) :
        
        news = response.css('div.col-md-8') #Pega a div com as noticias
        pagination = response.css('div.pagination a.next::attr("href")').get()

        
        try:
            for data in self.query:
                self.lista_etags.append(data['etag'])
                self.lista_titulos.append(data['title'])

                #print(data['title'])
        except KeyError as e:
            print(e)        


        
        for post in news: # para cada post pega o link
            link = post.css('div.col-md-5 h3.title a::attr("href")').get()
            

            if link:
                yield response.follow(link, callback=self.parse_link)   # segue o link
        
        
        while self.pagecounter < self.maxpagination:
            self.pagecounter += 1
            yield response.follow(pagination, callback=self.parse)
                     

    
    def parse_link(self, response): # chega ate e pagina e faz o parse.
        
        # Pega o etag atual da pagina a ser tratada
        etag = str(response.headers.get("ETag")).split('"')[1]
        

        conteudo = response.css("div.content")
        titulo = conteudo.css("h1.title::text").get()

        if not (linear_search(self.lista_titulos, titulo) and linear_search(self.lista_etags, etag)):
                print("========================================================")
                self.newRegistros +=1
                print("Adicionando novos registros: %d "  % self.newRegistros)
                
                self.item["url"]     = response.url
                self.item["etag"]    = etag
                self.item["title"]   = conteudo.css("h1.title::text").get()
                self.item["excerpt"] = conteudo.css("p.excerpt::text").get()
                self.item["date"]    = conteudo.css("header.article-header span.date::text").get()
                self.item["article"] = conteudo.css("article.article-main").get()
                yield self.item  

        
        

