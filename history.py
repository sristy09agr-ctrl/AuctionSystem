
def view_history(auction_history):
    """Display the results of previously closed auctions."""
    print("\n--- AUCTION HISTORY ---")

    if not auction_history:
        print("No auction history available yet.")
        return

    for result in auction_history:
        print(f"\nItem: {result['item_name']}")

        if result["winner"] is not None:
            print(f"Winner: {result['winner']}")
            print(f"Final price: Rs. {result['final_price']:.2f}")
        else:
            print("Winner: No bids")
