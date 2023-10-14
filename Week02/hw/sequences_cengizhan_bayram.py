my_list = [1, 2, 3, 4, 5, 6, 6, 5, 6]
my_tuple = ( 7, 8, 8, 9)
my_set = {4, 5, 6, 7, 8, 9, 10}
my_dict = {"name": "Cengizhan ", "surname": "BAYRAM", "age": 22}

def remove_duplicates(my_list):
    return list(set(my_list))


def list_counts(my_list):
    count_dict = {}
    for element in my_list:
        if element in count_dict:
            count_dict[element] += 1
        else:
            count_dict[element] = 1
    return count_dict


def reverse_dict(my_dict):
    rev_dictionary = dict()
    for key, value in my_dict.items():
        rev_dictionary[value] = key
    return(rev_dictionary)
