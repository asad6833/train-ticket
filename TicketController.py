from typing import List
class Ticket:
    def __init__(self, ticket_id, train_id, user_id, source_station, destination_station, departure_time, arrival_time, fare, status):
        self.ticket_id = ticket_id
        self.train_id = train_id
        self.user_id = user_id
        self.source_station = source_station
        self.destination_station = destination_station
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.fare = fare
        self.status = status
class TicketController:
    def __init__(self):
        self.ticket_list = []

    def book_ticket(self, train_id: int, user_id: int, source_station: str, destination_station: str) -> bool:
        # Assume that we have some function to check availability of the train and seat availability
        # If the seat is available, book the ticket and return True, otherwise return False
        ticket_id = len(self.ticket_list) + 1  # Unique ticket ID
        departure_time = get_departure_time(train_id, source_station)  # Assume this function returns a datetime object
        arrival_time = get_arrival_time(train_id, destination_station)  # Assume this function returns a datetime object
        fare = calculate_fare(train_id, source_station, destination_station)  # Assume this function returns a float
        ticket = Ticket(ticket_id, train_id, user_id, source_station, destination_station, departure_time, arrival_time, fare, "booked")
        self.ticket_list.append(ticket)
        return True

    def cancel_ticket(self, ticket_id: int) -> bool:
        for ticket in self.ticket_list:
            if ticket.ticket_id == ticket_id:
                ticket.status = "cancelled"
                return True
        return False

    def get_ticket_details(self, ticket_id: int) -> Ticket:
        for ticket in self.ticket_list:
            if ticket.ticket_id == ticket_id:
                return ticket
        return None

    def get_all_tickets(self, user_id: int) -> List[Ticket]:
        user_tickets = []
        for ticket in self.ticket_list:
            if ticket.user_id == user_id:
                user_tickets.append(ticket)
        return user_tickets
import datetime

def get_departure_time(train_id: int, source_station: str) -> datetime.datetime:
    # Assuming we have a database or API to retrieve train schedules, we can query the departure time of the given train and station.
    # Here's an example implementation:
    departure_time = datetime.datetime(2023, 5, 1, 10, 30) # Assuming departure time of the given train and station is 2023-05-01 10:30 AM
    return departure_time

def get_arrival_time(train_id: int, destination_station: str) -> datetime.datetime:
    # Assuming we have a database or API to retrieve train schedules, we can query the arrival time of the given train and station.
    # Here's an example implementation:
    arrival_time = datetime.datetime(2023, 5, 1, 14, 0) # Assuming arrival time of the given train and station is 2023-05-01 02:00 PM
    return arrival_time

def calculate_fare(train_id: int, source_station: str, destination_station: str) -> float:
    # Assuming we have a fare chart for the given train and stations, we can calculate the fare based on the distance between the stations.
    # Here's an example implementation:
    distance = 500 # Assuming the distance between the stations is 500 km
    fare_per_km = 2.5 # Assuming the fare per km is 2.5 rupees
    fare = distance * fare_per_km
    return fare
