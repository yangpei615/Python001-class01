# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class YangpeispiderPipeline:
    def process_item(self, item, spider):
        name = item['name']
        type = item['type']
        time = item['time']
        output = f'{name}\t{type}\t{time}\n\n'
        #第一周作业
        # with open('./maoyanmovie.csv',  encoding='utf-8', mode='a') as article:
        #     article.write(output)
        #第二周作业
        # 获取游标
        cursor=conn.cursor()
        # 执行sql语句
        sql = 'insert into  test (name,type,time) values(%s,%s,%s)="%s"' %(name,type,time)
        rows=cursor.execute(sql)  # 返回结果是受影响的行数
        
        # 关闭游标
        cursor.close()
        
        # 关闭连接
        conn.close()
        return item
    conn = pymysql.connect(host = 'localhost',
                       port = 3306,
                       user = 'root',
                       password = 'rootroot',
                       database = 'test',
                       charset = 'utf8mb4'
                        )
