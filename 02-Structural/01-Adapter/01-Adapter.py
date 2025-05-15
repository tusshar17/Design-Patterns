"""
app expects a pay() method, but a third-party Stripe library uses make_payment() instead
"""


# Target interfacce (what app expects)
class PaymentProcessor:
    def pay(self, amount: float):
        raise NotImplementedError


# Incompatible class (third-party)
class StripeAPI:
    def make_payment(self, amount_in_cents: int):
        print(f"Paid {amount_in_cents} cents using Stripe")


# Adapter class
class StripeAdapter(PaymentProcessor):
    def __init__(self, stripe_api: StripeAPI):
        self.stripe_api = stripe_api

    def pay(self, amount: float):
        cents = int(amount * 100)
        self.stripe_api.make_payment(cents)


# Client code using the adapter
def checkout(processor: PaymentProcessor):
    processor.pay(29.99)


stripe_api = StripeAPI()
adapter = StripeAdapter(stripe_api)
checkout(adapter)
