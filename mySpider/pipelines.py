# -*- coding: utf-8 -*-

import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class MyspiderPipeline(object):
    def __init__(self):
        # 建立连接
        self.conn = pymysql.connect('62.234.129.76','root','@^5%dJYWv6_a8[j}','rank')  # 有中文要存入数据库的话要加charset='utf8'
        # 创建游标
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        # print(item)
        # sql语句
        select_sql = """
        select `name` from `match` where `name` = '%s'
        """ % item['name']
        # print(select_sql)
        self.cursor.execute(select_sql)
        data = self.cursor.fetchall()
        if not data:
            # 数据库为空，进行插入操作
            inster_sql = """
            INSERT INTO `match`(`name`,src,`session`,victory,loss,scroe,rank) VALUES('%s','%s','%s',%s,%s,%s,%s)
            """ % (str(item['name']),str(item['src']),int(item['session']),int(item['victory']),int(item['loss']),int(item['scroe']),int(item['rank']))
            self.cursor.execute(inster_sql)
            self.conn.commit()
        else:
            # 数据库不为空，进行更新操作
            update_sql = """
            UPDATE `match` SET src = '%s',`session` = %s,victory = %s,loss = %s,scroe = %s,rank = %s WHERE `name` = '%s'
            """ % (str(item['src']),int(item['session']),int(item['victory']),int(item['loss']),int(item['scroe']),int(item['rank']),str(item['name']))
            self.cursor.execute(update_sql)
            self.conn.commit()
        
        return item

    def close_spider(self,spider):
        # 关闭游标和连接
        self.cursor.close()
        self.conn.close()
