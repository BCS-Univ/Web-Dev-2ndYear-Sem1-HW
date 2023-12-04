import json

class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price
    
    def to_dict(self):
        return {"name": self.name, "engine": self.engine, "price": self.price}

vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)

vehicle_json = json.dumps(vehicle.to_dict())

print(vehicle_json)
