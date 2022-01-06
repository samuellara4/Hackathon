# Author: Samuel Lara
# Date: 01/05/2022
# Description: This program will take user input and compare the item searched to a groceries data set and generate a
# shopping list and save as a csv file

import csv

class ItemNotFoundError(Exception):
    pass

def generate_grocery_list():
    # grocery_list = list()
    with open('Groceries_dataset.csv', 'r') as infile:
        data_list = csv.reader(infile)
        grocery_items = list()
        for line in data_list:
            if line[2].lower() == "itemdescription":  # remove the header from the list
                continue

            grocery_items.append(line[2])
        # print(len(grocery_items))
        grocery_set = set(grocery_items)  # remove duplicates - reduces list from 38765 to 167 items
        grocery_items = list(grocery_set)
        # print(len(grocery_items))
    return grocery_items


def get_user_items():
    adding_items = True
    shopping_list = list()
    while adding_items:
        item_to_search = input("What item do you want to add to your shopping list? \n")
        if not valid_item(item_to_search):
            print("Item not found")
        else:




def valid_item(item_to_check):
    """"""



def main():
    g_list = generate_grocery_list()
    print(g_list)


if __name__ == '__main__':
    main()