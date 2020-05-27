actual_price = 2.5238933482398
depth_ps = 15
min_price_increment = 0.05


price_for_put = ((actual_price * (100 - depth_ps) / 100) // min_price_increment)\
                * min_price_increment


print(price_for_put)
