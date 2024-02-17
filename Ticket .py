class Ticket:
    def __init__(self, ticket_id: int, train_id: int, user_id: int, source_station: str, destination_station: str,
                 departure_time: datetime, arrival_time: datetime, fare: float, status: str):
        self.ticket_id = ticket_id
        self.train_id = train_id
        self.user_id = user_id
        self.source_station = source_station
        self.destination_station = destination_station
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.fare = fare
        self.status = status

