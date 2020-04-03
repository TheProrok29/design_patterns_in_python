from creative_design_patterns.factory_method.shop import Shop

my_shop = Shop(4)
my_shop.print_shop_info()
print()
print()
print()
another_shop = my_shop.__class__(8)
another_shop.print_shop_info()
