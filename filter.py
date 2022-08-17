from pymongo import MongoClient, UpdateOne
import os

DATABASE_URL = os.environ.get('DATABASE_URL', 'Database url doesn\'t exist')
db = MongoClient(DATABASE_URL)

collection = db.abstracts['keywords2_dataset2']
docs = collection.find({})
filtered =  db.abstracts['filtered']

articles =[]
word = 'duck'

i = 0
for doc in docs:

    abs = doc['abstract']

    if word in abs:
        articles.append(abs)
        new_dict = {k: doc[k] for k in set(list(doc.keys())) - set(['_id'])}
        new_dict['filter_word'] = word
        filtered.insert_one(new_dict)

    i += 1
    print(f'Filter artles: {i}')


print(len(articles))




