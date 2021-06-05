import argparse
# from class_product import Product
from class_product import SystemState
from class_product import ShopAdmin
# from class_product import Product
from class_reports import Report
from class_reports import Time_range_report
from class_reports import Fixed_date_report

system_state = SystemState()
shop = ShopAdmin()
shop.inventory_list = system_state.instantiate_products([])
report = Report()

"""
cli_tool.py :
- initialises main classes
- handles command-line-input
"""

# gets product_choices from file for easy maintenance of product_range
product_range = system_state.get_import_data('product_range.csv', [])
product_choices = [p.get('prod_name') for p in product_range]


# Functions to get from user commands to function calls
def report_call(args):
    arg_dict = vars(args)
    rep_type = arg_dict['report_type']
    inv_list = shop.inventory_list
    if rep_type in ['inventory', 'product_range']:
        if arg_dict['now'] is True:
            Fixed_date_report(rep_type, inv_list, 'now').get_fd_report()
        elif arg_dict['yesterday'] is True:
            Fixed_date_report(rep_type, inv_list, 'yesterday').get_fd_report()
        elif arg_dict['date'] is None:
            Fixed_date_report(rep_type, inv_list, 'now').get_fd_report()
        else:
            date_str = f"date {arg_dict['date'][0]}"
            Fixed_date_report(rep_type, inv_list, date_str).get_fd_report()
    else:
        if arg_dict['report_type'] in ['revenue', 'profit', 'honest_profit']:
            if arg_dict['now'] is True:
                Time_range_report(rep_type, inv_list, 'now').get_report()
            elif arg_dict['yesterday'] is True:
                Time_range_report(rep_type, inv_list,
                                  'yesterday').get_report()
            else:
                date_str = f"date {arg_dict['date'][0]}"
                Time_range_report(rep_type, inv_list, date_str).get_report()
    print('\n')


def buy_call(args):
    arg_dict = vars(args)
    # print("Buying was not ok yet. But args = ", args)
    exp_date_str = arg_dict['expiration_date']
    shop.buy(arg_dict['product_name'], exp_date_str, arg_dict['price'])
    print('OK\n')


def sell_call(args):
    arg_dict = vars(args)
    # print("Selling is not ok yet. But args = ", args)
    shop.sell(arg_dict['product_name'], arg_dict['price'])
    print('OK\n')


def advance_time_call(args):
    arg_dict = vars(args)
    # no_of_days = arg_dict['no_of_days']
    # shop.advance_time(no_of_days)
    shop.advance_time(arg_dict['no_of_days'])
    print('OK\n')


parser = argparse.ArgumentParser(add_help=False)
parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                    help="""The supermarket entry shows a complete instruction
                            of all the commands.
                            See [-H] for dedicated help.""")
parser.add_argument('-H', action='help',
                    help="""Type [-H] after
                            positional argument to get more specific help.""")
subparsers = parser.add_subparsers()

# create subparser for the "'Report" methods
parser_report = subparsers.add_parser('report')
parser_report.add_argument('report_type', action='store',
                           choices=['inventory', 'product_range', 'revenue',
                                    'profit', 'honest_profit'])
parser_report.add_argument('-H', action='help',
                           help="""Report types are:
                                   [inventory], [product_range], [revenue],
                                   [profit] or [honest_profit].
                                   Time-options are:
                                   [--now], [--yesterday], [--date].""")
time_options = parser_report.add_mutually_exclusive_group()
time_options.add_argument('--yesterday', action='store_true')
time_options.add_argument('--now', action='store_true')
time_options.add_argument('--date', action='store', nargs=1,
                          help="""Specify a time-range of a month
                                  [--date YYYY-MM]. Or specify a specific date
                                  as [--date YYYY-MM-DD].""")
parser_report.set_defaults(func=report_call)

# create subparsers for "ShopAdmin" methods: buy and sell
parser_buy = subparsers.add_parser('buy')
parser_buy.add_argument('-H', action='help',
                        help="""NB: Note that the order of the arguments for buy
                                differs from Superpy assignment!""")
parser_buy.add_argument('--product-name', action='store',
                        choices=product_choices)
parser_buy.add_argument('--expiration-date', action='store')
parser_buy.add_argument('--price', action='store')
parser_buy.set_defaults(func=buy_call)

parser_sell = subparsers.add_parser('sell')
parser_sell.add_argument('--product-name', action='store',
                         choices=product_choices)
parser_sell.add_argument('--price', action='store')
parser_sell.set_defaults(func=sell_call)

parser_adv_t = subparsers.add_parser('advance-time')
parser_adv_t.add_argument('-H', action='help',
                          help="""NB: Note design decision that advance-time
                                  is a positional argument (and NOT an
                                  optional argument as specified in
                                  Superpy assignment).
                                  Command will prompt with the new date that is
                                  set and exported to 'superpy_date.txt.""")
parser_adv_t.add_argument('no_of_days', action='store', type=int,
                          help="""[=n] or [-n] = No-of-days to advance or reverse
                                  ADVANCE will invoke expiry of products.
                                  REVERSE will undo expiries and
                                  selling actions.""")
parser_adv_t.set_defaults(func=advance_time_call)


# # INPUT MODE - VERSION 1. Single command line parsing
# ACTIVATED in this file
def single_command_line_parser():
    """Parses single line commands and calls function connected to namespace
       This mode is activated in file cli_single_line.py"""
    args = parser.parse_args()
    args.func(args)
# # END INPUT MODE VERSION 1


# INPUT MODE - VERSION 2
# DE-ACTIVATED in this file
# def user_input_loop():
#     """Keeps reading from stdin and quits only if the word 'exit' is there.
#        This loop, by default does not terminate, since stdin is open.
#        This mode is activated in this file cli_tool.py"""
#     stdin_fileno = sys.stdin
#     for line in stdin_fileno:
#         # Remove trailing newline characters using strip()
#         if 'exit' == line.strip():
#             print('Found exit. Terminating the program.')
#             exit(0)
#         else:
#             args = parser.parse_args(line.split())
#             # print("During debugging contents of args are: ", args)
#             args.func(args)
# END INPUT MODE - VERSION 2


# START SHOPPING
print('For help, type [-H] or look at the manual. Type [exit] to quit.\n')

# single_command_line_parser()          # cli_single_line mode
# user_input_loop()                   # cli_tool mode
