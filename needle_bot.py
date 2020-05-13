from openapi_client import openapi
from datetime import datetime
from pytz import timezone

txt = open("c:\\Work\\Python\\Needle_bot\\1.txt", 'r').read()
token = f"{txt}"

print(datetime.now())
client = openapi.api_client(token)

t_from = datetime(2020, 3, 9, 15, 0, 0,tzinfo=timezone('Europe/Moscow'))
t_to = datetime(2020, 3, 10, 15, 0, 0,tzinfo=timezone('Europe/Moscow'))


#x = client.operations.operations_get(_from=t_from.isoformat(), to=t_to.isoformat(),
#                                     broker_account_id=2010122667)

x = client.market.market_candles_get(figi='BBG004S686W0', _from=t_from.isoformat(),
                                     to=t_to.isoformat(), interval="DAY")
y = client.market.market_search_by_figi_get(figi='BBG004S686W0')

print(x)
print(y)



