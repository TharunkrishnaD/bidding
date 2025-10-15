import csv

class BiddingSystem:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.records = self.datas()

    def datas(self):
        records = []
        with open(self.csv_file, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['Price'] = int(row['Price'].replace('$', ''))
                records.append(row)
        return records

    def get_items_type(self):
        return sorted(set(record['Type'] for record in self.records))

    def get_items_name(self, item_type):
        return sorted(set(record['Name'] for record in self.records if record['Type'] == item_type))

    def get_high_value(self, item_name):
        bids = [record for record in self.records if record['Name'] == item_name]
        high_value = max(bids, key=lambda x: x['Price'])
        return high_value

    def run(self):
        while True:
            types = self.get_items_type()
            print(types)
            print("Available Types:")
            for k, v in enumerate(types, 1):
                print(f"{k}. {v}")
            print("0.  Exit")
            type_choice = input("Enter the number of the Type you want to see: ")
            if type_choice == '0':
                print("Exiting the bidding system.")
                break

            if not type_choice.isdigit() or int(type_choice) < 1 or int(type_choice) > len(types):
                print("-"*20)
                print("Error : Invalid Number, Entered a valid number")
                print("-"*20)
                continue

            selected_type = types[int(type_choice) - 1]
            print(f"You selected Type: {selected_type}")

            names = self.get_items_name(selected_type)

            print("Available Names:")
            for k, v in enumerate(names, 1):
                print(f"{k}. {v}")
            print("0.  Back")

            enter_name = input("Enter the number of the Name you want to see highest bid for: ")
            if enter_name == '0':
                continue

            if not enter_name.isdigit() or int(enter_name) < 1 or int(enter_name) > len(names):
                print("-"*20)
                print("Error : Invalid Number, Entered a valid number")
                print("-"*20)
                continue

            selected_name = names[int(enter_name) - 1]

            high_value = self.get_high_value(selected_name)
            print(f"Highest Bid for {selected_name}:")
            print(f"Bidder: {high_value['User']}")
            print(f"Amount: ${high_value['Price']}")
            print("-" * 40)


if __name__ == "__main__":
    system = BiddingSystem("bidding_data.csv")
    system.run()
