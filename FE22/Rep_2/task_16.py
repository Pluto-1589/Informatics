class Airplane():

    def __init__(self, model: str, plane_id: str):
        self.model = model
        self.plane_id = plane_id

    def board(self):
        pass

    def get_passengers(self):
        pass

    def parse_manifest(self, manifest):
        pass


passengers = Airplane.parse_manifest(
    ("Montgomery,Rich,1;Tim,Merchant,2;Sally,Sale,2;Peter,Poor,3"))
a = Airplane("A388", "G-XLEK")
a.board(passengers)
print(a.get_passengers())
p = a.get_passengers(2)
print(type(p[1]))
print(p[1])

# [Montgomery Rich, 1st class, Tim Merchant, business class, Sally Sale, business class, Peter Poor, economy class]
# <class '__main__.Passenger'>
# Sally Sale, business class
