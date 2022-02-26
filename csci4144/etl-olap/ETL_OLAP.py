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
    print('-' * 40)
    print(f"{'Car Manufacturer':^15} {'Sales Units':^16}")
    print('-' * 40)
    for key, value in manufacturer_dict.items():
        print(f"{key:^15} {value:^15}")


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
    print('-' * 40)
    print(f"{'Time Year-Time Quarter':^15} {'Sales Units':^16}")
    print('-' * 40)

    for key, value in time_year_time_quarter_dict.items():
        time_year_time_quarter = key[0] + "-" + key[1]
        print(f"{time_year_time_quarter:^21} {value:^17}")


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
        print(f"{key:^35}")
        print('-' * 40)
        print(f"{'Time Year':^15} {'Sales Units':^16}")
        print('-' * 40)

        for row in value:
            print(f"{row[0][1]:^15} {row[1]:^15}")


'''
Queries the csv file based on the time_quarter - time_year and country
Completed(2D)
'''


def country_time_quarter_time_year_query():
    file_data = read_data('Car_Sales_Data_Set_Third_Sorting.csv')
    country_time_quarter_time_year_dict = {}

    for key, value in itertools.groupby(file_data[0], key=lambda x: (x[0], x[1], x[2])):
        country_time_quarter_time_year_dict[key] = sum(
            int(row[4]) for row in value)

    sort_by_country = sorted(
        country_time_quarter_time_year_dict.items(), key=lambda x: x[0][0])

    for key, value in itertools.groupby(sort_by_country, key=lambda x: (x[0][0])):
        print('\n')
        print('-' * 40)
        print(f"{key:^35}")
        print('-' * 40)
        print(f"{'Time Year-Time Quarter':^15} {'Sales Units':^16}")
        print('-' * 40)

        for row in value:
            time_year_time_quarter = row[0][1] + "-" + row[0][2]
            print(f"{time_year_time_quarter:^21} {row[1]:^17}")


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

    print(sorted_by_country)

    for key, value in itertools.groupby(sorted_by_country, key=lambda x: (x[0][0])):
        print('\n')
        print('-' * 40)
        print(f"{key:^35}")
        print('-' * 40)
        print(f"{'Car Manufacturer':^15} {'Sales Units':^16}")
        print('-' * 40)

        for row in value:
            print(f"{row[0][1]:^15} {row[1]:^17}")


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
        print(f"{key:^35}")
        print('-' * 40)
        print(f"{'Car Manufacturer':^15} {'Sales Units':^16}")
        print('-' * 40)

        for row in value:
            print(f"{row[0][1]:^15} {row[1]:^17}")


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
        print(f"{'Car Manufacturer':>27} - {key}")
        for k, v in itertools.groupby(value, key=lambda x: (x[0][0])):
            print('-' * 50)
            print(f"{'Time_Year':>24} - {k}")
            print('-' * 50)
            print(f"{'Time_Quarter':^24}{'Sales_Units':^24}")
            print('-' * 50)

            for row in v:
                print(f"{row[0][1]:^24}{row[1]:^24}")


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

    print(sort_dictionary_by_country_list)

    for key, value in itertools.groupby(sort_dictionary_by_country_list, key=lambda x: (x[0][0])):
        print('\n')
        print('-' * 60)
        print(f"{key:^55}")

        for k, v in itertools.groupby(value, key=lambda x: (x[0][2])):
            print('-' * 60)
            print(f"{k:^55}")
            print('-' * 60)
            print(f"{'Time_Year':^27} {'Sales Units':^27}")
            print('-' * 60)
            for row in v:
                print(f"{row[0][1]:^27} {row[1]:^27}")


'''
Queries the csv file based on the time_quarter and car_manufacturer
Completed
'''


def country_time_quarter_time_year_car_manufacturer_query():
    file_data = read_data('Car_Sales_Data_Set_Second_Sorting.csv')
    country_time_quarter_time_year_car_manufacturer_dict = {}

    sort_by_car_manufacturer_time_quarter = sorted(
        file_data[0], key=lambda x: (x[2], x[3], x[1]))

    for key, value in itertools.groupby(sort_by_car_manufacturer_time_quarter, key=lambda x: (x[0], x[1], x[2], x[3])):
        country_time_quarter_time_year_car_manufacturer_dict[key] = sum(
            int(row[4]) for row in value)

    sort_dictionary_by_country_list = sorted(
        country_time_quarter_time_year_car_manufacturer_dict.items(), key=lambda x: (x[0][0]))

    sorted_dictionary_by_country = dict(sort_dictionary_by_country_list)

    for key, value in itertools.groupby(sorted_dictionary_by_country.items(), key=lambda x: (x[0][0])):
        print('\n\n')
        print('-' * 60)
        print(f"{key:^55}")
        for k, v in itertools.groupby(value, key=lambda x: (x[0][3])):
            print('\n')
            print('-' * 60)
            print(f"{k:^55}")

            for k1, v1 in itertools.groupby(v, key=lambda x: (x[0][1])):
                print('-' * 60)
                print(f"{'Time_Year': >29}-{k1}")
                print('-' * 60)
                print(f"{'Time_Quarter':^27} {'Sales Units':^27}")
                print('-' * 60)
                for row in v1:
                    print(f"{row[0][2]:^27} {row[1]:^27}")


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
