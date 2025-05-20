# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


import pymongo


class MongoPipeline:
    def __init__(self, mongo_uri, mongo_db):  
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
# 2个参数： mongo_uri 是 MongoDB 的连接字符串，包含了连接所需的主机、端口等信息；mongo_db 是要连接的数据库名称
    @classmethod   #这是一个类方法装饰器，表明下面的方法是类方法，即可以通过类名直接调用，而不需要创建类的实例
    def from_crawler(cls, crawler):
        return cls(   #通过调用类的构造函数 cls，并传入从 crawler 的设置中获取的 MONGO_URI 和 MONGO_DATABASE，返回一个 MongoPipeline 类的实例
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        collection_name = 'tutututsafer'    #定义集合名称
        collection = self.db[collection_name]
        collection.insert_one(dict(item))  #将 item 转换为字典形式，然后使用 insert_one 方法将其插入到选定的集合 collection 中
        return item

    def close_spider(self, spider):
        self.client.close()