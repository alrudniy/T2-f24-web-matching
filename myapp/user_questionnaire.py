from enum import Enum

class TenantPreferences:
    class preferences(Enum):        # Enum class that determines if the user has a preference for a certain feature
        floorType = False   # like wood, carpet, tile, plastic hahahahaha
        buildingAesthetic = False   # like modern, rustic, etc
        balcony = False 
        floorNum = False    # do they want to be high up in a building or low if that makes any sense
        wheelchairAccess = False
        reqOneFloor = False     # tenant can only access one floor
        petFriendly = False
        parking = False     # need an accessible parking spot??
        lotSize = False
        lotCost = False
        distFromPol = False    # distance from police station
        distFromFire = False    # distance from fire station
        distFromGrocery = False    # distance from grocery store
        distFromSchool = False    # distance from school
        distFromHospital = False    # distance from hospital
        distFromPark = False    # distance from park
        distFromTrain = False    # distance from train station
        distFromBus = False    # distance from bus stop
        internetAccess = False  # how accessible or efficient the internet is??
        bedroomNum = False
        bathroomNum = False

        