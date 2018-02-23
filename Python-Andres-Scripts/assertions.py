def apply_discount(product, discount):
    price = int(product['price']*(1-discount))
    assert 0 <= price <= product['price']
    return price


shoes = {'name': 'Fancy shoes', 'price': 14900}
# print(apply_discount(shoes, 0.25))
print(apply_discount(shoes, 1.25))

# Assertions are meant to perform internal checks
# Assertions should never be raised unless there are bugs
# Bugs = Undesired behaviors
