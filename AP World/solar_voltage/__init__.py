from typing import Dict, Any
from BaseClasses import ItemClassification, Region
from worlds.AutoWorld import World

from .Items import SolarVoltageItem, base_items, filler_items, item_dict, item_alias_list
from .Locations import location_dict, tagged_locations_dict
from .Options import SolarVoltageOptions, slot_data_options
from .Rules import apply_location_rules, apply_connection_rules
from .Regions import region_list
from ..generic.Rules import add_item_rule


class SolarVoltageWorld(World):

    """Solar Voltage's official Archipelago world"""
    game = "Solar Voltage"
    options_dataclass = SolarVoltageOptions
    options: SolarVoltageOptions
    topology_present = True
    # TODO: Determine if this is a good number to use
    base_id = 198436
    item_name_to_id = {name: id for id, name in enumerate(item_dict, base_id)}
    location_name_to_id = {name: id for id, name in enumerate(location_dict, base_id)}
    item_name_groups = item_alias_list
    location_name_groups = {location: set(tags) for location, tags in tagged_locations_dict.items()}

    def generate_early(self):
        self.logic_sets: set[str] = {"casual"} # always include at least casual
        self.location_exclusion_list: list[str] = []


    def create_region(self, name: str):
        return Region(name, self.player, self.multiworld)

    def create_regions(self) -> None:
        
        menu = self.create_region("Menu")
        self.multiworld.regions.append(menu)

        for region_name in region_list:
            region = self.create_region(region_name)
            self.multiworld.regions.append(region)

            if region_name == "vanilla/newhub/center":
                menu.connect(region)

        apply_connection_rules(self)
        apply_location_rules(self)

    def restrict_item(self, tag: str, item_name: str):
        for location in tagged_locations_dict[tag]:
            if location not in self.location_exclusion_list:
                add_item_rule(self.get_location(location), lambda item: item.name != item_name)

    def create_item(self, name: str) -> SolarVoltageItem:
        return SolarVoltageItem(name, item_dict[name][0], self.item_name_to_id[name], self.player)

    def create_items(self) -> None:

        item_list = dict(base_items)
        item_count = 0

        for item_key, item_value in item_list.items():
            # override the item values for counts that come from options

            for count in range(item_value[1]):
                item = self.create_item(item_key)

                self.multiworld.itempool.append(item)
                item_count += 1

        unfilled_locations = len(self.multiworld.get_unfilled_locations(self.player))
        self.multiworld.itempool += [self.create_filler() for _ in range(unfilled_locations - item_count)]

    def create_event(self, event: str) -> SolarVoltageItem:
        return SolarVoltageItem(event, ItemClassification.progression, None, self.player)

    def set_rules(self) -> None:
        
        
        self.multiworld.completion_condition[self.player] = lambda state: \
            state.has("MainGem", self.player, self.options.gem_required.value)


    def fill_slot_data(self) -> Dict[str, Any]:
        slot_data: Dict[str, Any] = {}

        for option_name, option_value in self.options.as_dict(*slot_data_options).items():
            slot_data[option_name] = option_value

        return slot_data

    def get_filler_item_name(self) -> str:
        total = sum([item[1] for item in filler_items.values()])
        weights = [item[1] / total for item in filler_items.values()]
        return self.random.choices(list(filler_items.keys()), weights)[0]