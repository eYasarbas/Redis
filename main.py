import logging.config
import logging
import yaml
import redis

with open('log.yaml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

logger = logging.getLogger('redis')
# bir istemci objesi olustaralim.
r = redis.StrictRedis()
#consumer_data=
#r.set("vibration_data")
# Bir atama yapalim.
r.set("view_counter", 7)
logging.debug("Set view_counter to 7")

# Atadigimiz degeri geri okuyup ekrana yazdiralim.
view_count = r.get("view_counter")
logging.debug("Get view_counter: %s", view_count)

# Bir baska deger atayalim
r.set("view_counter", 15)
logging.debug("Set view_counter to 15")

view_count = r.get("view_counter")
logging.debug("Get view_counter: %s", view_count)

# Degeri arttiralim.
r.incr("view_counter")
logging.debug("Increment view_counter")

view_count = r.get("view_counter")
logging.debug("Get view_counter: %s", view_count)

# Degeri bir sayi kadar arttiralim
r.incr("view_counter", 4)
logging.debug("Increment view_counter by 4")

view_count = r.get("view_counter")
logging.debug("Get view_counter: %s", view_count)

# Coklu atamalar
# Bir cok degeri tek bir cagri ile atamak icin
r.mset({'id': 3, 'view_count': 6, 'read_count': 1})
logging.debug("Set multiple values: id=3, view_count=6, read_count=1")

# mset fonksiyonu iki cins parametre aliyor
# 1. sekil **kwargs kullaniyor ve yukaridaki gibi atama yapabiliyorsunuz
ex_dict = {"key1": 1, "key2": 2}
r.mset(ex_dict)
logging.debug("Set multiple values: %s", ex_dict)

# Ya da dictionary olusturup arguman olarak verebiliyorsunuz.
# Ayni sekilde 'Key' degerlerin isimlerinden olusan bir liste verip karsilik gelen degerlerden olusan bir liste elde edebiliyoruz
key_list = r.mget(["id", "view_count", "view_counter", "key1"])
logging.debug("Get multiple values: %s", key_list)
