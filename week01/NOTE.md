爬取猫眼电影学习笔记：

1.在电脑用pip命令安装第三方库后，Pycharm的file-setting设置解释器和Edit Configurations的解释器要保持一致，设置为python安装目录，否则会出现import导入第三方库，找不到相应的方法；

2.爬取网页出现多个重复标签，可以使用列表，再获取元素
  
  例如：movie_all = dtags("li")
        movie_all[0].text
        movie_all[1].text
      
3.导出数据到excle，使用mode=a，可追加内容；
  
  movie.to_csv('./movie.csv', encoding='gbk', index=False, header=False, mode='a')
  
4.遇到反爬虫，可以做如下操作：
  
   1：F12后查看headers的所有项，添加到代码中
   
   2：增加cookie
   
   3：请求的时候增加延迟时间
   
   4：使用requests.Session()
