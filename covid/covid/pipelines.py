import pymongo


class WorkPipeline:

    def __init__(self):
        self.conn = pymongo.MongoClient('localhost', 27017)
        db = self.conn['covid']
        check = db.list_collection_names()
        if 'country_data' in check:
            db.country_data.drop()
        self.collection = db['country_data']

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item
