class Train:
    def __init__(self, train_id, name, source_station, destination_station, departure_time, arrival_time, capacity, available_seats, fare_per_km):
        self.train_id = train_id
        self.name = name
        self.source_station = source_station
        self.destination_station = destination_station
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.capacity = capacity
        self.available_seats = available_seats
        self.fare_per_km = fare_per_km

class TrainController:
    def __init__(self):
        self.train_list = []

    def get_train_details(self, train_id):
        for train in self.train_list:
            if train.train_id == train_id:
                return train

        return None

    def search_trains(self, source_station, destination_station):
        matching_trains = []
        for train in self.train_list:
            if train.source_station == source_station and train.destination_station == destination_station:
                matching_trains.append(train)

        return matching_trains
