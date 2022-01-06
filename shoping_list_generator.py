# Author: Samuel Lara
# Date: 01/05/2022
# Description: This program will take user input and compare the item searched to a groceries data set and generate a
# shopping list and save as a csv file

import csv


class ItemNotFoundError(Exception):
    pass


class GroceryList:

    def __init__(self):
        self._g_list = self.generate_grocery_list()

    def get_grocery_list(self):
        return self._g_list

    def generate_grocery_list(self):
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

    def get_user_items(self):
        adding_items = True
        selection_list = list()
        while adding_items:
            item_to_search = input("What item do you want to add to your shopping list? \n")
            for item in self.get_grocery_list():
                if not item_to_search.lower() in item:
                    # print(f"Item not found")
                    continue
                # if not self.valid_item(item_to_search):
                else:
                    selection_list.append(item)

            self.selection_menu(selection_list)
            # print(selection_list)

    def selection_menu(self, list_to_select_from):
        if list_to_select_from == []:
            print("Item Not Found.Try again \n")
            return False
        valid_selection = False
        while valid_selection:
            print("Choose from the following items:")
            counter = 1
            for item in list_to_select_from:
                print(f"{counter} - {item}")
                counter += 1

            user_selection = int(input())
            print(user_selection)
            if not self.valid_item_selection(counter, user_selection):
                print("while loop")

            else:
                print("How many would you like to add?")

    def valid_item_selection(self, selections, user_selection):
        print("valid_selection")
        if not 1 <= user_selection <= selections:
            print("False")
            return False
        print("True")
        return True

def main():
    g_list = GroceryList()
    # print(g_list)
    g_list.get_user_items()


if __name__ == '__main__':
    main()