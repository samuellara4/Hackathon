# Author: Samuel Lara
# Date: 01/05/2022
# Description: This program will take user input and compare the item searched to a groceries data set and generate a
# shopping list and save as a csv file

import csv


class ItemNotFoundError(Exception):
    pass


class GroceryList:

    def __init__(self):

        # grocery list data
        self._g_list = self.generate_grocery_list()
        # item attributes
        self._grocery_item = ""
        self._quantity = 0
        self._desc = ""
        self._shopping_list_data = list()

    def get_grocery(self):
        return self._grocery_item

    def get_quantity(self):
        return self._quantity

    def get_desc(self):
        return self._desc

    def set_grocery_item(self, item_to_set):
        self._grocery_item = item_to_set

    def set_quantity(self, quantity_to_set):
        self._quantity = quantity_to_set

    def set_desc(self, desc_to_set):
        self._desc = desc_to_set

    def get_grocery_list(self):
        return self._g_list

    def get_shopping_list_data(self):
        return self._shopping_list_data

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
            print(f"You have added {self.get_quantity()} {self.get_grocery()} Specification: {self.get_desc()} \n")
            self.add_item(self.get_grocery(), self.get_desc(), self.get_quantity())

            add_more_items = input("Would you like to add more items? (Y/N) ")
            if add_more_items[0].lower() == "y":
                self.get_user_items()
            elif add_more_items[0].lower() == "n":
                break
            else:
                return False
            # need to store the item and quantity then create menu to ask if additional items
            # if no additional items then generates the shopping list in csv file. If add more items
            # returns to the selection menu until user exits to generate shopping list (csv)
            # print(f"You have added {self.get_quantity()} {self.get_grocery()} Specification: {self.get_desc()} \n")
        return False

    def add_item(self, grocery_name, grocery_desc, grocery_quantity):
        self.get_shopping_list_data().append(grocery_name)
        self.get_shopping_list_data().append(grocery_desc)
        self.get_shopping_list_data().append(grocery_quantity)

    def selection_menu(self, list_to_select_from):
        invalid_selection = True
        if list_to_select_from == []:
            print("Item Not Found.Try again \n")
            invalid_selection = False
        # invalid_selection = True
        while invalid_selection:
            # print("invalid_selection:", invalid_selection)
            print("Choose from the following items:")
            counter = 1
            for item in list_to_select_from:  # menu selection
                print(f"{counter} - {item}")
                counter += 1

            try:
                user_selection = int(input("Your selection: "))
            except ValueError:
                print("Select from the menu only \n")
                continue
            # print(user_selection, list_to_select_from)
            if self.valid_item_selection(counter, user_selection):
                brand_description = input("What brand or type? ")
                quantity = input("How many would you like to add? ")
                selected_item = list_to_select_from[user_selection-1]
                self.set_desc(brand_description)
                self.set_quantity(quantity)
                self.set_grocery_item(selected_item)
                print("return", quantity, selected_item, brand_description)
                return

    def valid_item_selection(self, selections, user_selection):
        # print("Checking if valid_selection")
        # print(selections)
        if not 1 <= user_selection <= selections-1:
            print("Try again. See menu below for available options\n")
            return False
        # print("True")
        return True

    # def generate_shopping_list(self):
    #     with open('shopping_list.csv', 'w') as outfile:
    #         pass

def main():
    g_list = GroceryList()
    # print(g_list)
    g_list.get_user_items()
    # g_list.generate_shopping_list()
    print(g_list.get_shopping_list_data())

if __name__ == '__main__':
    main()