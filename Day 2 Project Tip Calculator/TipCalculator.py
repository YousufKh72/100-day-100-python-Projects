def TipCalculator():
    print("Welcome to the tip calculator.")
    TotalBill = float(input("What was the total bill?\n"))
    Tip = int(input("How much tip would you like to give? 10, 12, or 15?\n"))
    People = float(input("How many people to split the bill?\n"))

    Bill = round((TotalBill + (TotalBill * float(Tip) / 100))/People, 2)
    return(f"Each person should pay:{Bill}")


if __name__ == "__main__":
    print(TipCalculator())