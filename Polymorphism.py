class Batangas:
    def touristspot(self):
        print('Taal Volcano')
    
    def famousfood(self):
        print('Loming Batangas')
    
class Laguna:
    def touristspot(self):
        print('Jose Rizal Shrine')

    def famousfood(self):
        print('Bibingka de Macapuno')

obj_bats = Batangas()
obj_Lag = Laguna()
for province in (obj_bats, obj_Lag):
    province.touristspot()
    province.famousfood()
    