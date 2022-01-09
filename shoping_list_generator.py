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
                if item_to_search.lower() in item:
                    selection_list.append(item)
                    adding_items = False
            if selection_list == []:
                print("Item not found. Try again")

        self.selection_menu(selection_list)
        # print(f"You have added {self.get_quantity()} {self.get_grocery()} Specification: {self.get_desc()} \n")
        self.add_item(self.get_grocery(), self.get_desc(), self.get_quantity())

        add_more_items = input("Would you like to add more items? (Y/N) ")
        if add_more_items[0].lower() == "y":
            print("adding more")
            self.get_user_items()
            return # break
        elif add_more_items[0].lower() == "n":
            print("no more add")
            return # break
        else:
            print("Invalid choice")
            return # False

        return self.get_shopping_list_data()

    def add_item(self, grocery_name, grocery_desc, grocery_quantity):
        add_list = list()
        add_list.append(grocery_name)
        add_list.append(grocery_desc)
        add_list.append(grocery_quantity)
        self.get_shopping_list_data().append(add_list)

    def selection_menu(self, list_to_select_from):
        invalid_selection = True
        if list_to_select_from == []:
            print("Item Not Found.Try again \n")
            invalid_selection = False
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

        if not 1 <= user_selection <= selections-1:
            print("Try again. See menu below for available options\n")
            return False
        return True


def generate_shopping_list_file(list_to_generate):
    headers = l1 = [["Type", "Brand/Description", "Quantity"]]
    complete_list = headers + list_to_generate
    # print(complete_list)
    with open('shopping_list.csv', 'w') as outfile:
        for line in complete_list:

            outfile.write(line)
        # for row in complete_list:
        #     csv_str = ""
        #     for grocery in complete_list[row]:


def main():
    g_list = GroceryList()
    # print(g_list)
    g_list.get_user_items()
    # g_list.generate_shopping_list()
    shopping_list1 = g_list.get_shopping_list_data()
    # need function to iterate through list and generate the shopping list csv file
    generate_shopping_list_file(shopping_list1)


if __name__ == '__main__':
    main()
