from ibapi.client import *
from ibapi.wrapper import *
import time

class TestApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)

    def contractDetails(self, reqId, contractDetails):
        print(f"contract details: {contractDetails.longName}")

    def contractDetailsEnd(self, reqId):
        print("End of contractDetails")
        self.disconnect()

def main():
    app = TestApp()

    app.connect("127.0.0.1", 7497, 1000)

    mycontract = Contract()
    mycontract.symbol = "AAPL"
    mycontract.secType = "STK"
    mycontract.exchange = "SMART"
    mycontract.currency = "USD"
    mycontract.primaryExchange = "ISLAND"

    time.sleep(3)

    app.reqContractDetails(1, mycontract)

    app.run()

if __name__ == "__main__":
    main()