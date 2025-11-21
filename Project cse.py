# Monthly Expense Management System
import csv
import datetime

DATA_FILE = "data_log.csv"

def file():
    try:
        with open(DATA_FILE, "w", newline="") as txt:
            Write = csv.writer(txt)
            Write.writerow(["Date", "Category", "Amount", "Note"])
    except FileExistsError:
        pass


def Expense():
    Date = datetime.date.today().strftime("%Y-%m-%d")
    Category = input("Enter Category (Food/Travel/Total Bill/Other): ")
    Amount = float(input("Enter amount: "))
    Note = input("Enter the note: ")

    with open(DATA_FILE, "a", newline="") as txt:
        Write = csv.writer(txt)
        Write.writerow([Date, Category, Amount, Note])

    print("\nData Added Successfully!\n")


def View_Expense():
    print("\n---Total Expense List---\n")
    with open(DATA_FILE, "r") as txt:
        reader = csv.reader(txt)
        for row in reader:
            print(row)
    print("\n---End of the List---\n")


def Monthly_Expense_Summary():
    Month = input("Enter month (MM format): ")
    Year = input("Enter year (YYYY format): ")

    Total_Entry = 0

    with open(DATA_FILE, "r") as txt:
        reader = csv.reader(txt)
        next(reader)  

        for Row in reader:
            Row_Date = Row[0]
            Row_Month = Row_Date[5:7]
            Row_Year = Row_Date[0:4]

            if Row_Month == Month and Row_Year == Year:
                Total_Entry += float(Row[2])

    print(f"\nTotal Expense for {Month}-{Year}: ₹{Total_Entry}\n")


def Menu():
    file()
    
    while True:
        print("--- Monthly Expense Manager---")
        print("1. Add New Expense")
        print("2. View All The Expenses That Has Been Done")
        print("3. Monthly Expense Summary")
        print("4. Exit The Code")

        Entry = input("Enter your choice: ")

        if Entry == "1":
            Expense()
        elif Entry == "2":
            View_Expense()
        elif Entry == "3":
            Monthly_Expense_Summary()
        elif Entry == "4":
            print("Good Day...Bye!")
            break
        else:
            print("Invalid Entry! Please Try again.")

Menu()
