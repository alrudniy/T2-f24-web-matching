

class TenantPreferences:    # Determines user preference; 0 means no preference; also idk why it's making me format it this way
    buildingAesthetic = [int modern = 0, rustic = 0, traditional = 0, minimalist = 0]   # like modern, rustic, etc
    balcony: int = 0 
    floorNum = [int low = 0, middle = 0, high = 0]    # do they want to be high up in a building or low if that makes any sense
    wheelchairAccess: int = 0
    reqOneFloor: int = 0     # tenant can only access one floor
    petFriendly: int = 0
    parking: int = 0     # need an accessible parking spot??
    lotSize = [int small = 0, medium = 0, large = 0]    # how big of a lot do they want
    lotCost = [int low = 0, medium = 0, high = 0]    # how much are they willing to pay for a lot
    closeToPol: int = 0   # distance from police station
    closeToFire: int = 0    # distance from fire station
    closeToGrocery: int = 0    # distance from grocery store
    closeToSchool: int = 0    # distance from school
    closeToHospital: int = 0    # distance from hospital
    closeToPark: int = 0    # distance from park
    closeToTrain: int = 0    # distance from train station
    closeToBus: int = 0    # distance from bus stop
    internetAccess: int = 0  # how accessible or efficient the internet is??
    bedroomNum = [int one = 0, two = 0, threeOrMore = 0]
    bathroomNum: [int one = 0, two = 0, threeOrMore = 0]

    # I feel it would be a good idea to categorize these different preferences for easier access - basic house features, accessibility, and location
    print("Basic house information\n\n")
    print("Please select what your preferences are. If you have no preference, choose 'no preference'.")    # Will probably be in the form of buttons. For now just type.