import os
import csv


# $$$ building blocks FOR OVERWRITING ONE SINGLE LINE IN CSV
# functies uit SystemState
# was meant for overwriting old line in csv with new line
# now exporting complete list
def get_length_of_file(file_name):
    path_current_file = os.path.dirname(os.path.realpath(__file__))
    file_to_open = f'{path_current_file}/{file_name}'
    file_to_count = open(file_to_open)
    reader = csv.reader(file_to_count)
    no_lines = len(list(reader))
    file_to_count.close()
    return no_lines


def find_line_no(self, dict_of_elem):
    path_current_file = os.path.dirname(os.path.realpath(__file__))
    file_to_open = f'{path_current_file}/product_data.csv'
    # print('file to open is: ', file_to_open)
    with open(file_to_open, newline='') as csvfile:
        # line_num = 1    # starts from 1 ; line 1 is Headerrow
        reader = csv.DictReader(csvfile, delimiter=';')
        for line_num, content in enumerate(reader):
            prod_id = dict_of_elem['id']
            # print(content)
            if content['id'] == prod_id:
                print(content, line_num)
                name = content['prod_name']
                print("Now name is ", name, 'and lineno is', line_num)
                line_no_found = line_num + 2
                break
    return line_no_found
# $$$ building blocks FOR OVERWRITING ONE SINGLE LINE IN CSV

# $$$ ITERATION OVER CLASS INSTANCES
# methods of class Product; to iterate over all instances of the class
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
# $$$ END ITERATION OVER CLASS INSTANCES

# $$$ for class SystemState() ; DATE FUNCTIONS WITH SEPERATE USER-FILE
    # keep this one - with writh writing to user_datefile

    def set_today(self):
        # get path to directory of current file main
        # file "superpy_date.txt" should contain reference_date (rfd)
        path_current_file = os.path.dirname(os.path.realpath(__file__))
        # when user changed date in last session, import user_date
        if os.path.isfile(f'{path_current_file}/superpy_user_date.txt'):
            datefile_to_open = f'{path_current_file}/superpy_user_date.txt'
        # otherwise import default reference_date
        else:
            # check if file superpy_date.txt with default_date exists
            if os.path.isfile(f'{path_current_file}/superpy_date.txt'):
                datefile_to_open = f'{path_current_file}/superpy_date.txt'
        # final check if date_file exists
        if os.path.isfile(datefile_to_open):
            with open(datefile_to_open) as superpy_date:
                date_from_file = superpy_date.readline()
                self.today = self.proper_date(date_from_file)
        # if no such file as superpy_date.txt, notice user + set virtual date
        else:
            virtual_date = '0001-01-01 00:00:00.000000'
            self.today = self.proper_date(virtual_date)
            print("""No valid date could be found.
            Please look at the user guide how to provide a system date.""")
        return self.today

    # keep this one - with writh writing to user_datefile
    def change_today(self, new_date):
        new_today = self.proper_date(new_date)
        self.today = new_today
        print("Do you want to store this new date? y/n")
        keep = input()
        if keep == 'y':
            path_current_file = os.path.dirname(os.path.realpath(__file__))
            datefile_to_open = f'{path_current_file}/superpy_user_date.txt'
            with open(datefile_to_open, 'w') as f:
                new_user_date = str(self.today)
                f.write(new_user_date)
        update = self.set_today()
        return update
# $$$ for class SystemState() ; END DATE FUNCTIONS WITH SEPERATE USER-FILE
