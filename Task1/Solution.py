import re


# class LogEntry(object):
#     def __init__(self):
#         self

# def delete_empty_lines(list):
#     filtered_list = filter(lambda line: line != "", list)
#     return filtered_list


def print_list(list):
    for i in range(0, len(list)):
        print (list[i])

def print_list_top_n(list, n):
    if (n > len(list)):
        print("N is too big. The list size is: {}".format(len(list)))
        n = len(list)

    print_list(list[:n])


def print_dictionary(**dictionary):
    for key in dictionary:
        print ("{}: {}".format(key, dictionary[key]))


def count_ip_appearance(text):
    myregex = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    ip_list = re.findall(myregex, text)

    dict = {}

    for ip in ip_list:
        if (ip not in dict):
            dict[ip] = 1
        else:
            dict[ip] += 1

    return dict


def count_url_appearance(text):
    my_regex = r'http[s]?://.*.html|http[s]?://.*.php'
    url_list = re.findall(my_regex, text)

    dict = {}

    for url in url_list:
        if (url not in dict):
            dict[url] = 1
        else:
            dict[url] += 1

    return dict


def the_largest_by_val(**dict):
    if (len(dict) == 0):
        return

    max = dict.values()[0]
    max_ip_val = dict.keys()[0]

    for key in dict:
        if (max < dict[key]):
            max = dict[key]
            max_ip_val = key

    return max_ip_val

def sort_by_value(**dictionary):
    sorted_by_value = sorted(dictionary.items(), key=lambda entry: entry[1], reverse=True)
    return sorted_by_value

file = open("logSample", "r")
text = file.read()
file.close()

lines = text.split("\n")
# filtered_lines = delete_empty_lines(lines)

n = 3
ip_count = count_ip_appearance(text)
sorted_by_frequencyIp = sort_by_value(**ip_count)
print ("Top ip {} by frequency(ip:freq): ")
print_list_top_n(sorted_by_frequencyIp, n)

n=2
url_count = count_url_appearance(text)
sorted_by_frequency_url = sort_by_value(**url_count)
print ("\nTop url {} by frequency(url:freq): ")
print_list_top_n(sorted_by_frequency_url, n)
#
# the_most_frequent_ip = the_largest_by_val(**ip_count)
# ip_frequency = ip_count[the_most_frequent_ip]
#
# print ("The most frequent ip is: {} . It was found {} times".format(the_most_frequent_ip, ip_frequency))
# print ("The most frequent up")
