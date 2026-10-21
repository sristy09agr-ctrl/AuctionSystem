


items = [
    {"id": 1, "name": "Laptop", "starting_price": 25000, "highest_bid": 25000},
    {"id": 2, "name": "Headphones", "starting_price": 1500, "highest_bid": 1500},
    {"id": 3, "name": "Smartphone", "starting_price": 12000, "highest_bid": 12000}
]

def show_menu():
    """Display the main menu."""
    print("\n===== AUCTION SYSTEM =====")
    print("1. View auction items")
    print("2. Place a bid")
    print("3. View leaderboard")
    print("4. Register bidder")
    print("5. Close an auction")
    print("6. Exit")



def view_items():
    """Display all available auction items."""
    print("\n--- AUCTION ITEMS ---")

    for item in items:
        print(f"ID: {item['id']}")
        print(f"Name: {item['name']}")
        print(f"Starting price: Rs. {item['starting_price']}")
        print(f"Current highest bid: Rs. {item['highest_bid']}")
        print("--------------------")


bidders = []


def register_bidder():
    """Register a new bidder."""
    print("\n--- BIDDER REGISTRATION ---")

    name = input("Enter bidder name: ").strip()

    if name == "":
        print("Name cannot be empty.")
        return

    bidder_id = len(bidders) + 1

    bidder = {
        "id": bidder_id,
        "name": name,
        "total_bids": 0,
        "items_won": 0
    }

    bidders.append(bidder)

    print(f"Bidder registered successfully!")
    print(f"Your bidder ID is: {bidder_id}")



def place_bid():
    """Allow a registered bidder to place a valid bid."""

    if not bidders:
        print("No bidders registered. Please register first.")
        return

    view_items()

    try:
        item_id = int(input("Enter the item ID: "))
        bidder_id = int(input("Enter your bidder ID: "))
        amount = float(input("Enter your bid amount: "))
    except ValueError:
        print("Invalid input. Enter numeric IDs and a valid amount.")
        return

    item = None
    for current_item in items:
        if current_item["id"] == item_id:
            item = current_item
            break

    if item is None:
        print("Item not found.")
        return

    
    if item.get("closed", False):
        print("This auction is closed. Bidding is no longer allowed.")
        return


    bidder = None
    for current_bidder in bidders:
        if current_bidder["id"] == bidder_id:
            bidder = current_bidder
            break

    if bidder is None:
        print("Bidder not found. Please register first.")
        return

    if amount <= 0:
        print("Bid amount must be positive.")
        return

    if amount <= item["highest_bid"]:
        print("Your bid must be higher than the current highest bid.")
        return

    item["highest_bid"] = amount
    item["highest_bidder"] = bidder["name"]
    bidder["total_bids"] += 1

    print("Bid placed successfully!")
    print(f"Item: {item['name']}")
    print(f"New highest bid: Rs. {amount:.2f}")
    print(f"Highest bidder: {bidder['name']}")


    
def close_auction():
    """Close an auction item and record its winner."""

    view_items()

    try:
        item_id = int(input("Enter the item ID to close: "))
    except ValueError:
        print("Please enter a valid numeric item ID.")
        return

    item = None
    for current_item in items:
        if current_item["id"] == item_id:
            item = current_item
            break

    if item is None:
        print("Item not found.")
        return

    if item.get("closed", False):
        print("This auction is already closed.")
        return

    item["closed"] = True

    if "highest_bidder" in item:
        for bidder in bidders:
            if bidder["name"] == item["highest_bidder"]:
                bidder["items_won"] += 1
                break

        print(f"Auction closed! Winner: {item['highest_bidder']}")
        print(f"Winning price: Rs. {item['highest_bid']:.2f}")
    else:
        print("Auction closed without any bids.")




def view_leaderboard():
    """Display bidder rankings based on auction performance."""

    print("\n===== AUCTION LEADERBOARD =====")

    if not bidders:
        print("No bidders registered yet.")
        return

    ranked_bidders = sorted(
        bidders,
        key=lambda bidder: (bidder["items_won"], bidder["total_bids"]),
        reverse=True
    )

    for rank, bidder in enumerate(ranked_bidders, start=1):
        print(f"\nRank: {rank}")
        print(f"Name: {bidder['name']}")
        print(f"Items won: {bidder['items_won']}")
        print(f"Successful bids: {bidder['total_bids']}")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            view_items()
        elif choice == "2":
            place_bid()
        elif choice == "3":
            view_leaderboard()
        elif choice == "4":
           register_bidder()
        elif choice == "5":
            close_auction()
            break
        elif choice == "6":
            print("Exiting Auction System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")


if __name__ == "__main__":
    main()
