class PaymentGateway:
    def __init__(self, merchant_id, merchant_key):
        self.merchant_id = merchant_id
        self.merchant_key = merchant_key

    def initiate_payment(self, amount):
        transaction_id = str(uuid.uuid4())
        return transaction_id

    def process_payment(self, transaction_id, amount, card_number, card_expiry, cvv):
        authenticated = self.authenticate()

        if not authenticated:
            return False

        result = self.gateway_process_payment(transaction_id, amount, card_number, card_expiry, cvv)

        return result

    def authenticate(self):
        return True

    def gateway_process_payment(self, transaction_id, amount, card_number, card_expiry, cvv):
        return True
