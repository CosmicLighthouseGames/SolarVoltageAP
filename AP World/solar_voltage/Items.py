from BaseClasses import Item, ItemClassification


class SolarVoltageItem(Item):
    game: str = "Solar Voltage"


base_items = {
    "MainGem": (ItemClassification.progression, 52),
}

filler_items = {
    # since filler is added dynamically at the end of item generation, the numbers here don't correspond
    # with how many are in the multiworld. Rather they are weights relative to each other
    "Dust": (ItemClassification.filler, 1),
    "Coins1": (ItemClassification.filler, 5),
    "Coins10": (ItemClassification.filler, 20),
    "Coins25": (ItemClassification.filler, 10),
    "Coins50": (ItemClassification.filler, 5),
}

item_dict = {
    **base_items,
    **filler_items
}

item_alias_list = {
    "MainGem": {"PowerCell"},
}