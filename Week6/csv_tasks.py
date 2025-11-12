import csv


def read(file_path):
    with open(file_path) as file:
        csv_reader = csv.reader(file)

        headings = next(csv_reader)
        print(f"Headings:\n{headings}")

        print("Values:")
        for values in csv_reader:
            print(values)

def run_task1():
    read("clothing.csv")

if __name__ == "__main__":
    run_task1()

import csv


def extract(file_path):
    print("Extracting...", end="")
    with open(file_path) as file:

        csv_reader = csv.reader(file)
        next(csv_reader)
        names = ""
        for values in csv_reader:
            names += f"{values[1]}\n"
    print("Done!")
    print(f"The extracted items are:\n{names}")

def run_task2():
    extract("clothing.csv")

if __name__ == "__main__":
    run_task2()

def export(file_path, num_items):
    print("Exporting...")
    with open(file_path, "a") as file:
        for count in range(num_items):
            print("Please enter the item id:")
            item_id = int(input())

            print("Please enter the item name:")
            item_name = input()

            print("Please enter the item colour:")
            item_colour = input()

            data = f"{item_id},{item_name},{item_colour}\n"
            file.write(data)
    print("Done!")

def run_task3():
    export("exported_items.csv", 2)

if __name__ == "__main__":
    run_task3()