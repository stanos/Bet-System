SLOT_MACHINE_PRICE = 10

class slot_machine:
    def __init__(self, balance) -> None:
        self.balance = balance
        if self.balance < SLOT_MACHINE_PRICE:
            self.can_gamble = False
        else:
            self.can_gamble = True

    def gamble(self):
        if self.can_gamble:
            self.after_balance = self.balance - SLOT_MACHINE_PRICE
            print(f"slot gamble. {self.after_balance}")
            return self.after_balance
        else:
            print("you don't have enough money, you can't play this game.")


def get_input():
    input_comnmand = input("#: ")
    return input_comnmand

def main():
    balance = 10
    game_running = True
    while game_running:
        input = get_input()
        if input == "balance":
            print(balance)
        
        elif input == "slot machine":
            slot_game = slot_machine(balance)
            balance = slot_game.gamble()
        elif input == "exit":
            game_running = False
        else:
            print("not a valid command.")

if __name__ == "__main__":
    main()
