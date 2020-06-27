# -*- coding: utf-8 -*-
__author__ = 'yangpei'

# 使用requests库获取猫眼电影
# 使用BeautifulSoup解析网页
import requests
import time
import pandas
from bs4 import BeautifulSoup as bs
session = requests.Session()
header = {
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'Accept-Encoding': 'gzip, deflate, br',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'Cache-Control': 'max-age=0',
  'Connection': 'keep-alive',
  'Cookie':'__mta=45576603.1593069559427.1593222103091.1593223750285.24; uuid_n_v=v1; uuid=51926AA0B6B411EA8A833903D316728317FC2ED69C48402886911B638D0BEA4D; _csrf=9446b5084a67efc049261280c11c8cb2a313d8ec302ff86de44e727b0eea0b02; _lxsdk_cuid=172ea5855f4c8-038d461150973e-3b634504-1fa400-172ea5855f5c8; _lxsdk=51926AA0B6B411EA8A833903D316728317FC2ED69C48402886911B638D0BEA4D; mojo-uuid=837fb1cb6c6ca6fd219b7b9c14b2c978; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593069558; mojo-session-id={"id":"6e3c02c109409f62254de859991236be","time":1593221505962}; mojo-trace-id=24; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593225063; __mta=45576603.1593069559427.1593223750285.1593225063328.25; _lxsdk_s=172f366e4bd-dca-a3b-3cf%7C%7C38',
  'Host': 'maoyan.com',
  'Sec-Fetch-Dest': 'document',
  'Sec-Fetch-Mode': 'navigate',
  'Sec-Fetch-Site': 'none',
  'Sec-Fetch-User': '?1',
  'Upgrade-Insecure-Requests': '1',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
}
# 爬虫的网页地址
# 获取网页内容
# 解析网页内容
maoyanurl = 'https://maoyan.com/films?showType=3'
reponse = session.get(maoyanurl, headers=header)
reponse.encoding = 'utf-8'
bs_info = bs(reponse.text, 'html.parser')
time.sleep(10) #减少访问频次
#抓取前10个电影链接
icnt = 0



for tags in bs_info.find_all('div', attrs={'class': 'channel-detail movie-item-title'}):
  for atag in tags.find_all('a'):
    #获取电影连接
    movie_url = 'https://maoyan.com' + atag.get('href')
    # print(movie_url)
    #爬取电影详情页的名称、类型、上映时间
    reponsedetail = session.get(movie_url, headers=header)
    reponsedetail.encoding = 'utf-8'
    detail_info = bs(reponsedetail.text, 'html.parser')
    #for循环获取网页指定模块内容
    for dtags in detail_info.find_all('div', attrs={'class': 'movie-brief-container'}):
        movie_all = dtags("li")
        movie_name = dtags.find('h1',).text
        movie_type = movie_all[0].text
        movie_time = movie_all[2].text
        # print("电影名称: %s" % movie_name)
        # print("电影类型: %s" % movie_type)
        # print("电影上映时间: %s" % movie_time)
        mylist = [movie_name, movie_type, movie_time]
        movie = pandas.DataFrame(data=mylist)
        movie.to_csv('./movie.csv', encoding='gbk', index=False, header=False, mode='a')
    #     print(type(mylist))
    #     print(mylist)
    #     mylists.append(mylist)
    # print(mylists)

  #指定获取前10个电影
  icnt = icnt + 1
  if icnt == 10:
    break
