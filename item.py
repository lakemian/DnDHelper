import csv

item_list = []
table_list = []
magic_item_list = []


class Item(object):
    def __init__(self, name, category, weight, cost, properties, roll_lo, roll_hi):
        self.name = name
        self.category = category
        self.weight = weight
        self.cost = cost
        self.properties = properties
        self.roll_lo = roll_lo
        self.roll_hi = roll_hi

    def get_stats(self):
        info_str = f'{self.name}\nWeight: {str(self.weight)}\nCost: {self.cost}\nProperties: {str(self.properties)}'
        print(info_str)
        # print(*self.properties, sep='\n')

    def __str__(self):
        info_str = "%s-%s\t%s" % (self.roll_lo, self.roll_hi,self.name)
        return info_str

    @staticmethod
    def search(name):
        flag = 0
        for i in range(len(item_list)):
            if item_list[i].get_name().lower() == name.lower():
                return item_list[i]
                flag = 1
        if flag == 0:
            return "Item not found"

    def get_name(self):
        return self.name

    def get_category(self):
        return self.category

    def get_weight(self):
        return self.weight

    def get_cost(self):
        return self.cost

    def get_properties(self):
        return self.properties

    @staticmethod
    def read_file():
        with open('dummyfile.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    # print(f'{", ".join(row)}')
                    line_count += 1
                else:
                    x = Item(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
                    item_list.append(x)
                    # itemList[line_count-1].get_stats()
                    line_count += 1
        # print(f'Processed {line_count} lines.')
        csv_file.close()


class Weapon(Item):
    def __init__(self, name, category, weight, cost, damage, properties):
        self.damage = damage
        Item.__init__(self, name, category, weight, cost, properties)

    def get_stats(self):
        weaponstat_string = \
            f"{self.name}\nCategory: {self.category}\nWeight:" \
            f" {self.weight}\nDamage: {self.damage}\nProperties: {self.properties}\nCost: {self.cost}"
        print(weaponstat_string)


class Armor(Item):
    def __init__(self, name, category, weight, cost, atype, ac, properties):
        super(Armor, self).__init__(name, category, weight, cost, properties)
        self.atype = atype
        self.ac = ac

    def get_stats(self):
        armorstat_string = \
            f"{self.name}\nCategory: {self.category}\nWeight: {self.weight}\nArmor Type: {self.atype}\nAC: " \
            f"{self.ac}\nProperties: {self.properties}\nCost: {self.cost}"
        print(armorstat_string)


class MagicItem(Item):
    def __init__(self, name, category, weight, cost, rarity, properties, roll_lo, roll_hi):
        super(MagicItem, self).__init__(name, category, weight, cost, properties, roll_lo, roll_hi)
        self.rarity = rarity
        if self.rarity == "common":
            self.cost = 50
        elif self.rarity == "uncommon":
            self.cost = 100
        elif self.rarity == "rare":
            self.cost = 500
        elif self.rarity == "very rare":
            self.cost = 2000
        elif self.rarity == "legendary":
            self.cost = 5000
        elif self.rarity == "artifact":
            self.cost = 10000

    def get_stats(self):
        magic_item_str = f'{self.name}\nWeight: {str(self.weight)}\nCost: {self.cost}\nRarity: {self.rarity}' \
                         f'\nProperties: {str(self.properties)}'
        print(magic_item_str)

    @staticmethod
    def read_file():
        with open('realMagicItem.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    # print(f'{", ".join(row)}')
                    line_count += 1
                else:
                    x = MagicItem(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                    magic_item_list.append(x)
                    # itemList[line_count-1].get_stats()
                    line_count += 1
        # print(f'Processed {line_count} lines.')
        csv_file.close()

class LootTable:
    def __init__(self, title, num_items, table):
        self.title = title
        self.num_items = num_items
        self.table = []
        self.table = table

    def print_table(self):
        str1 = "%s\nDie: d%s \nList of Items:" % (self.title, self.num_items)
        print(str1)
        for x in range(len(self.table)):
            print(self.table[x])

    @staticmethod
    def search1(name):
        flag = 0
        for i in range(len(item_list)):
            if item_list[i].get_name().lower() == name.lower():
                return item_list[i]
                flag = 1
        if flag == 0:
            return "Item not found"

    @staticmethod
    def read_loot_table_file():
        with open('magicItem.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0

            for row in csv_reader:
                table_list_items = []
                if line_count == 0:
                    line_count += 1
                else:
                    for y in range(int(row[1])):
                        table_list_items.append(LootTable.search1(row[y+2]))
                    x = LootTable(row[0], row[1], table_list_items)

                    table_list.append(x)
                    del table_list_items
                    line_count += 1
        csv_file.close()