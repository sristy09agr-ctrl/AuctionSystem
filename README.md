# Auction System Simulator + Leaderboard/Results Tracker

## CS213 – Python Course Project

**Name:** Sristy Kumari  
**ID Number:** CS25B1036  
**Project Title:** Auction System Simulator + Leaderboard/Results Tracker

## 1. About the Project

The Auction System Simulator is a Python-based project that simulates a simple auction system. It allows users to register as bidders, add items for auction, and place bids on available items. The program checks whether a bid is valid and updates the highest bid whenever a higher bid is placed. An auction can be closed, after which the winner and final bidding price are recorded. The project also includes a leaderboard to show bidder performance and an auction history to view the results of previous auctions. Auction data is saved in a JSON file so that it can be loaded again when the program is restarted.

## 2. Problem It Addresses

In an auction, it is important to keep track of items, bidders, bids, and the final results. Managing these details manually can become confusing, especially when several items and bidders are involved.

This project provides a simple way to manage these activities through a menu-driven program. It demonstrates the basic working of an auction system and how Python can be used to store information, validate inputs, and maintain auction records.

## 3. Features

- **View Auction Items:** Displays item names, starting prices, current highest bids, highest bidders, and auction status.
- **Place a Bid:** Allows registered bidders to bid on items and checks whether the bid is valid.
- **View Leaderboard:** Displays bidder rankings based on auction performance.
- **Register a Bidder:** Registers new bidders and assigns them unique IDs.
- **Close an Auction:** Ends bidding for an item and records the winner and final price, if there is a winning bid.
- **Add an Auction Item:** Allows new items to be added to the system.
- **View Auction History:** Displays the results of previously closed auctions.
- **Save Data:** Stores auction items, bidder information, and auction history in a JSON file for future use.

## 4. Input and Output

### Inputs

The program takes input from the user through the terminal, including:

- Menu option
- Bidder name
- Item ID and bidder ID
- Item name and starting price when adding an item
- Bid amount

### Outputs

The program displays:

- Available auction items and their current status
- Whether a bid was accepted or rejected
- The current highest bid and highest bidder
- Auction winner and final price
- Bidder leaderboard
- Results of previous auctions

The data is also saved locally so that it can be reused in later runs.

## 5. Python Concepts Demonstrated

The project demonstrates the following concepts from the CS213 Python course.

### 1. Control Flow

The program uses `while` loops and conditional statements such as `if`, `elif`, and `else` to display the menu, process user choices, and validate bids. For example, a bid is rejected if it is not higher than the current highest bid or if the auction has already been closed.

### 2. Functions

The program is divided into functions for tasks such as registering bidders, placing bids, adding items, closing auctions, and displaying results. These functions accept parameters such as item lists, bidder lists, and auction history so that they can work with the program's data.

### 3. Data Structures

Lists and dictionaries are used to store and organize auction information. The lists contain auction items, registered bidders, and auction history, while dictionaries store details such as IDs, names, prices, and auction status.

### 4. File Handling

The project uses a JSON file named `auction_data.json` to save and load data. This allows auction information to remain available even after the program is closed and started again.

### 5. Exception Handling

The program uses `try` and `except` blocks to handle invalid numeric input. This prevents the program from crashing when a user enters something other than a valid number where a numeric value is required.

### 6. Modules

The code is organized into separate Python files. Each file handles a particular part of the project, such as auction operations, bidder registration, history, leaderboard, or data storage. These files are connected using Python imports.

### Additional Concept: Docstrings

Docstrings are included in functions to describe their purpose and make the code easier to understand.

## 6. Technologies Used

- Python 3
- JSON for storing and retrieving data
- Visual Studio Code for writing and running the program
- Git and GitHub for version control

## 7. Project Structure

```text
AuctionSystem/
│
├── main.py
├── auction.py
├── bidder.py
├── history.py
├── leaderboard.py
├── storage.py
├── auction_data.json
├── .gitignore
└── README.md
```

- `main.py` – Displays the main menu and connects the different functions.
- `auction.py` – Handles viewing items, adding items, placing bids, and closing auctions.
- `bidder.py` – Handles bidder registration.
- `history.py` – Displays previous auction results.
- `leaderboard.py` – Displays bidder rankings.
- `storage.py` – Handles saving and loading data.
- `auction_data.json` – Stores the program's data locally when generated by the application.

## 8. How to Run the Project

### Requirements

- Python 3 installed on the computer
- A terminal or an editor such as Visual Studio Code

### Steps

1. Download or clone the project repository.
2. Open the project folder in the terminal.
3. Run the following command:

   ```bash
   python main.py
   ```

   On Windows, the following command can also be used:

   ```powershell
   py main.py
   ```

4. Select an option from the menu and follow the instructions displayed by the program.

## 9. Data Storage

The program stores its data in `auction_data.json`. The file contains information about auction items, bidders, and auction history. When the program starts, it loads the previously saved data if available.

The JSON file is excluded from Git tracking so that local bidder records and test data are not automatically published to the GitHub repository.

## 10. Conclusion

This project helped me apply Python concepts to a practical problem. By developing the Auction System Simulator, I worked with functions, data structures, control flow, exception handling, JSON file handling, and modules. The project brings these concepts together in a menu-driven application that manages auction items, bids, bidders, and results.

