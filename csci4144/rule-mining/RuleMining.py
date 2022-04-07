import csv
from faulthandler import cancel_dump_traceback_later
import itertools


def read_data(file_name):
    header = ""
    file_data = []
    with open(file_name, 'r', encoding="utf-8") as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        header = next(data)
        for row in data:
            file_data.append(row)
    return file_data


def write_data(file_name, data):
    with open(file_name, 'a', encoding="utf-8") as text_file:
        for line in data:
            text_file.write(line)
    return


def first(data):
    '''
    Generates the frequency set
    '''
    dictionary = dict()

    for row in data:
        for item in row:
            if item not in dictionary:
                dictionary[item] = 1
            else:
                dictionary[item] += 1

    dictionary2 = dict()

    for k, v in dictionary.items():
        if v >= round(float(min_sup) * len(data)):
            dictionary2[k] = v

    return dictionary2


def check_item(item_set, transaction):
    '''
    Checks whether each item in item_set is present in transaction
    '''
    contained = False

    for item in item_set:
        if item in transaction:
            contained = True
        else:
            contained = False
            break

    return contained


def item_sets(candidateList, data):
    '''
    Generates frequent item sets given a candidate list and also prunes 
    '''
    candidate_Set = set(candidateList)

    freq = dict()

    for item in candidate_Set:
        for transaction in data:
            check = check_item(item, transaction)
            if check:
                if item in freq:
                    freq[item] += 1
                else:
                    freq[item] = 1

    prune = dict()

    for k, v in freq.items():
        if v >= round(float(min_sup) * len(data)):
            prune[k] = v

    return prune


def freq_sets(data):
    ''' 
    Generates frequent item sets, association rules and confidence values and writes them to a file
    '''
    candidateDict = dict(first(data))
    g_dict = candidateDict
    k = 2

    while len(candidateDict) != 0:
        c = []
        for i in candidateDict:
            for j in candidateDict:
                if k == 2:
                    if j > i:
                        c.append((i, j))
                else:
                    if (j[-1] != i[-1]) and (i[:-1] == j[:-1]):
                        if j[-1] < i[-1]:
                            c.append((j, i[-1]))
                        else:
                            c.append((i, j[-1]))

        candidateDict = item_sets(c, data)
        g_dict.update(candidateDict)
        k += 1

    out_buffer = []
    out_buffer.append('-' * 70 + '\n')
    out_buffer.append('1. User Input:' + '\n')
    out_buffer.append('\n')
    out_buffer.append('Support=' + str(min_sup) + '\n')
    out_buffer.append('Confidence=' + str(min_conf) + '\n')
    out_buffer.append('\n')
    out_buffer.append('2. Rules:' + '\n')
    out_buffer.append('\n')
    write_data('Rules.txt', out_buffer)
    out_buffer.clear()

    rule_no = 1
    for k, v in g_dict.items():
        if type(k) == tuple:

            for j in range(1, len(k)):
                combinations = list(itertools.combinations(k, j))
                for combination in combinations:
                    if len(combination) != 1:
                        if combination in g_dict:
                            c = v / g_dict[combination]
                    else:
                        if combination[0] in g_dict:
                            c = v / g_dict[combination[0]]

                    if c >= min_conf:
                        key_list = list(k)
                        for r in list(combination):
                            key_list.remove(r)

                        new_list = list(combination)
                        for key in list(key_list):
                            new_list.append(key)
                        sup = getSupport(new_list, data)

                        if sup >= min_sup:
                            out_buffer.append('Rule#' + str(rule_no) + ': ' + '{' + getOutputString(list(combination)) + '}'
                                              + '=>' + '{' + getOutputString(list(key_list)) + '}' + '\n')
                            out_buffer.append('(Support=' + str(round(sup, 2)) + ', ' +
                                              'Confidence=' + str(round(c, 2)) + ')' + '\n')
                            out_buffer.append('\n')
                            write_data('Rules.txt', out_buffer)
                            out_buffer.clear()
                            rule_no += 1
                        else:
                            continue


def getSupport(items, data):
    '''
    Returns the support of a given rule
    '''
    count = 0
    for row in data:
        if set(items).issubset(set(row)):
            count += 1

    return count / len(data)


def getOutputString(list_combination):
    '''
    Returns a formatted string of the rule to be written to file
    '''
    out = ''

    for i in range(0, len(list_combination)):
        item = list_combination[i]

        if item == 'sunny' or item == 'overcast' or item == 'rain':
            out += 'Outlook=' + item
        elif item == 'hot' or item == 'mild' or item == 'cool':
            out += 'Temperature=' + item
        elif item == 'high' or item == 'normal':
            out += 'Humidity=' + item
        elif item == 'TRUE' or item == 'FALSE':
            out += 'Windy=' + item
        elif item == 'P' or item == 'N':
            out += 'PlayTennis=' + item

        if i != len(list_combination) - 1:
            out += ','
    return out


def main():

    data = read_data('Play_Tennis_Data_Set.csv')

    global min_sup, min_conf, g_dict
    min_sup = float(input("Enter minimum support value: "))
    min_conf = float(input("Enter minimum confidence value: "))

    freq_sets(data)


if __name__ == "__main__":
    main()
