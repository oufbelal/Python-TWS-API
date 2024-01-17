from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.order import Order

class TestApp(EClient, EWrapper):
    def __init__(self):
        EClient.__init__(self, self)

    def nextValidId(self, orderId: int):
        self.start_order_id = orderId
        self.place_next_order()

    def place_next_order(self):
        contract = Contract()
        contract.symbol = "AAPL"
        contract.secType = "STK"
        contract.exchange = "SMART"
        contract.currency = "USD"

        order = Order()
        order.action = "BUY"
        order.orderType = "LMT"
        order.lmtPrice = 144.80
        order.totalQuantity = 10
        # The following two lines get rid of EtradeOnly errors:
        order.eTradeOnly = ''
        order.firmQuoteOnly = ''

        self.placeOrder(self.start_order_id, contract, order)
        self.start_order_id += 1

    def orderStatus(self, orderId, status, filled, remaining, avgFillPrice, permId, parentId, lastFillPrice, clientId, whyHeld, mktCapPrice):
        print(f"Order Status - Id: {orderId}, Status: {status}, Filled: {filled}, Remaining: {remaining}, Last Fill Price: {lastFillPrice}")

    def openOrder(self, orderId, contract, order, orderState):
        print(f"Open Order - Id: {orderId}, Contract: {contract}, Order: {order}")

# Main function
def main():
    app = TestApp()
    app.connect("127.0.0.1", 7497, clientId=100)
    app.run()

if __name__ == "__main__":
    main()