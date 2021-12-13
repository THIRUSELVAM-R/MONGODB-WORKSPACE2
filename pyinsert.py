import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["game"]
mycol = mydb["clan"]

mylist = [
  { "name": "samivan", "roles": ["clan leader","moderator","rank s++ hunter "]},
  { "name": "THIRU", "roles": ["shogun","rank s hunter"]},
  { "name": "bubu", "roles": ["shogun","rank s++ hunter","lepracon"]},
  { "name": "pensa", "roles": ["shogun","rank s++ hunter","power player"]}
]

x = mycol.insert_many(mylist)
print(x.inserted_ids)

for x in mycol.find():
    print(x)