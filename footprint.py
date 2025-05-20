# 1. Group by Price:
    # Sum total buy volume per price level
    # Sum total sell volume per price level
    # Create price_ladder dict to store values

# 2. Build Ladder Structure:
    # Create a row per price level showing Buy | Sell   
    # Show delta ( total buys - total sells)

# 3 Highlight POC:  
    # Identify price level with highest total volume

# 4 Record Metadata:
    # Bar number
    # Start and end time
    # Price high, low
    # Total volume
    # Delta

# 5 Store and Repeat:
    # Store each bar’s ladder and metadata
    # Move to next 1,000 ticks


with open("synthetic_mnq_ticks.csv") as file:
    
    file.readline() # Skips the header row
    
    buy_volume = 0
    sell_volume = 0
    price_ladder = {}


    for x in file.readlines():
        Timestamp, Price, Volume, Side = x.strip().split(',')
        
        if float(Price) not in price_ladder:
            price_ladder[float(Price)] = {"Buy": 0, "Sell": 0}

        if Side == "Buy":
            buy_volume += int(Volume)
            price_ladder[float(Price)]["Buy"] += int(Volume)

        elif Side == "Sell":
            sell_volume += int(Volume)
            price_ladder[float(Price)]["Sell"] += int(Volume)