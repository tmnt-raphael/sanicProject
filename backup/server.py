import os
from sanic import Sanic
from sanic.response import text
from tortoise import Tortoise
from tortoise.contrib.sanic import register_tortoise
from models.finance import Quotes
import tortoise.timezone

pgHostname = os.getenv('PG_HOSTNAME')
dbUrl = "postgres://Ken:password@" + pgHostname + ":5432/kensdb"
myApp = Sanic("MySanicApp")

# serves static files
myApp.static("/", "index.html", name="homePage")
myApp.static("/createJob", "createJob.html", name="createJob")
myApp.static("/js", "js", name="jsFiles")

# serves endpoints
@myApp.get('/quote/test')
async def hello(request):
    return text("Test Quote")

@myApp.get('/quote/create')
async def create(request):
    curTime = tortoise.timezone.now()
    myExchange = "Binance"
    myLastPrice = 20123

    quote = await Quotes.create(timestamp=curTime, exchange=myExchange, lastPrice=myLastPrice)

    return text("Created a quote: " + str(curTime))

register_tortoise(
    myApp,
    db_url=dbUrl,
    modules={"models": ["models.finance"]},
    generate_schemas=False
)

if __name__ == '__main__':
    myApp.run(host='0.0.0.0', port=8000)












