Enable a venv and install modules as pre requrements file in the root

### How to use venv shell ?

source venv/bin/activate


### How to start scrapy?

You can start your first spider with:
    cd rdpscraper

    scrapy genspider example example.com

#### Scrapy shell ipython ?
    cd rdpscraper

    source venv/bin/activate
    scrapy shell

### Start spider and save to mongo
    cd rdpscraper

    scrapy crawl -s MONGODB_URI="mongodb+srv://user:password@maincluster.s9jsn2d.mongodb.net/?retryWrites=true&w=majority" -s MONGODB_DATABASE="scrapy" generic

