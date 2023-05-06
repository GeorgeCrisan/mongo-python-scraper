### How to use venv shell ?

source venv/bin/activate


### How to start scrapy?

You can start your first spider with:
    cd rdpscraper
    <-----------------  name  -- URL ---------------->
    scrapy genspider example example.com

#### Scrapy shell ipython ?
    cd rdpscraper
    source venv/bin/activate
    scrapy shell

### Save to mongo
scrapy crawl -s MONGODB_URI="mongodb+srv://<userName>:<password>@maincluster.s9jsn2d.mongodb.net/?retryWrites=true&w=majority" -s MONGODB_DATABASE="scrapy" viseRo