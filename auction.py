
def view_items(items):
    """Display all available auction items."""
    print("\n--- AUCTION ITEMS ---")

    for item in items:
        print(f"ID: {item['id']}")
        print(f"Name: {item['name']}")
        print(f"Starting price: Rs. {item['starting_price']}")
        print(f"Current highest bid: Rs. {item['highest_bid']}")
        print(f"Highest bidder: {item.get('highest_bidder', 'No bids yet')}")
        status = "Closed" if item.get("closed", False) else "Open"
        print(f"Status: {status}")
        print("--------------------")



def add_item(items, bidders, auction_history, save_data):
    """Add a new item to the auction."""

    print("\n--- ADD AUCTION ITEM ---")

    name = input("Enter item name: ").strip()

    if name == "":
        print("Item name cannot be empty.")
        return

    try:
        starting_price = float(input("Enter starting price: "))
    except ValueError:
        print("Invalid price. Please enter a number.")
        return

    if starting_price <= 0:
        print("Starting price must be positive.")
        return

    # Generate a new, unique item ID
    new_id = max(
        (item["id"] for item in items),
        default=0
    ) + 1

    new_item = {
        "id": new_id,
        "name": name,
        "starting_price": starting_price,
        "highest_bid": starting_price,
        "closed": False
    }

    items.append(new_item)
    save_data(items, bidders, auction_history)

    print(f"Item '{name}' added successfully!")
    print(f"Item ID: {new_id}")



def place_bid(items, bidders, auction_history, save_data):
    """Allow a registered bidder to place a valid bid."""

    if not bidders:
        print("No bidders registered. Please register first.")
        return

    view_items(items)

    try:
        item_id = int(input("Enter the item ID: "))
        bidder_id = int(input("Enter your bidder ID: "))
        amount = float(input("Enter your bid amount: "))

        if item_id <= 0 or bidder_id <= 0:
            print("Item ID and bidder ID must be positive integers.")
            return

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

    save_data(items, bidders, auction_history)

    print("Bid placed successfully!")
    print(f"Item: {item['name']}")
    print(f"New highest bid: Rs. {amount:.2f}")
    print(f"Highest bidder: {bidder['name']}")




def close_auction(items, bidders, auction_history, save_data):
    """Close an auction item and record its result."""

    view_items(items)

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

    # Mark the auction as closed
    item["closed"] = True

    if item.get("highest_bidder"):
        result = {
            "item_id": item["id"],
            "item_name": item["name"],
            "winner": item["highest_bidder"],
            "final_price": item["highest_bid"]
        }

        for bidder in bidders:
            if bidder["name"] == item["highest_bidder"]:
                bidder["items_won"] += 1
                break

        print(f"Auction closed! Winner: {item['highest_bidder']}")
        print(f"Winning price: Rs. {item['highest_bid']:.2f}")

    else:
        result = {
            "item_id": item["id"],
            "item_name": item["name"],
            "winner": None,
            "final_price": 0
        }

        print("Auction closed without any bids.")

    auction_history.append(result)
    save_data(items, bidders, auction_history)
