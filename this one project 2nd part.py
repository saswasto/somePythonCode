MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount

def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES})? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    return lines

def get_bet():
    while True:
        amount = input(f"What would you like to bet on each line? (${MIN_BET}-${MAX_BET}) $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
    return amount

def play_game(balance, lines, bet):
    total_bet = bet * lines
    if total_bet > balance:
        print(f"You do not have enough to bet that amount. Your current balance is: ${balance}")
    else:
        balance -= total_bet

    return balance

def main():
    balance = deposit()
    while True:
        lines = get_number_of_lines()
        bet = get_bet()
        balance = play_game(balance, lines, bet)
        print(f"Your current balance is: ${balance}")
        if balance == 0:
            print("Game over! You are out of money.")
            break
        choice = input("Would you like to play again? (y/n) ")
        if choice.lower() != "y":
            break
    print("Thanks for playing!")
if __name__ == "__main__":
    main()
