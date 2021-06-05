from class_product import Product
from class_product import SystemState
from class_product import ShopAdmin
import csv
import os
import datetime
import calendar
import pandas as pd
from prettytable import from_csv


class Report():
    def __init__(self):
        self.prod_range = Product.get_product_range(self)
        self.inventory_list = ShopAdmin().inventory_list

    def __str__(self):
        return f"Reports the {self.type} for specified time period."

    def change_report_date(inputdate, x_days):
        """Returns datetime-object that is x_days earlier or later
           than inputdate."""
        new_date = inputdate + datetime.timedelta(days=x_days)
        result = new_date
        return result

    def show_inventory_csv(self):
        """Show inventory.csv file as a table, using PrettyTable."""
        path_current_file = os.path.dirname(os.path.realpath(__file__))
        printfile = f'{path_current_file}/inventory.csv'
        with open(printfile, "r") as fp:
            x = from_csv(fp)
            print(x)

    def show_product_range_csv(self):
        """Show product_range.csv file as a table, using PrettyTable."""
        path_current_file = os.path.dirname(os.path.realpath(__file__))
        printfile = f'{path_current_file}/product_range.csv'
        with open(printfile, "r") as fp:
            x = from_csv(fp, field_names=["Product Name", "Product group",
                                          "Footprint Weight"])
            x_to_show = x[1:]
            print(x_to_show)

    # This one is not used, because show_product_range_csv looks nicer
    # But it is working, and meets requirement 'use of external module'
    def show_prod_range_as_table(self):
        """Show Shop's Product Range as a table, using Pandas.
           Shows dictionary input as a table."""
        prod_rge_dict1 = SystemState().get_import_data('product_range.csv', [])
        df = pd.DataFrame(prod_rge_dict1,
                          columns=['prod_name', 'prod_group', 'footpr_fct'])
        df.columns = ['Product name', 'Product Group', 'Footprint weight']
        print('\n', df)

    def export_rep_to_csv(self, fields, output_file, data_to_export):
        """Export instances of classes, with the specified fields, to
           specified output csv file."""
        path_current_file = os.path.dirname(os.path.realpath(__file__))
        file_to_open = f'{path_current_file}/{output_file}'
        with open(file_to_open, 'w', newline='') as csvfile:
            # create a writer object from csv
            dict_writer = csv.DictWriter(csvfile,
                                         fieldnames=fields,
                                         delimiter=';')
            dict_writer.writeheader()
            dict_writer.writerows(data_to_export)


class Fixed_date_report():
    """Input is 1. type from <'inventory', 'productrange'>,
       2. an inventory list and
       3. date string specifying the required reporting day).
        Format is <'now', 'yesterday, 'date YYYY-MM-DD'>.
        NB: 'date ' itself is part of the date request."""
    def __init__(self, type, inventory_list, date_request):
        self.type = type
        self.report_date = self.date_req_to_report_date(date_request)
        self.product_range = Product.get_product_range(self)
        self.inventory_list = inventory_list

    def date_req_to_report_date(self, date_request):
        """Transforms string-date-request in (list of) datetime.date dates.
           Expects: 'now', 'yesterday' or 'date YYYY-MM-DD'."""
        try:
            now = SystemState().today
            if date_request == 'now':
                req_report_date = now
            elif date_request == 'yesterday':
                req_report_date = now + datetime.timedelta(-1)
            else:                               # YYYY-MM-DD format
                if len(date_request) == 15:
                    proper_date = SystemState().proper_date(date_request[5:])
                    req_report_date = proper_date
            return req_report_date
        except UnboundLocalError:
            print("""Please provide a proper date for this type of report.
                  As reporting date 'today' was taken.""")

    def count_products(self, name, list):
        counter = 0
        for x in list:
            if x == name:
                counter += 1
        return counter

    def get_fd_report(self):
        """Assembles the data for the different reports."""
        if self.type == 'product_range':
            report_object = self.product_range
            Report().show_product_range_csv()         # option1 from csv
            # Report().show_prod_range_as_table()     # option2 from dicionary
        if self.type == 'inventory':
            today = SystemState().today
            not_sold = [x for x in self.inventory_list if x.sold is False]
            # check if already bought on reportdate
            was_in = [x for x in not_sold if x.buy_date <= self.report_date]
            if self.report_date != today:
                print("Today is ", today)
                print("Report date is", self.report_date)
                print("Only today's stock report is exported to inventory.csv")
            in_stock = [x for x in was_in if x.expired is False]
            stock_report = []
            if in_stock != []:
                for prod in in_stock:
                    counter = 0
                    for x in in_stock:
                        if x.name == prod.name:
                            counter += 1
                    dict_to_append = {'Product name': prod.name,
                                      'Count': f'1 of {counter}',
                                      'Buy price': prod.buy_price,
                                      'Expiration date': prod.exp_date}
                    stock_report.append(dict_to_append)
            report_object = stock_report
            fields = ['Product name', 'Count', 'Buy price', 'Expiration date']
            # avoid export of non-actual inventory reports
            if self.report_date == today:
                Report().export_rep_to_csv(fields, 'inventory.csv',
                                           stock_report)
            Report().show_inventory_csv()
        return report_object


class Time_range_report():
    """Input is 1. type from <'revenue', 'profit'>, 2. an inventory list and
       3. date string specifying the required reporting period (or single day).
          Format is <'now', 'yesterday, 'date YYYY-MM', 'date YYYY-MM-DD'>."""
    def __init__(self, type, inventory_list, date_str):
        self.type = type
        self.inventory_list = inventory_list
        self.date_str = date_str
        self.rep_string = ''

    def get_report(self):
        """Selects proper function for making up the required report."""
        if self.type == 'revenue':
            report = self.make_up_revenue_report()
        else:
            if self.type == 'profit':
                report = self.make_up_profit_report()
        if self.type == 'honest_profit':
            report = self.make_up_true_profit_report()
        print(report)           # show report on screen
        return report

    def get_days_from_periode(self, date_request):
        """Provides a range of dates in a requested year-month-period."""
        cld = calendar.Calendar()
        year = int(date_request[0:4])
        month = int(date_request[5:7])
        datelist_to_filter = cld.itermonthdates(year, month)
        # filter outside month; itermonthdates adds dates to complete weeks
        datelist = [d for d in datelist_to_filter if d.month == month]
        return datelist

    def report_time_and_result_template(self, date_request):
        """Makes a report string template, depending of input datestring. Input format
           isone of <'now', 'yesterday, 'date YYYY-MM', 'date YYYY-MM-DD'>."""
        rep_type = self.type
        if date_request == 'now':
            self.rep_string = str(f"Today's {rep_type} so far: ")
        if date_request == 'yesterday':
            self.rep_string = str(f"Yesterday's {rep_type} was: ")
        if date_request[0:4] == 'date':
            if len(date_request) == 12:         # YYYY-MM format
                self.year = date_request[5:9]
                if len(date_request) > 10:
                    self.month = date_request[10:]
                datetime_object = datetime.datetime.strptime(self.month, "%m")
                full_month_name = datetime_object.strftime("%B")
                msg = str(f"In {full_month_name} {self.year} {rep_type} is: ")
                self.rep_string = msg
            else:                               # YYYY-MM-DD format
                if len(date_request) == 15:
                    date = SystemState().proper_date(date_request[5:])
                    self.rep_string = str(f'On {date} the {rep_type} is: ')
        return self.rep_string

    def date_req_to_report_period(self, date_request):
        """Transforms string-date-request in (list of) datetime.date dates.
           Expects either a time-range 'date YYYY-MM',
           or a specific day: 'now', 'yesterday', 'date YYYY-MM-DD'.
           """
        try:
            now = SystemState().today
            if date_request == 'now':
                report_period = now
            if date_request == 'yesterday':
                report_period = now + datetime.timedelta(-1)
            if date_request[0:4] == 'date':
                if len(date_request) == 12:         # YYYY-MM format
                    d_obj = self.get_days_from_periode(date_request[5:])
                    date_list = [d for d in d_obj]
                    report_period = date_list
                else:                               # YYYY-MM-DD format
                    if len(date_request) == 15:
                        prop_date = SystemState().proper_date(date_request[5:])
                        report_period = prop_date
            return report_period
        except UnboundLocalError:
            print("Please provide a proper date for the report.")

    def get_revenue(self):
        """Returns sum_total of sell_prices within requested period."""
        report_period = self.date_req_to_report_period(self.date_str)
        table = self.inventory_list
        if type(report_period) != list:
            prices = [x for x in table if (x.sell_price
                                           and x.sell_date == report_period)]
        else:
            prices = [x for x in table if (x.sell_price
                                           and x.sell_date in report_period)]
        revenue_raw = sum([float(x.sell_price)
                           for x in prices if float(x.sell_price)])
        revenue = '{:.2f}'.format(revenue_raw)
        return revenue

    def get_profit(self):
        """Returns sum_total of sell_prices when sell_dates in timeperiod."""
        report_period = self.date_req_to_report_period(self.date_str)
        table = self.inventory_list
        total_revenue = float(self.get_revenue())
        if type(report_period) != list:
            sells = [x for x in table if (x.buy_price
                                          and x.sell_date == report_period)]
            total_costs = sum([float(x.buy_price)
                               for x in sells if float(x.buy_price)])
        else:
            sells = [x for x in table if (x.buy_price
                                          and x.sell_date in report_period)]
            total_costs = sum([float(x.buy_price)
                               for x in sells if float(x.buy_price)])
        profit_raw = total_revenue - total_costs
        profit = '{:.2f}'.format(profit_raw)
        return profit

    def get_true_profit(self):
        """Returns sum_total of true_profit when sell_dates in timeperiod.
           True profit is based on 'true_costs' price, that takes into account
           the footprint factor (weight), between 1-10. Footprint factor is
           specified in product_range.csv for easy maintenance.
           True cost = cost * (1 + foot_print_factor/10).
           Example: cost = 2.00; footprint_fact = 4 -->
                    true_cost = 2.00 * (1+0.4) = 2.8 ."""
        report_period = self.date_req_to_report_period(self.date_str)
        table = self.inventory_list
        total_revenue = float(self.get_revenue())
        if type(report_period) != list:
            sells = [x for x in table if (x.buy_price
                                          and x.sell_date == report_period)]
            # total_costs = sum([float(x.buy_price)
            #                    for x in sells if float(x.buy_price)])
            # print('total_costs', total_costs)
            true_costs = sum([float(x.buy_price)*(1+(float(x.footpr_fct)/10))
                              for x in sells
                              if
                              float(x.buy_price)*(1+(float(x.footpr_fct)/10))])
            # print('true_costs', true_costs)
        else:
            sells = [x for x in table if (x.buy_price
                                          and x.sell_date in report_period)]
            # total_costs = sum([float(x.buy_price)
            #                    for x in sells if float(x.buy_price)])
            # print('total_costs', total_costs)
            true_costs = sum([float(x.buy_price)*(1+(float(x.footpr_fct)/10))
                              for x in sells
                              if
                              float(x.buy_price)*(1+(float(x.footpr_fct)/10))])
            # print('true_costs', true_costs)
        true_profit_raw = total_revenue - true_costs
        true_profit = '{:.2f}'.format(true_profit_raw)
        return true_profit

    def make_up_revenue_report(self):
        """Connects report template with report string for feedback."""
        date_request = self.date_str
        template_string = self.report_time_and_result_template(date_request)
        revenue = self.get_revenue()
        report_string = str(f'{template_string}{revenue}')
        return report_string

    def make_up_profit_report(self):
        """Connects report template with report string for feedback."""
        date_request = self.date_str
        template_string = self.report_time_and_result_template(date_request)
        profit = self.get_profit()
        report_string = str(f'{template_string}{profit}')
        return report_string

    def make_up_true_profit_report(self):
        """Connects report template with report string for feedback."""
        date_request = self.date_str
        template_string = self.report_time_and_result_template(date_request)
        true_profit = self.get_true_profit()
        report_string = str(f'{template_string}{true_profit}')
        return report_string
