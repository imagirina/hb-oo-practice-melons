############
# Part 1   #
############

class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""

        self.pairings = []

        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name


    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code
    
    def print_pairing_info(self):
        if len(self.pairings) > 0:
            print(f"{self.name} pairs well with ")
            for pairing in self.pairings:
                print(f"- {pairing}") 
        else:
            print(f"{self.name} doesn't pair with anything")

    def __repr__(self):
        return f"MelonType name={self.name} code={self.code} first_harvest={self.first_harvest}"


# Function instantiates the class MelonType for each of the above melon types.
def make_melon_types(): 
    """Returns a list of objects (current melon types)."""

    all_melon_types = []

    muskmelon = MelonType("musk", 1998, "green", True, True, "Muskmelon")
    muskmelon.add_pairing("mint")
    all_melon_types.append(muskmelon)

    casabamelon = MelonType("cas", 2003, "orange", True, None, "Casaba")
    casabamelon.add_pairing("strawberries")
    casabamelon.add_pairing("mint")
    all_melon_types.append(casabamelon)

    crenmelon = MelonType("cren", 1996, "green", True, None, "Crenshaw")
    crenmelon.add_pairing("prosciutto")
    all_melon_types.append(crenmelon)

    yelmelon = MelonType("yw", 2013, "yellow", True, None, "Yellow Watermelon")
    yelmelon.add_pairing("ice cream")
    all_melon_types.append(yelmelon)

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    for melon_type in melon_types:
        melon_type.print_pairing_info()
        # print(f"{melon_type.name} pairs well with ")
        # for pairing in melon_type.pairings:
            # print(f"- {pairing}")         
    

# This function should return a dictionary whose keys are reporting codes (as strings) and whose values are the appropriate melon type instance for that reporting code.
# Takes in a list of MelonType objects as an argument
def make_melon_type_lookup(melon_types): 
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_types_by_code = {}
    for melon_type in melon_types:
        if melon_type.code not in melon_types_by_code:
            melon_types_by_code[melon_type.code] = melon_type
    
    return melon_types_by_code


############
# Part 2   #
############


# The first argument to the __init__ function would be the MelonType instance that represents the Yellow Watermelon melon type.
class Melon:
    """A melon in a melon harvest."""    
    def __init__(self, type, shape_rating, color_rating, field, harvested_by):
        self.type = type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvested_by = harvested_by

    def is_sellable(self):
        return self.shape_rating > 5 and self.color_rating > 5 and self.field != 3


# The melon_type attribute should be the actual instance of the MelonType class from Part 1. In order to make this work, you’ll need to add a parameter to your function which is melon_types– the list of MelonType instance that you created in part 1.
# Function instantiates the class Melon for each of the above melons.
def make_melons(melon_types): 
    """Returns a list of Melon objects."""
    
    melons = []

    melon_types_by_code = make_melon_type_lookup(melon_types)

    # print(f"melon_types_by_code: {melon_types_by_code}")

    # for mt in melon_types:    
    #     if mt.code == "yw":
    #         melon1 = Melon(mt, 8, 7, 2, "Sheila")
    #         melons.append(melon1)
    #     elif mt.code == "cas":
    #         melon4 = Melon(mt, 10, 6, 35, "Sheila")
    #         melons.append(melon4)

    melons.append(Melon(melon_types_by_code["yw"], 8, 7, 2, "Sheila"))
    melons.append(Melon(melon_types_by_code["yw"], 3, 4, 2, "Sheila"))
    melons.append(Melon(melon_types_by_code["yw"], 9, 8, 3, "Sheila"))
    melons.append(Melon(melon_types_by_code["cas"], 10, 6, 35, "Sheila"))
    melons.append(Melon(melon_types_by_code["cren"], 8, 9, 35, "Michael"))
    melons.append(Melon(melon_types_by_code["cren"], 8, 2, 35, "Michael"))
    melons.append(Melon(melon_types_by_code["cren"], 2, 3, 4, "Michael"))
    melons.append(Melon(melon_types_by_code["musk"], 6, 7, 4, "Michael"))
    melons.append(Melon(melon_types_by_code["yw"], 7, 10, 3, "Sheila"))

    return melons

# Function takes a list of melon instances as an argument
def get_sellability_report(melons): 
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        print(f"Harvested by {melon.harvested_by} from Field {melon.field} ", end ="")
        if melon.is_sellable():
            print("(CAN BE SOLD)")
        else:
            print("NOT SELLABLE")


# print("Melon Types:")
melon_types = make_melon_types()
# print(melon_types)

# print("Melons:")
melons = make_melons(melon_types)
# print(melons)

get_sellability_report(melons)