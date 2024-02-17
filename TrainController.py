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

    def add_train(self, name, source_station, destination_station, departure_time, arrival_time, capacity, available_seats, fare_per_km):
        train_id = len(self.train_list) + 1
        train = Train(train_id, name, source_station, destination_station, departure_time, arrival_time, capacity, available_seats, fare_per_km)

        self.train_list.append(train)

    def update_train_details(self, train_id, name, source_station, destination_station, departure_time, arrival_time, capacity, available_seats, fare_per_km):
        for train in self.train_list:
            if train.train_id == train_id:
                train.name = name
                train.source_station = source_station
                train.destination_station = destination_station
                train.departure_time = departure_time
                train.arrival_time = arrival_time
                train.capacity = capacity
                train.available_seats = available_seats
                train.fare_per_km = fare_per_km
                break

    def delete_train(self, train_id):
        for train in self.train_list:
            if train.train_id == train_id:
                self.train_list.remove(train)
                break
