from item import *


def search():
    flag = 0
    x = input("Item name: ")
    for i in range(len(item_list)):
        if item_list[i].get_name().lower() == x.lower():
            item_list[i].get_stats()
            flag = 1
    if flag == 0:
        print("Item not found")


def search_magic():
    flag = 0
    x = input("Item name: ")
    for i in range(len(magic_item_list)):
        if magic_item_list[i].get_name().lower() == x.lower():
            magic_item_list[i].get_stats()
            flag = 1
    if flag == 0:
        print("Item not found")


def list_items():
    y = input("Choose type to list:\n1. Items\n4. Magic Item\n").lower()
    if y == "Items".lower() or y == "1":
        for i in range(len(item_list)):
            if isinstance(item_list[i], Item):
                print(item_list[i].name)
    elif y == "Weapons".lower() or y == "2":
        for i in range(len(item_list)):
            if isinstance(item_list[i], Weapon):
                print(item_list[i].name)
    elif y == "Armor".lower() or y == "3":
        for i in range(len(item_list)):
            if isinstance(item_list[i], Armor):
                print(item_list[i].name)
    elif y == "Magic Item".lower() or y == "4":
        for i in range(len(magic_item_list)):
            if isinstance(magic_item_list[i], MagicItem):
                print(magic_item_list[i].name)
    else:
        print("Invalid Input")


def options():
    flag = 1
    while flag != 0:
        options_str = "1. Search for item\n2. List items\n3. Search Magic Items\n0. End\n"
        x = input(options_str).lower()
        if x == "1" or x == "Search for item".lower():
            search()
        elif x == "2" or x == "List items".lower():
            list_items()
        elif x == "3" or x == "Search Magic Items":
            search_magic()
        elif x == "0" or x == "End".lower():
            flag = 0


Item.read_file()
LootTable.read_loot_table_file()
MagicItem.read_file()

options()
