from storage import save_data, load_data
from bidder import register_bidder
from auction import view_items, add_item, place_bid, close_auction
from history import view_history
from leaderboard import view_leaderboard

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
    print("6. Add an auction item")
    print("7. View auction history")
    print("8. Exit")



bidders = []
auction_history=[]


def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            view_items(items)
        elif choice == "2":
            place_bid(items, bidders, auction_history, save_data)
        elif choice == "3":
            view_leaderboard(bidders)
        elif choice == "4":
            register_bidder(bidders, items, auction_history, save_data)
        elif choice == "5":
            close_auction(items, bidders, auction_history, save_data)
        elif choice == "6":
            add_item(items, bidders, auction_history, save_data)
        elif choice == "7":
            view_history(auction_history)
        elif choice == "8":
            print("Exiting Auction System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8")


if __name__ == "__main__":
    saved_data = load_data()

    if saved_data is not None:
        items, bidders, auction_history = saved_data

    main()