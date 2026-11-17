print("Welcome to the Fantasy Item Shop!")
player_name = input("What is your name? ")
player_gold = 100
inventory = []
print(f"Hello {player_name}! You have {player_gold} gold.")
items = ["Sword", "Shield", "Potion", "Bow"]
prices = [50, 40, 20, 60]
while True:
    print("\n=== Fantasy Item Shop ===\n")
    for i in range(len(items)):
        print(f"{i + 1}. Buy {items[i]} ({prices[i]} gold)")
    print("5. View Inventory")
    print("6. Exit Shop")
    choice = input("\nWhat would you like to do? ")
    match choice:
        case "1":
            if player_gold >= prices[0]:
                player_gold = player_gold - prices[0]
                inventory.append(items[0])
                print(f"\nYou bought a {items[0]}!")
                print(f"Remaining gold: {player_gold}")
            else:
                print("\nYou don't have enough gold!")
        case "2":
            if player_gold >= prices[1]:
                player_gold = player_gold - prices[1]
                inventory.append(items[1])
                print(f"\nYou bought a {items[1]}!")
                print(f"Remaining gold: {player_gold}")
            else:
                print("\nYou don't have enough gold!")
        case "3":
            if player_gold >= prices[2]:
                player_gold = player_gold - prices[2]
                inventory.append(items[2])
                print(f"\nYou bought a {items[2]}!")
                print(f"Remaining gold: {player_gold}")
            else:
                print("\nYou don't have enough gold!")
        case "4":
            if player_gold >= prices[3]:
                player_gold = player_gold - prices[3]
                inventory.append(items[3])
                print(f"\nYou bought a {items[3]}!")
                print(f"Remaining gold: {player_gold}")
            else:
                print("\nYou don't have enough gold!")
        case "5":
            if len(inventory) == 0:
                print("\nYour inventory is empty!")
            else:
                print("\nYour inventory:")
                for item in inventory:
                    print(f"- {item}")
        case "6":
            print(f"\nThanks for visiting, {player_name}!")
            print(f"You have {player_gold} gold left.")
            break
        case _:
            print("\nInvalid option! Please choose a number from 1 to 6.")