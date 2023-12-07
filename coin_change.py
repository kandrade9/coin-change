def main():
    while True:
        try:
            change = float(input("Change: "))
            if change > 0:
                break
            else:
                print("Enter value greater than 0.")
        except ValueError:
            print("Please enter only numbers.")
    result = num_coins(change)
    print(f"Change can be returned with a minimum of {result} coins.")

def num_coins(cents):
    coins = [25, 10, 5, 1]
    count = 0
    for coin in coins:
        while cents >= coin:
            cents -= coin
            count += 1
    return count

main()
