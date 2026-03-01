from BaseClasses import Item, ItemClassification


class SolarVoltageItem(Item):
    game: str = "Solar Voltage"


base_items = {
    "Power Cell": (ItemClassification.progression, 100),
}

world_items = {
    "Snowballs": (ItemClassification.progression, 1),
    "Screws": (ItemClassification.progression, 1),
    "Launchers": (ItemClassification.progression, 1),
    "IceBerries": (ItemClassification.progression, 1),
    "Pipes": (ItemClassification.progression, 1),
    "ConveyorBelts": (ItemClassification.progression, 1),
    "Fans": (ItemClassification.progression, 1),
    "HoverPlatforms": (ItemClassification.progression, 1),
    "CrystalPedestals": (ItemClassification.progression, 1),
    "Slingshots": (ItemClassification.progression, 2), # Slingshots, then rotater
    "GlowCrystals": (ItemClassification.progression, 1),
    "CrystalLamps": (ItemClassification.progression, 1),
    "LightFlowers": (ItemClassification.progression, 1),
    "Teleporters": (ItemClassification.progression, 1),
}
ability_items = {
    "Roll": (ItemClassification.progression, 2), # Roll, then roll jump
    "Hover": (ItemClassification.progression, 1),
    "GroundPound": (ItemClassification.progression, 1),
    "Spin": (ItemClassification.progression, 1),
    "AirDive": (ItemClassification.progression, 1),
    "GrabbingItems": (ItemClassification.progression, 1),
}
ability_speedrun_items = {
    "WallJump": (ItemClassification.progression, 1),
    "SuperHover": (ItemClassification.progression, 1),
    "RollCancel": (ItemClassification.progression, 1),
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
}