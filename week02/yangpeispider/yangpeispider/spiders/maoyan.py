import scrapy
import lxml
from scrapy.selector import Selector
from yangpeispider.items import YangpeispiderItem


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    # 起始URL列表
    start_urls = ['https://maoyan.com/films?showType=3']

    # def parse(self, response):
    #     pass
    #先注释掉默认函数parse


    # 爬虫启动时，引擎自动调用该方法，并且只会被调用一次，用于生成初始的请求对象（Request）。
    # start_requests()方法读取start_urls列表中的URL并生成Request对象，发送给引擎。
    # 引擎再指挥其他组件向网站服务器发送请求，下载网页
    def start_requests(self):
        #定义抓取的网页地址，抓取内容传参给psrse
        url = f'https://maoyan.com/films?showType=3'
        #第二周作业，增加try catch
        try:
            yield scrapy.Request(url=url, callback=self.parse, dont_filter=False)
            #获取网页的内容
            # url 请求访问的网址
            # callback 回调函数，引擎回将下载好的页面(Response对象)发给该方法，执行数据解析
            # 这里可以使用callback指定新的函数，不是用parse作为默认的回调参数
        except expression as e:
            print(e)
            


    #编写默认函数获取前10个电影链接
    def parse(self, response):
        icnt= 0
        try:
            movies = Selector(response=response).xpath('//div[@class="channel-detail movie-item-title"]')
            for movie in movies:
                link = movie.xpath('./a/@href')
                #截取xpath的第一个返回元素，拼接电影全路径，
                movie_url = 'https://maoyan.com' + str(link.extract()[0])
                # print(movie_url)
                yield scrapy.Request(url=movie_url, callback=self.parse2, dont_filter=False)
                icnt = icnt + 1 
                if icnt ==2:
                    break
        except expression as ex:
            print(ex)
        

    #获取电影名称、类型、上映时间
    def parse2(self, response):
         movie_info = Selector(response=response).xpath('//div[@class="movie-brief-container"]')
         movie_name = str(movie_info.xpath('./h1/text()').extract()[0])
         movie_time = str(movie_info.xpath('./ul/li[3]/text()').extract()[0])
         movie_type = movie_info.xpath('//a[@class="text-link"]/text()').extract()
         item = YangpeispiderItem()
         item['name'] = movie_name
         item['type'] = movie_type
         item['time'] = movie_time
         yield  item



