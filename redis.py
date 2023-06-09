# Bu kodun calismasi icin redis-server'in calisir halde olmasi gerekiyor.
# Temel islemler
import redis
# bir istemci objesi olustaralim.
r = redis.StrictRedis()

# Bir atama yapalim.
r.set("view_counter", 7)
# Atadigimiz degeri geri okuyup ekrana yazdiralim.
print(r.get("view_counter"))
# Output: 7
# Bir baska deger atayalim
r.set("view_counter", 15)
print(r.get("view_counter"))
# Output: 15
# Degeri arttiralim.
r.incr("view_counter")
# Degeri bir sayi kadar arttiralim
r.incr("view_counter", 4)

# Coklu atamalar
# Bir cok degeri tek bir cagri ile atamak icin

r.mset(id=3, view_count=6, read_count=1)  # Multiple SET
# mset fonksiyonu iki cins parametre aliyor
# 1. sekil **kwargs kullaniyor ve yukaridaki gibi atama yapabiliyorsunuz
ex_dict = {
    "key1": 1,
    "key2": 2
}
r.mset(ex_dict)
# Ya da dictionary olusturup arguman olarak verebiliyorsunuz.
# Ayni sekilde 'Key' degerlerin isimlerinden olusan bir liste verip karsilik gelen degerlerden olusan bir liste elde edebiliyoruz
key_list = r.mget(["id", "view_count", "view_counter", "key1"])

print(key_list)
