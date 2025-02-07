from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass
    
class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount=999):
        print(f"Processing payment of ${amount} using {self.__class__.__name__}")
        
class StripeProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing payment of ${amount} using {self.__class__.__name__}")

paypal_processor = PayPalProcessor()
stripe_processor = StripeProcessor()

def function_call(obj):
    if isinstance(obj, PayPalProcessor):
        obj.process_payment()
        return
    obj.process_payment(1000)

for processor in [paypal_processor, stripe_processor]:
    function_call(processor)
