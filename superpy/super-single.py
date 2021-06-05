
# Do not change these lines.
__winc_id__ = 'a2bc36ea784242e4989deb157d527ba0'
__human_name__ = 'superpy'


# Your code below this line.


def main():
    import cli_single_line
    cli_single_line.single_command_line_parser()


if __name__ == '__main__':

    print("""
      HOW TO SWITCH COMMAND MODE ?
      This is the command-line-tool version, with one user-input-loop.
      Switch to single-line-input-mode, by using super2.py.

                              *****
      Welcome in the Supermarket that is very simple and yet offers you a nice
      range of product. Beneath you find a list of commands you can type. They
      are indicated as [string-to-type]; leave out the brackets when used.
      [-h] with this  you can type [-h] to ask for help.
                              *****

                  **** ALL COMMANDS IN BRIEF ****
      exit -->  quit supermarket
      today = simulated 'today' coming from file superpy_date.txt
      SYSTEM ACTION
      * advance-time <n-days>. n may be positive or negative.
        e.g advance-time 2    or   advance-time -3
      REPORTS Command formats
      *  report product_range
      *  report inventory <time-indicator>
            <time_indicator> is one of: --now / --yesterday / --date YYYY-MM-DD
      * report with time-range <report_type> --<time_indicator>
            <report_types> is one of: revenue / profit / honest_profit
            <time_indicator> is one of:
                    --now
                    --yesterday
                    --date YYYY-MM) = month
                    --date YYYY-MM-DD = specific day
            e.g.
         *  report revenue --now
         *  report profit --date 2020-10
         *  report honest_profit --yesterday
      SHOPPING ACTIONS Command formats
       buy --product-name <> --expiration-date YYYY-MM-DD --price <>
       sell --product-name <> --price <>
            e.g.
      *      buy --product-name orange --expiration-date 2022-01-01 --price 1
      *      sell --product-name peas --price 0.8
       """)

    main()
