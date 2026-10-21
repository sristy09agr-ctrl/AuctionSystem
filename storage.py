
import json

def save_data(items, bidders, auction_history):
    """Save auction items, bidders, and history to a JSON file."""
    data = {
        "items": items,
        "bidders": bidders,
        "auction_history": auction_history
    }

    try:
        with open("auction_data.json", "w") as file:
            json.dump(data, file, indent=4)
    except OSError:
        print("Error: Could not save auction data.")


def load_data():
    """Load auction items, bidders, and history from a JSON file."""
    try:
        with open("auction_data.json", "r") as file:
            data = json.load(file)

        return (
            data["items"],
            data["bidders"],
            data.get("auction_history", [])
        )

    except FileNotFoundError:
        print("No saved data found. Starting a new auction.")
    except (json.JSONDecodeError, KeyError, TypeError):
        print("Saved data is invalid. Starting with default data.")

    return None
