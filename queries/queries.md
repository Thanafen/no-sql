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


# Average time by each country and device 

db.getCollection('clickstream').aggregate([

{$group:{
    _id:{device:"$device",
        country:"$country"
    },
        sum_time: {$sum:"$time_spent"}
    }
}
]);


# Min time spent by device and user

db.getCollection('clickstream').aggregate([

{$group:{
    _id:{
        device:"$device",
        _id:"$user_id"
    },
        min_time:{$min:"$time_spent"}
    }
} 
]);

# Return Only device and country, page, time spent === all except the user id
db.getCollection("clickstream").find({},
{
    device: 1,
    country: 1,
    page: 1,
    time_spent: 1,
    _id: 0
});

# Sort by time spent from max to min
db.getCollection("clickstream").find().sort({
    time_spent: -1
})

// combine last 2 queries
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

# Show top 3 highest engagement sessions == 3 top time spent

db.getCollection("clickstream").find().sort({time_spent: -1}). limit(3);

# Show the page with the lowest engagement session

db.getCollection("clickstream")
  .find(
    {},
    {
      page: 1,
      time_spent: 1,
      _id: 0,
    }
  )
  .sort({time_spent: 1})
  .limit(1);

# Show the lowest engagement session per page

db.getCollection("clickstream")
  .aggregate([{
    $group :{
        _id: "$page",
        lowest_time: {$min:"$time_spent"}
            }
    }
])

# Analytics pipeline example
// filter mobile users, group by page, calculate metrics and sort results
db.getCollection("clickstream").aggregate([
    {
        $match: {
          device:"mobile"
        }
    },
    {
    $group:{
        _id:"$page",
        avg_time: {$avg: "$time_spent"}
    }
    },
    {
    $sort: {
        avg_time: -1}
    }
])