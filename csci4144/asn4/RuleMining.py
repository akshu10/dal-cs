import csv


def read_data(file_name):
    header = ""
    file_data = []
    with open(file_name, 'r', encoding="utf-8") as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        header = next(data)
        for row in data:
            file_data.append(row)
    return (file_data, header)


def main():

    data, header = read_data('Play_Tennis_Data_Set.csv')
    print(header)
    print(data)

    global min_sup, min_conf
    min_sup = input("Enter minimum support value: ")
    min_conf = input("Enter minimum confidence value: ")


if __name__ == "__main__":
    main()
