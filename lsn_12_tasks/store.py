class Product:
    def __init__(self, naming: str, typ: str, price: int):
        self.name = naming
        self.type = typ
        self.price = price


class ProductStore:
    def __init__(self, naming: str, start_discount=0, standart_nacenka=0):
        self.name = naming
        self.product_list = []
        self.start_discount = start_discount
        self.income = 0
        self.standart_nac = standart_nacenka

    def check_exist(self, prod):
        try:
            for product in self.product_list:
                if prod.name == product['name']:
                    return True
            return False
        except AttributeError:
            print('attribute error')

    def _price_update(self):
        try:
            for product in self.product_list:
                product.update(
                    {'real_price': product['start_price'] - product['start_price'] * product['discount'] / 100})
        except AttributeError:
            print('attribute error')

    def add(self, prod: Product, amount: int, discount=0, additional_price=0):
        if additional_price == 0:
            additional_price = self.standart_nac
        try:
            for product in self.product_list:
                if prod.name == product['name']:
                    product.update({'amount': product['amount'] + amount})
                    self._price_update()

                    return
            temp_dict = {'type': prod.type,
                         'name': prod.name,
                         'amount': amount,
                         'discount': discount + self.start_discount,
                         'start_price': prod.price + prod.price * additional_price / 100,
                         'real_price': prod.price
                         }
            self.product_list.append(temp_dict)
            self._price_update()
        except AttributeError:
            print('attribute error')
        except ValueError:
            print('value error')

    def set_discount(self, discount, prod: Product, howto):
        """
        |param discount:
        |param prod:
        |param howto: 'name' for name, 'type' for type
        """
        try:
            if self.check_exist(prod):
                if 0 <= discount <= 100:
                    for product in self.product_list:
                        if howto == 'name':
                            if prod.name == product['name']:
                                product.update({'discount': discount + self.start_discount})
                                self._price_update()
                        elif howto == 'type':
                            if prod.type == product['type']:
                                product.update({'discount': discount + self.start_discount})
                                self._price_update()
                        else:
                            print('Param error')
                        return
                else:
                    print('Discount can be 1-100 only')
                print('No such item in shop')
        except AttributeError:
            print('attribute error')

    def sell_product(self, prod: (str, Product), amount):
        try:
            if isinstance(prod, Product):
                for product in self.product_list:
                    if product['name'] == prod.name and product['amount'] > amount:
                        product.update({'amount': product['amount'] - amount})
                        self.income += product['real_price'] * amount
                        return
                    elif product['name'] == prod.name and product['amount'] == amount:
                        self.income += product['real_price'] * amount
                        self.product_list.remove(product)
                        return
            elif isinstance(prod, str):
                for product in self.product_list:
                    if product['name'] == prod and product['amount'] > amount:
                        product.update({'amount': product['amount'] - amount})
                        self.income += product['real_price'] * amount
                        return
                    elif product['name'] == prod and product['amount'] == amount:
                        self.income += product['real_price'] * amount
                        self.product_list.remove(product)
                        return
                print('not enough items in shop')
        except AttributeError:
            print('attribute error')

    def get_income(self):
        return self.income

    def get_all_products(self):
        return [{item['name']: item['amount']} for item in self.product_list]

    def get_product_info(self, name: str):
        return [{item['name']: item['amount']} for item in self.product_list if item['name'] == name]
