
def register_bidder(bidders, items, auction_history, save_data):
    """Register a new bidder and save the updated data."""

    print("\n--- BIDDER REGISTRATION ---")
    name = input("Enter bidder name: ").strip()

    if not name:
        print("Bidder name cannot be empty.")
        return

    # Prevent duplicate bidder names
    for bidder in bidders:
        if bidder["name"].lower() == name.lower():
            print("This bidder name is already registered.")
            print(f"Existing bidder ID: {bidder['id']}")
            return

    # Generate a unique bidder ID
    bidder_id = max(
        (bidder["id"] for bidder in bidders),
        default=0
    ) + 1

    bidder = {
        "id": bidder_id,
        "name": name,
        "items_won": 0,
        "total_bids": 0
    }

    bidders.append(bidder)

    save_data(items, bidders, auction_history)

    print(f"Bidder registered successfully! Your bidder ID is {bidder_id}.")
