from ibapi.client import *
from ibapi.wrapper import *
from datetime import datetime, time

class TestApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)

    def check_market_hours(self):
        current_time = datetime.now().time()
        market_open = time(9, 30)  # Assuming the market opens at 9:30 AM
        market_close = time(16, 0)  # Assuming the market closes at 4:00 PM
        return market_open <= current_time <= market_close

    def nextValidId(self, orderId: int):
        if not self.check_market_hours():
            print("Error: Outside of market hours.")
            self.disconnect()
            return

        mycontract = Contract()
        mycontract.symbol = "AAPL"
        mycontract.secType = "STK"
        mycontract.exchange = "SMART"
        mycontract.currency = "USD"

        self.reqContractDetails(orderId, mycontract)

    # ... (rest of the code remains unchanged)

app = TestApp()
app.connect("127.0.0.1", 7497, 100)
app.run()
from ibapi.client import *
from ibapi.wrapper import *
from datetime import datetime, time

class TestApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)

    def check_market_hours(self):
        current_time = datetime.now().time()
        market_open = time(9, 30)  # Assuming the market opens at 9:30 AM
        market_close = time(16, 0)  # Assuming the market closes at 4:00 PM
        return market_open <= current_time <= market_close

    def nextValidId(self, orderId: int):
        if not self.check_market_hours():
            print("Error: Outside of market hours.")
            self.disconnect()
            return

        mycontract = Contract()
        mycontract.symbol = "AAPL"
        mycontract.secType = "STK"
        mycontract.exchange = "SMART"
        mycontract.currency = "USD"

        self.reqContractDetails(orderId, mycontract)

    # ... (rest of the code remains unchanged)

app = TestApp()
app.connect("127.0.0.1", 7497, 100)
app.run()
