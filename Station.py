class Station:
    def __init__(self, station_id,name, code, address):
        self.station_id = station_id
        self.name = name
        self.code = code
        self.address = address

    def get_station(self):
        return self.station_id
    def get_name(self):
        return self.name
    def get_code(self):
        return self.code
    def get_address(self):
        return self.address

    def set_station(self, station_id):
        self.station_id = station_id
    def set_name(self, name):
        self.name = name
    def set_code(self, code):
        self.code = code
    def set_address(self, address):
        self.address = address
        
    def to_dict(self):
        return {
            "station_id": self.username,
            "name": self.name,
            "code": self.code,
            "address": self.address,
        }
