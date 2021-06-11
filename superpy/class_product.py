import csv
import os
import datetime
import weakref


class SystemState():
    """Methods relating the system state attributes and processing."""

    def __init__(self):
        self.today = self.set_system_today()
        self.line_number = 1
        self.system_inventory_list = []

    def proper_date(self, string_date):
        """Turns string-date into a proper date with format YYYY-MM-DD."""
        try:
            extended_date = f'{string_date} 00:00:00.000000'
            if extended_date != ' 00:00:00.000000':
                proper_date = datetime.datetime.strptime(extended_date,
                                                         '%Y-%m-%d %H:%M:%S.%f'
                                                         ).date()
            else:
                proper_date = ''
            return proper_date
        except ValueError as err:
            print("Please provide a proper date : ", err)

    # WORDT DEZE GEBRUIKT? IN REPORTS? IK GELOOF HET
    def proper_month(self, string_month):
        """Turns string-date into a proper month with format YYYY-MM-DD."""
        try:
            extended_date = f'{string_month}-00 00:00:00.000000'
            proper_month = datetime.datetime.strptime(extended_date,
                                                      '%Y-%m-%d %H:%M:%S.%f'
                                                      ).date()
            return proper_month
        except ValueError as err:
            print("Please provide a proper date : ", err)

    def proper_price(self, price):
        """Rewrites (*user input) price to string to valuta-notation."""
        str_price = str(price)
        if ',' in str_price:
            str_price.replace(',', '.')
        if '.' not in str_price:
            currency_str_price = f'{str_price}.00'
        elif str_price[-2] == '.':
            currency_str_price = f'{str_price}0'
        else:
            currency_str_price = str_price
        return currency_str_price

    def set_system_today(self):
        """Sets system.today based on date in 'superpy_date.txt'-file."""
        # get path to directory of current file main
        # file "superpy_date.txt" contains last exported reference_date
        path_current_file = os.path.dirname(os.path.realpath(__file__))
        if os.path.isfile(f'{path_current_file}/superpy_date.txt'):
            datefile_to_open = f'{path_current_file}/superpy_date.txt'
            with open(datefile_to_open) as superpy_date:
                date_from_file = superpy_date.readline()
                self.today = self.proper_date(date_from_file)
        # if no such file as superpy_date.txt, notice user + set virtual date
        else:
            virtual_date = '0001-01-01 00:00:00.000000'
            self.today = self.proper_date(virtual_date)
            print("""No valid date could be found. Please look at the user guide
                  how to provide a system date.
                  A file called 'superpy_date.txt' should be present.""")
        return self.today

    def change_system_today(self, new_date):
        """Sets system.today to new date and exports it to 'superpy_date.txt'-file
           as the new refererence-date for 'today'.
           Used in ShopAdmin.advance_time() function."""
        new_today = self.proper_date(new_date)
        self.set_system_today()
        self.today = new_today
        # no authorisation of user needed ; written to superpy_date
        path_current_file = os.path.dirname(os.path.realpath(__file__))
        datefile_to_open = f'{path_current_file}/superpy_date.txt'
        with open(datefile_to_open, 'w') as f:
            new_date_to_export = str(self.today)
            f.write(new_date_to_export)
        update = self.set_system_today()
        return update

    def get_import_data(self, importfile, imported_data):
        """General import function for importing csv.files."""
        try:
            path_current_file = os.path.dirname(os.path.realpath(__file__))
            file_to_open = f'{path_current_file}/{importfile}'
            # print('file to open is: ', file_to_open)
            with open(file_to_open, newline='') as csvfile:
                # reader = csv.DictReader(csvfile)
                reader = csv.DictReader(csvfile, delimiter=';')
                # self.no_of_lines = reader.line_num
                for row in reader:
                    imported_data.append(row)
            return imported_data
        except FileNotFoundError:
            print(f'Importfile {importfile} is missing, but should be place.')
            raise

    def append_dict_as_row(file_name, dict_of_elem, field_names):
        """Appends a dictionariy as a new row in csv file."""
        # Open file in append mode
        with open(file_name, 'a+', newline='') as write_object:
            # create a writer object from csv
            dict_writer = csv.DictWriter(write_object,
                                         fieldnames=field_names,
                                         delimiter=';')
            dict_writer.writerow(dict_of_elem)

    # Uiteindelijk niet gebruikt, maar behouden
    def get_length_of_file(file_name):
        path_current_file = os.path.dirname(os.path.realpath(__file__))
        file_to_open = f'{path_current_file}/{file_name}'
        file_to_count = open(file_to_open)
        reader = csv.reader(file_to_count)
        no_lines = len(list(reader))
        file_to_count.close()
        return no_lines

    def instantiate_one_product(self, product_dictrecord):
        # show = product_dictrecord.items()
        pd = product_dictrecord
        shop_today = SystemState().today
        p = Product(pd.pop('prod_name'),
                    SystemState().proper_date(pd.pop('exp_date')),
                    pd.pop('buy_price'))
        p_list = p.product_list
        # different instantiation for: new buys or imported records
        if pd.get('id'):
            if pd['id'] == 'INIT':          # case of new buy == not import
                p.id = (len(p_list) + 1)
            else:
                p.id = pd['id']
        if pd['buy_date'] == 'INIT':
            p.buy_date = shop_today         # case of new buy == not import
            p.buy_date = SystemState().today
        else:                               # case of import
            p.buy_date = SystemState().proper_date(pd.pop('buy_date'))
            # p.buy_date = pd.pop('buy_date')
        if pd['sold'] == 'True':
            p.sold = True
            p.sell_price = pd['sell_price']
            p.sell_date = SystemState().proper_date(pd['sell_date'])
        if pd['expired'] == 'True':
            p.expired = True
        p.discount_factor = pd['discount_factor']
        return p

    def instantiate_products(self, inventory_list):
        try:
            imported_dicts = self.get_import_data('product_data.csv', [])
            for product_dictrecord in imported_dicts:
                p = self.instantiate_one_product(product_dictrecord)
                inventory_list.append(p)
        except FileNotFoundError:
            print("""
                  Please have a look at the Superpy manual.
                  A file 'product_data.csv' is expected. This file is empty,
                  when you run Superpy for the first time.
                  When you used Superpy earlier, please check what happened to
                  the file 'product_data.csv'. It should contain all the data
                  of your earlier Superpy sessions. Maybe you accidentally
                  misplaced the file.
                  Please try to put the file back in place, so Superpy can
                  properly import your shop data.""")
        else:
            return inventory_list

    def update_csv(self, updated_dicts):
        fields = ['id', 'prod_name', 'prod_group', 'buy_date',
                  'exp_date', 'buy_price', 'sold', 'sell_date',
                  'sell_price', 'expired', 'discount_factor',
                  'footpr_fct']
        path_current_file = os.path.dirname(os.path.realpath(__file__))
        file_to_open = f'{path_current_file}/product_data.csv'
        with open(file_to_open, 'w', newline='') as csvfile:
            # create a writer object from csv
            dict_writer = csv.DictWriter(csvfile,
                                         fieldnames=fields,
                                         delimiter=';')
            dict_writer.writeheader()
            dict_writer.writerows(updated_dicts)
        return


class ShopAdmin():
    """Methods relating Shop Administration and Processes."""

    def __init__(self):
        self.prod_range = []
        self.inventory_list = []

    def export_buying(self, record_to_add):
        """exports new product's dictionary to csv."""
        path_current_file = os.path.dirname(os.path.realpath(__file__))
        file_to_open = f'{path_current_file}/product_data.csv'
        field_names = ['id', 'prod_name', 'prod_group', 'buy_date',
                       'exp_date', 'buy_price', 'sold', 'sell_date',
                       'sell_price', 'expired', 'discount_factor',
                       'footpr_fct']
        SystemState.append_dict_as_row(file_to_open, record_to_add,
                                       field_names)
        return

    def buy(self, name, exp_date, buy_price):
        """Instantiate new product and assemble it's record to export."""
        exp_date_string = exp_date
        exp_date_proper_date = SystemState().proper_date(exp_date_string)
        buy_price_proper_price = SystemState().proper_price(buy_price)
        prod_dict_to_add = {'id': 'INIT',
                            'prod_name': name,
                            'exp_date': exp_date_proper_date,
                            'prod_group': '',
                            'buy_date': 'INIT',
                            'buy_price': buy_price_proper_price,
                            'sold': False,
                            'sell_date': '',
                            'sell_price': '',
                            'expired': False,
                            'discount_factor': '1.0',
                            'footpr_fct': ''
                            }
        # instantiate product
        product_added = SystemState().instantiate_one_product(prod_dict_to_add)
        record_to_add = product_added.assemble_product_record()
        # write buy to CSV
        ShopAdmin.export_buying(self, record_to_add)
        new_product_list = list(product_added.instance_list)
        # update Shop administration's inventorylist
        ShopAdmin.update_inventory(self, new_product_list)
        return product_added

    def update_inventory(self, new_list):
        """Update ShopAdmin attribute for easy access to inventory."""
        sorted_list = [prod for prod in new_list]
        sorted_list.sort(key=lambda x: int(x.id))
        self.inventory_list = sorted_list
        new_list.sort(key=lambda x: int(x.id))
        self.inventory_list = new_list
        return self.inventory_list

    def sell(self, name, list_price):
        """Sell checks in stock, checks expiry, calculates discounts
           and exports changes."""
        all_products = self.inventory_list
        # check expiry of all products + update value for '.expired'
        all_not_sold = [x for x in all_products if x.sold is False]
        not_expired = [x for x in all_not_sold if x.check_expiry() is False]
        candidates = [p for p in not_expired if p.name == name]
        if len(candidates) == 0:
            p_to_sell = 'not_specified'                 # nothing to sell
        else:
            candidates.sort(key=lambda x: x.exp_date)   # FIFO-sort
            p_to_sell = candidates[0]
        # handle the selling of the product
        if p_to_sell == 'not_specified':
            print(f'"Sorry, currently no {name} in stock.')
        # check discount when expiry_date == today
        elif p_to_sell.exp_date == SystemState().today:
            p_to_sell.discount_factor = p_to_sell.check_discount()
            p_to_sell.sold = True
            calc_sell_price = (float(list_price) * p_to_sell.discount_factor)
            p_to_sell.sell_price = SystemState().proper_price(calc_sell_price)
            p_to_sell.sell_date = SystemState().today
        else:
            p_to_sell.sold = True
            p_to_sell.sell_price = SystemState().proper_price(list_price)
            p_to_sell.sell_date = SystemState().today
        # prepare export of all changes in products attributes (also expiries)
        if not(p_to_sell == 'not_specified'):
            all_updates = list(p_to_sell.getinstances())
            self.process_product_updates(all_updates)
        return

    def process_product_updates(self, updated_instance_list):
        """Process + export(1) current/updated state of all product instances.
           Returns input to update csv with all products (export2)."""
        # as input for update_csv --> export2
        updated = ShopAdmin.update_inventory(self, updated_instance_list)
        all_records = []
        for p in updated:
            product_record = p.assemble_product_record()
            all_records.append(product_record)
        SystemState().update_csv(all_records)
        return

    def advance_time(self, no_of_days):
        """Advances or reverses system.today with no_of_days,
           updates expiries and sellings and processes and exports all
           changes in the inventory.
           Expiries of sold products are untouched."""
        # #change_today()
        old_date = SystemState().set_system_today()
        new_date = old_date + datetime.timedelta(days=no_of_days)
        SystemState().change_system_today(new_date)
        inventory = self.inventory_list
        not_sold = [x for x in inventory if x.sold is False]
        # undo selling in case of reverse time
        sold = [x for x in inventory if x.sold is True]
        sellings_undone = 0
        for prod in sold:
            if type(prod.sell_date) != str:   # safetycheck on date format
                if prod.sell_date > new_date:
                    prod.sold = False
                    prod.sell_date = ''
                    prod.sell_price = ''
                    sellings_undone += 1
        # check expiry with new date; prod.expired may be reset (in check)
        new_expiries = 0
        for prod in not_sold:
            if prod.expired is False:
                if prod.check_expiry() is True:
                    prod.expired = True
                    new_expiries += 1
            if prod.expired is True:
                if prod.check_expiry() is False:
                    prod.expired = False              # reverse expiry
                    new_expiries -= 1
        if new_expiries != 0:
            print(f'Changing the date caused {new_expiries} expiry-changes.')
        if sellings_undone != 0:
            print(f'Changing date turned {sellings_undone} sellings back.')
        # undo buying -- not implemented
        # needs Product().delete_instances (implemented but not tested enough)
        actual_situation = [x for x in Product.getinstances()]
        actual_situation.sort(key=lambda x: int(x.id))
        self.process_product_updates(actual_situation)
        user_feedback = f"""
                         OK. Date is changed to {new_date}.
                         Date is also exported to file superpy_date.txt."""
        print(user_feedback)
        return new_date


class Product():

    _instances = set()

    def __init__(self, name, exp_date, buy_price):
        self._instances.add(weakref.ref(self))
        self.id = 'INIT'
        self.name = name
        self.buy_date = SystemState().today
        self.exp_date = SystemState().proper_date(exp_date)
        self.buy_price = buy_price
        self.sold = False
        self.expired = self.check_expiry()
        self.prod_group = self.find_product_group()
        self.footpr_fct = self.find_footpr_fct()
        self.prod_range = self.get_product_range()
        self.discount_factor = 1.0
        self.sell_date = ''
        self.sell_price = ''
        self.instance_list = self.getinstances()
        self.product_list = self.get_product_list('product_data.csv', [])

    @classmethod
    def getinstances(cls):
        dead = set()
        for ref in cls._instances:
            obj = ref()
            if obj is not None:
                yield obj
            else:
                dead.add(ref)
        cls._instances -= dead

    # NOT USED UPTO NOW
    @classmethod
    def delete_instances(cls):
        dead = set()
        for ref in cls._instances:
            obj = ref()
            del obj
            dead.add(ref)
        cls._instances -= dead

    @classmethod
    def from_dict_to_product(cls, dictionary):
        new_product = cls(**dictionary)
        return new_product

    def check_expiry(self):
        """Checks self.exp_date > today; if so, sets self.expired to True.
           When setting back time, 'unexpiry' for sold products is avoided."""
        try:
            # set default
            check = False
            if self.sold is False:
                if SystemState().today > self.exp_date:
                    self.expired = True
                    check = True
        except ValueError as err:
            print('Please provide a proper expiry_date: ', err)
        finally:
            return check

    def check_discount(self):
        """if expiring today default discount_factor is adjusted"""
        discount_factor = 1
        if SystemState().today == self.exp_date:
            discount_factor = 0.65
        return discount_factor

    def find_product_group(self):
        """look_up of product_group in table product_range.csv."""
        self.prod_group = ''
        range = SystemState.get_import_data(self, 'product_range.csv', [])
        for product in range:
            if self.name == product['prod_name']:
                self.prod_group = product['prod_group']
        return self.prod_group

    def find_footpr_fct(self):
        """footpr_fct is footprint weight [1-10] (social, environmental).
           look_up of product_group in table product_range.csv."""
        self.footpr_fct = ''
        range = SystemState.get_import_data(self, 'product_range.csv', [])
        for product in range:
            if self.name == product['prod_name']:
                self.footpr_fct = product['footpr_fct']
        return self.footpr_fct

    def get_product_range(self):
        """returns list of dictionaries, with key-pairs
                                {<prod_name>:X, <prod_group>:Y}."""
        result = SystemState.get_import_data(self, 'product_range.csv', [])
        self.prod_range = result
        return self.prod_range

    def get_product_list(self, input_file, product_list):
        '''loads the different product reports, to start a new session'''
        product_list = []
        product_list = SystemState.get_import_data(self, input_file, [])
        return product_list

    def assemble_product_record(self):
        product_record = {'id': self.id,
                          'prod_name': self.name,
                          'prod_group': self.prod_group,
                          'buy_date': self.buy_date,
                          'exp_date': self.exp_date,
                          'buy_price': self.buy_price,
                          'sold': self.sold,
                          'sell_date': self.sell_date,
                          'sell_price': self.sell_price,
                          'expired': self.expired,
                          'discount_factor': self.discount_factor,
                          'footpr_fct': self.footpr_fct
                          }
        return product_record
