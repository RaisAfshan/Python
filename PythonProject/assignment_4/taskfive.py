class Currency():
    @staticmethod
    def convert_to_usd(rs):
        result = rs/82
        print("inr to usd = ",result)

obj = Currency()
obj.convert_to_usd(1000)
