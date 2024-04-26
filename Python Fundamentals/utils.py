
def find_max(my_list):
# my_list = [4, 1, 6, 10, 5, 11]
    largest = my_list[0]
    for item in my_list:
        if item > largest:
            largest = item
    return largest
