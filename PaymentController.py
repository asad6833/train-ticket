class PaymentController:
    def __init__(self, payment_gateway):
        self.payment_gateway = payment_gateway

    def initiate_payment(self, ticket_id, user_id, fare):
        transaction_id = self.generate_transaction_id()

        return True

    def process_payment(self, user_id, transaction_id):

        return True

    def generate_transaction_id(self):
        transaction_id = str(uuid.uuid4())
        return transaction_id
