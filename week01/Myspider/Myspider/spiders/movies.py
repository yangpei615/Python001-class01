import scrapy
import pandas
#from Myspider.items import SpidersItem
# from bs4 import BeautifulSoup
from scrapy.selector import Selector

class MoviesSpider(scrapy.Spider):
    # 定义爬虫名称
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    # 起始URL列表
    start_urls = ['https://maoyan.com']

#   注释默认的parse函数
#   def parse(self, response):
#        pass


    # 爬虫启动时，引擎自动调用该方法，并且只会被调用一次，用于生成初始的请求对象（Request）。
    # start_requests()方法读取start_urls列表中的URL并生成Request对象，发送给引擎。
    # 引擎再指挥其他组件向网站服务器发送请求，下载网页
    def start_requests(self):
        # for i in range(0, 10):
            i=0
            url = f'https://maoyan.com/films?showType=3'
            yield scrapy.Request(url=url, callback=self.parse, dont_filter=False)
            # url 请求访问的网址
            # callback 回调函数，引擎回将下载好的页面(Response对象)发给该方法，执行数据解析
            # 这里可以使用callback指定新的函数，不是用parse作为默认的回调参数

    # 解析函数
    def parse(self, response):
        # 打印网页的url
        print(response.url)
        # 打印网页的内容
        # print(response.text)
        icnt = 0
        # soup = BeautifulSoup(response.text, 'html.parser')
        # title_list = soup.find_all('div', attrs={'class': 'hd'})
        movies = Selector(response=response).xpath('//div[@class="channel-detail movie-item-title"]')
        for movie in movies:
        #     title = i.find('a').find('span',).text
        #     link = i.find('a').get('href')
            # 路径使用 / .  .. 不同的含义　
            title = movie.xpath('./a/text()')
            link = movie.xpath('./a/@href')
            newurls='https://maoyan.com'+ str(link.extract()[0])
            # print(newurls)
            # print('1：-----------')
            # print(title.extract())
            # print(link.extract())
            # print('1：-----------')
            yield scrapy.Request(url=newurls, dont_filter=False, callback=self.parse2)
            icnt = icnt + 1
            if icnt == 11:
             break
    # 解析具体页面
    
    def parse2(self, response):
        #item = response.meta['item']
        movie = Selector(response=response).xpath('//div[@class="movie-brief-container"]')
        movie_name = str(movie.xpath('./h1/text()').extract()[0])
        movie_date = str(movie.xpath('./ul/li[3]/text()').extract()[0])
        
        movie_type= movie.xpath('//a[@class="text-link"]/text()').extract()
        print('2：-----------')
        print(movie_name)
        print(movie_date)
        print(movie_type)
        print('2：-----------')
        mylist = [movie_name, movie_type, movie_date]
        movie = pandas.DataFrame(data=mylist)
        movie.to_csv('./movie.csv', encoding='gbk', index=False, header=False, mode='a')
        # output = f'|{movie_name}\t{movie_date}|\t|{movide_type}|\n\n'
        # with open('./maoyan.txt', 'a+', encoding='utf-8') as article:
        #     article.write(output)
        #     article.close()
       # yield item