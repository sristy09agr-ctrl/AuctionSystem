
def view_leaderboard(bidders):
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
