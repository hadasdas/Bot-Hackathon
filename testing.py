import requests
import sched, time


def extension2():
    print("===== extension 2 =====")
    s = sched.scheduler(time.time, time.sleep)
    res = requests.get(url='http://localhost:3000/priceCheck/chair').json()
    curr_price = res["price"]

    def try_to_buy():
        nonlocal curr_price
        res = requests.get(url='http://localhost:3000/priceCheck/chair').json()
        old_price = curr_price
        curr_price = res["price"]
        if curr_price < old_price:
            res = requests.get(url='http://localhost:3000/buy/chair')
            print(res.text)
            print("bought chair for less")
        else:
            print("still waiting for a price drop...")
            s.enter(3, 1, try_to_buy)
    s.enter(0, 1, try_to_buy)
    s.run()
