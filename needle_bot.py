from openapi_client import openapi
import datetime
from pytz import timezone

# Инициализация сессии с брокером
txt = open("c:\\Work\\Python\\Needle_bot\\1.txt", 'r').read()
token = f"{txt}"
client = openapi.api_client(token)


# t_from = datetime(2020, 3, 10, 14, 59, 0,tzinfo=timezone('Europe/Moscow'))
# t_to = datetime(2020, 3, 10, 15, 0, 0,tzinfo=timezone('Europe/Moscow'))


# Класс для акций
class ShareToFish:
    actual_price = 0
    min_price_increment = 0

    def __init__(self, figi, current_price):
        self.figi = figi
        self.current_price = current_price
        self.min_price_increment = client.market.market_search_by_figi_get(figi=self.figi).payload.min_price_increment

    def get_actual_price(self, now_time, time_frame):
        t_from = now_time - datetime.timedelta(minutes=1)
        share_dict = client.market.market_candles_get(figi=self.figi, _from=t_from.isoformat(),
                                                      to=now_time.isoformat(), interval=time_frame)
        return share_dict

    def put_limit_order_needle(self, depth_ps):
        price_for_put = (self.actual_price * (
                    100 - depth_ps) / 100) // self.min_price_increment * self.min_price_increment
        order_response = client.orders.orders_limit_order_post(broker_account_id=2010122667,
                                                               figi=self.figi,
                                                               limit_order_request={"lots": 1,
                                                                                    "operation": "Buy",
                                                                                    "price": price_for_put})
        return order_response


UNPRO = ShareToFish(figi='BBG004S686W0', current_price=0)
debug = True
now = datetime.datetime(2020, 5, 26, 18, 23) if debug else datetime.datetime.now()
now_time = timezone('Europe/Moscow').localize(now)


UNPRO.actual_price = UNPRO.get_actual_price(now_time=now_time, time_frame="1min").payload.candles[0].l
#a = UNPRO.put_limit_order_needle(15)

print(UNPRO.actual_price)
print(UNPRO.min_price_increment)
#print(a)

# t_to = datetime.datetime(2020, 5, 26, 18, 24, tzinfo=timezone('Europe/Moscow')) - datetime.timedelta(minutes=30)
#
# t_from = t_to - datetime.timedelta(minutes=1)
# x = client.market.market_candles_get(figi='BBG004S686W0', _from=t_from.isoformat(),
#                                      to=t_to.isoformat(), interval="1min")
# print(x)


# x = client.market.market_candles_get(figi='BBG004S686W0', _from=t_from.isoformat(),
#                                      to=t_to.isoformat(), interval="1min")
# y = client.market.market_search_by_figi_get(figi='BBG004S686W0')
#
#
# order_response = client.orders.orders_limit_order_post(broker_account_id=2010122667, figi='BBG004S686W0',
#                                                        limit_order_request={"lots": 1,
#                                                                             "operation": "Buy",
#                                                                             "price": 2.4})
# t_from = datetime.datetime(2020, 5, 26, 18, 18, tzinfo=timezone('Europe/Moscow'))
# t_to = datetime.datetime(2020, 5, 26, 18, 19, tzinfo=timezone('Europe/Moscow'))
