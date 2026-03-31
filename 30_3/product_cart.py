class Product:
    def __init__(self,name,order):
        self._name = name
        self._order = order #{order_id:(price,qty)}

    def get_price(self):
        total_price = 0
        for ord in self._order:
            total_price += self._order[ord][0] * self._order[ord][1]

        return f"Total bill for {self._name} is {total_price}"

    def get_order_detail(self):
        print(f"{self._name}")
        for ord_id, (price,qty) in self._order.items():
            print(f'{price} : {qty}')


class DiscountedProduct(Product):
    def __init__(self,name,order,discount):
        super().__init__(name,order)
        self._discount = discount

    def get_price(self):
        total = super().get_price()
        total = int(total.split(' ')[-1])
        return f"Total bill for {self._name} is {total - total * (1-self._discount)}"

class Cart:
    pass

if __name__ == '__main__':
    product = Product("Toothbrush",{'101':(20,2)})
    discount_product = DiscountedProduct("Soap",{'104':(10,3)},0.5)
    # print(product.get_price())
    # product.get_order_detail()
    # print(discount_product.get_price())
    print(discount_product.get_price())
    discount_product.get_order_detail()
    