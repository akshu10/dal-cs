import itertools
import csv
# Reads data from the given csv file


def read_data(file_name):
    header = ""
    file_data = []
    with open(file_name, 'r', encoding="utf-8") as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        header = next(data)
        for row in data:
            file_data.append(row)
    return (file_data, header)

# Writes the data to csv file


def write_data(file_name, data, header):
    with open(file_name, 'w', newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(header)
        for row in data:
            writer.writerow(row)
    return

# Sorts the csv file by country, time_year, time_quarter, car_manufacturer


def sort_csv_data():
    print("Performing First Sort")
    file_data = read_data('Car_Sales_Data_Set.csv')
    header = file_data[1]
    sorted_data_by_country = sorted(file_data[0], key=lambda x: x[0])
    write_data('Car_Sales_Data_Set_First_Sorting.csv',
               sorted_data_by_country, header)

    print("Performing Second Sort")
    file_data = read_data('Car_Sales_Data_Set_First_Sorting.csv')
    header = file_data[1]
    sorted_data_by_time_year = sorted(file_data[0], key=lambda x: x[1])
    write_data('Car_Sales_Data_Set_Second_Sorting.csv',
               sorted_data_by_time_year, header)

    print("Performing Third Sort")
    file_data = read_data('Car_Sales_Data_Set_Second_Sorting.csv')
    header = file_data[1]
    sorted_data_by_time_quarter = sorted(file_data[0], key=lambda x: x[2])
    write_data('Car_Sales_Data_Set_Third_Sorting.csv',
               sorted_data_by_time_quarter, header)

    print("Sorting Complete")


'''
Displays the aggregate sales
Completed
'''


def aggregate_sales():
    file_data = read_data('Car_Sales_Data_Set.csv')

    total_sales = 0
    for row in file_data[0]:
        total_sales += int(row[4])

    print(f"Total Sales Units: {total_sales}")

    print('\n')


'''
Queries the csv file based on the country
Completed
'''


def country_query():
    file_data = read_data('Car_Sales_Data_Set_First_Sorting.csv')

    country_dict = {}
    for key, value in itertools.groupby(file_data[0], key=lambda x: x[0]):
        country_dict[key] = sum(int(row[4]) for row in value)

    print('\n')
    print('-' * 40)
    print(f"{'Country':^15} {'Sales Units':^16}")
    print('-' * 40)

    for key, value in country_dict.items():
        print(f"{key:^15} {value:^15}")

    print('\n')


'''
Queries the csv file based on the time_year
Completed
'''


def time_year_query():
    file_data = read_data('Car_Sales_Data_Set_Second_Sorting.csv')
    time_year_dict = {}

    for key, value in itertools.groupby(file_data[0], key=lambda x: x[1]):
        time_year_dict[key] = sum(int(row[4]) for row in value)

    print('\n')
    print('-' * 40)
    print(f"{'Time Year':^15} {'Sales Units':^16}")
    print('-' * 40)
    for key, value in time_year_dict.items():
        print(f"{key:^15} {value:^15}")

    print('\n')


'''
Queries the csv file based on the car_manufacturer
Completed
'''


def car_manufacturer_query():
    file_data = read_data('Car_Sales_Data_Set.csv')

    sort_by_car_manufacturer = sorted(file_data[0], key=lambda x: x[3])
    manufacturer_dict = {}

    for key, value in itertools.groupby(sort_by_car_manufacturer, key=lambda x: x[3]):
        manufacturer_dict[key] = sum(int(row[4]) for row in value)

    print('\n')
    print('-' * 45)
    print(f"{'Car Manufacturer':>20} {'Sales Units':>20}")
    print('-' * 45)
    for key, value in manufacturer_dict.items():
        print(f"{key:>15} {value:>20}")

    print('\n')


'''
Queries the csv file based on the time_quarter - time_year
completed
'''


def time_quarter_time_year_query():
    file_data = read_data('Car_Sales_Data_Set_Third_Sorting.csv')
    time_year_time_quarter_dict = {}

    for key, value in itertools.groupby(file_data[0], key=lambda x: (x[1], x[2])):
        time_year_time_quarter_dict[key] = sum(int(row[4]) for row in value)

    print('\n')
    print('-' * 53)
    print(f"{'Time Year-Time Quarter':>25} {'Sales Units':>21}")
    print('-' * 53)

    for key, value in time_year_time_quarter_dict.items():
        time_year_time_quarter = key[0] + "-" + key[1]
        print(f"{time_year_time_quarter:>17} {value:>25}")

    print('\n')


'''
Queries the csv file based on the country and time_year
Completed(2D)
'''


def country_time_year_query():
    file_data = read_data('Car_Sales_Data_Set_First_Sorting.csv')
    country_time_year_dict = {}

    for key, value in itertools.groupby(file_data[0], key=lambda x: (x[0], x[1])):
        country_time_year_dict[key] = sum(int(row[4]) for row in value)

    for key, value in itertools.groupby(country_time_year_dict.items(), key=lambda x: (x[0][0])):
        print('\n')
        print('-' * 40)
        print(f"\033[1m{'Country':>16} - {key}\033[0m")
        print('-' * 40)
        print(f"{'Time Year':^15} {'Sales Units':^23}")
        print('-' * 40)

        for row in value:
            print(f"{row[0][1]:^15} {row[1]:^23}")

    print('\n')


'''
Queries the csv file based on the time_quarter - time_year and country
Completed(2D)
'''


def country_time_quarter_time_year_query():
    file_data = read_data('Car_Sales_Data_Set_First_Sorting.csv')
    country_time_quarter_time_year_dict = {}

    for key, value in itertools.groupby(file_data[0], key=lambda x: (x[0], x[1], x[2])):
        country_time_quarter_time_year_dict[key] = sum(
            int(row[4]) for row in value)

    transformed_list = list(country_time_quarter_time_year_dict.items())

    for k, v in itertools.groupby(transformed_list, key=lambda x: (x[0][0])):
        print('\n')
        print('-' * 70)
        print(f"\033[1m{'Country':>33} - {k}\033[0m")
        print('-' * 70)

        temp_list = list(v)
        sort_list = sorted(temp_list, key=lambda x: (x[0][1], x[0][2]))

        splice_2017 = sort_list[:len(sort_list)//2]

        splice_2018 = sort_list[len(sort_list)//2:]

        print(
            f"\x1B[3m{'Time_Year':>15} - {sort_list[0][0][1]} {'Time_Year':>31} - {sort_list[len(sort_list)//2][0][1]}\x1B[0m")
        print('-' * 70)
        print(
            f"{'Time_Quarter':>15} {'Sales Units':>14}{'Time_Quarter':>25}{'Sales Units':>14}")
        print('-' * 70)

        for i in range(len(sort_list)//2):
            print(
                f"{splice_2017[i][0][2]:>8} {splice_2017[i][1]:>17} {splice_2018[i][0][2]:>21} {splice_2018[i][1]:>16}")

    print('\n')


'''
Queries the csv file based on the country and car_manufacturer
Completed(2D)
'''


def country_car_manufacturer_query():
    file_data = read_data('Car_Sales_Data_Set_First_Sorting.csv')
    country_car_manufacturer_dict = {}

    sort_by_car_manufacturer = sorted(file_data[0], key=lambda x: (x[3]))

    for key, value in itertools.groupby(sort_by_car_manufacturer, key=lambda x: (x[0], x[3])):
        country_car_manufacturer_dict[key] = sum(int(row[4]) for row in value)

    sorted_by_country = sorted(
        country_car_manufacturer_dict.items(), key=lambda x: (x[0][0]))

    for key, value in itertools.groupby(sorted_by_country, key=lambda x: (x[0][0])):
        print('\n')
        print('-' * 40)
        print(f"\033[1m{'Country':>17} - {key}\033[0m")
        print('-' * 40)
        print(f"{'Car Manufacturer':^15} {'Sales Units':^25}")
        print('-' * 40)

        for row in value:
            print(f"{row[0][1]:^15} {row[1]:^25}")

    print('\n')


'''
Queries the csv file based on the time_year and car_manufacturer
Completed(2D)
'''


def time_year_car_manufacturer_query():
    file_data = read_data('Car_Sales_Data_Set_Second_Sorting.csv')
    time_year_car_manufacturer_dict = {}

    sort_by_car_manufacturer = sorted(file_data[0], key=lambda x: (x[3]))

    for key, value in itertools.groupby(sort_by_car_manufacturer, key=lambda x: (x[1], x[3])):
        time_year_car_manufacturer_dict[key] = sum(
            int(row[4]) for row in value)

    sorted_by_time_year = sorted(
        time_year_car_manufacturer_dict.items(), key=lambda x: (x[0][0]))

    for key, value in itertools.groupby(sorted_by_time_year, key=lambda x: (x[0][0])):
        print('\n')
        print('-' * 40)
        print(f"\033[1m{'Time_Year':>20} - {key}\033[0m")
        print('-' * 40)
        print(f"{'Car Manufacturer':^15} {'Sales Units':^25}")
        print('-' * 40)

        for row in value:
            print(f"{row[0][1]:^15} {row[1]:^25}")

    print('\n')


'''
Queries the csv file based on the time_quarter, car_manufacturer, and time_year
Completed
'''


def time_quarter_time_year_car_manufacturer_query():
    file_data = read_data('Car_Sales_Data_Set.csv')
    time_quarter_time_year_car_manufacturer_dict = {}

    sort_data = sorted(file_data[0], key=lambda x: (x[1], x[2], x[3]))

    for key, value in itertools.groupby(sort_data, key=lambda x: (x[1], x[2], x[3])):
        time_quarter_time_year_car_manufacturer_dict[key] = sum(
            int(row[4]) for row in value)

    sort_by_car_manufacturer = sorted(
        time_quarter_time_year_car_manufacturer_dict.items(), key=lambda x: (x[0][2]))

    for key, value in itertools.groupby(sort_by_car_manufacturer, key=lambda x: (x[0][2])):
        print('\n')
        print('-' * 50)
        print(f"\033[1m{'Car Manufacturer':>27} - {key}\033[0m")
        for k, v in itertools.groupby(value, key=lambda x: (x[0][0])):
            print('-' * 50)
            print(f"\x1B[3m{'Time_Year':>24} - {k}\x1B[0m")
            print('-' * 50)
            print(f"{'Time_Quarter':^24}{'Sales Units':^24}")
            print('-' * 50)

            for row in v:
                print(f"{row[0][1]:^24}{row[1]:^24}")

    print('\n')


'''
Queries the csv file based on country, time_year, car_manufacturer
Completed(3D)
'''


def country_time_year_car_manufacturer_query():
    file_data = read_data('Car_Sales_Data_Set_First_Sorting.csv')
    country_time_year_car_manufacturer_dict = {}

    sort_by_car_manufacturer = sorted(
        file_data[0], key=lambda x: (x[3], x[0], x[1]))

    for key, value in itertools.groupby(sort_by_car_manufacturer, key=lambda x: (x[0], x[1], x[3])):
        country_time_year_car_manufacturer_dict[key] = sum(
            int(row[4]) for row in value)

    sort_dictionary_by_country_list = sorted(
        country_time_year_car_manufacturer_dict.items(), key=lambda x: (x[0][0]))

    for key, value in itertools.groupby(sort_dictionary_by_country_list, key=lambda x: (x[0][0])):
        print('\n')
        print('-' * 60)
        print(f"\033[1m {key:^55}\033[0m")

        for k, v in itertools.groupby(value, key=lambda x: (x[0][2])):
            print('-' * 60)
            print(f"\x1B[3m{k:^55}\x1B[0m")
            print('-' * 60)
            print(f"{'Time_Year':^27} {'Sales Units':^27}")
            print('-' * 60)
            for row in v:
                print(f"{row[0][1]:^27} {row[1]:^27}")

    print('\n')


'''
Queries the csv file based on the time_quarter and car_manufacturer
Completed
'''


def country_time_quarter_time_year_car_manufacturer_query():
    file_data = read_data('Car_Sales_Data_Set_Second_Sorting.csv')
    country_time_quarter_time_year_car_manufacturer_dict = {}

    sort_by_car_manufacturer_time_quarter = sorted(
        file_data[0], key=lambda x: (x[3], x[2]))

    for key, value in itertools.groupby(sort_by_car_manufacturer_time_quarter, key=lambda x: (x[0], x[1], x[2], x[3])):
        country_time_quarter_time_year_car_manufacturer_dict[key] = sum(
            int(row[4]) for row in value)

    sort_dictionary_by_country_list = sorted(
        country_time_quarter_time_year_car_manufacturer_dict.items(), key=lambda x: (x[0][0]))

    sorted_dictionary_by_country = dict(sort_dictionary_by_country_list)

    for key, value in itertools.groupby(sorted_dictionary_by_country.items(), key=lambda x: (x[0][0])):
        print('\n\n')
        print('-' * 75)
        print(f"\033[92m{key:>43}\033[0m")
        for k, v in itertools.groupby(value, key=lambda x: (x[0][3])):
            print('-' * 75)
            print(f"\033[91m{k:>41}\033[0m")

            temp = list(v)
            sort_by_year = sorted(temp, key=lambda x: (x[0][1]))
            splice_2017 = sort_by_year[:4]
            splice_2018 = sort_by_year[4:]

            print('-' * 75)
            print(
                f"\033[93m{'Time_Year':>17} - {sort_by_year[0][0][1]} {'Time_Year':>33} - {sort_by_year[4][0][1]}\033[0m")
            print('-' * 75)
            print(
                f"\033[95m{'Time_Quarter':>15}{'Sales Units':>19} {'Time_Quarter':>21}{'Sales Units':>19}\033[0m")
            print('-' * 75)
            for i in range(len(sort_by_year)//2):
                print(
                    f"\033[36m{splice_2017[i][0][2]:>10}{splice_2017[i][1]:>19}{splice_2018[i][0][2]:>21}{splice_2018[i][1]:>20}\033[0m")

            print('\n')


'''
Print ETL-OLAP query menu
'''


def print_menu():

    print("\n")
    print(" 1.  ()")
    print(" 2.  (Country)")
    print(" 3.  (Time_Year)")
    print(" 4.  (Time_Quarter - Time_Year)")
    print(" 5.  (Car_Manufacturer)")
    print(" 6.  (Country, Time_Year)")
    print(" 7.  (Country, Time_Quarter - Time_Year)")
    print(" 8.  (Country, Car_Manufacturer)")
    print(" 9.  (Time_Year, Car_Manufacturer)")
    print(" 10. (Time_Quarter - Time_Year, Car_Manufacturer)")
    print(" 11. (Country, Time_Year, Car_Manufacturer)")
    print(" 12. (Country, Time_Quarter - Time_Year, Car_Manufacturer)")

    user_input = input(
        "\n\nEnter a number in the range 1-12 to perform a query: ")

    if user_input.isdigit():
        return int(user_input)


'''
Handles the user input and calls the appropriate function
'''


def handle_query(query):
    if query == 1:
        aggregate_sales()
    elif query == 2:
        country_query()
    elif query == 3:
        time_year_query()
    elif query == 4:
        time_quarter_time_year_query()
    elif query == 5:
        car_manufacturer_query()
    elif query == 6:
        country_time_year_query()
    elif query == 7:
        country_time_quarter_time_year_query()
    elif query == 8:
        country_car_manufacturer_query()
    elif query == 9:
        time_year_car_manufacturer_query()
    elif query == 10:
        time_quarter_time_year_car_manufacturer_query()
    elif query == 11:
        country_time_year_car_manufacturer_query()
    elif query == 12:
        country_time_quarter_time_year_car_manufacturer_query()
    else:
        print("Invalid input. Please try again.")


def main():
    sort_csv_data()
    user_input = print_menu()

    handle_query(user_input)


if __name__ == '__main__':
    main()
