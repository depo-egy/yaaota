# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3 

class TutorialPipeline:
    
    def __init__(self) :
        self.con = sqlite3.connect("ecommerce.db")
        self.cur = self.con.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS products(
            URL TEXT,
            TITLE TEXT,
            MAIN_CATEGORY TEXT
        )"""
        )

    def process_item(self, item, spider):
        self.cur.execute("""INSERT OR IGNORE INTO products VALUES (?,?,?)""",
                        (item['URL'],item['TITLE'],item['MAIN_CATEGORY']))
        self.con.commit()
        return item

#,,item['TITLE'],item['MAIN_CATEGORY']sku REAL PRIMARY KEY,item['sku']