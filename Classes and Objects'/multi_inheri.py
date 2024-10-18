class Country:
    countryname = ""

    def country(self):
        print(self.countryname)

class State:
    statename = ""

    def state(self):
        print(self.statename)

class City(Country, State):
    def address(self):
        print("Country:", self.countryname)
        print("State:", self.statename)

s1 = City()
s1.countryname = "India"
s1.statename = "Karnataka"
s1.address()