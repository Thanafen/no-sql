# NoSQL notes
# create a json file with some documents
# insert document to the database (MongoDB playground)
# basic queries like avg, min and sum and combinations of documents


# how to return specific keys and how to return specific key values from the database

# how to show only device, country, page, time spent (ascending)

db.getCollection("clickstream").find({},
{
    device: 1,
    country: 1,
    page: 1,
    time_spent: 1,
    _id: 0
})
.sort({
    time_spent: -1
})