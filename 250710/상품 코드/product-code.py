product_name, product_code = input().split()
product_code = int(product_code)

class p:
    def __init__(self, name = 'codetree', code = '50'):
        self.name = name
        self.code = code


p1 = p()
p2 = p('leebros', '88')

print('product', p1.code, 'is', p1.name)
print('product', p2.code, 'is', p2.name)