from typing import Set, cast

from .RulesData import location_rules
from .RulesData import connection_rules
from .Items import SolarVoltageItem, item_dict
from .Locations import SolarVoltageLocation, tagged_locations_dict
from .Options import SolarVoltageOptions
from BaseClasses import CollectionState, Location, Entrance, ItemClassification, Region
from ..AutoWorld import World
from ..generic.Rules import add_rule, set_rule


def apply_location_rules(world: World):
    # for each region in location rules, and for each location
    # create a location and call process_access_point
    for region_name, locations in location_rules.items():
        region = world.get_region(region_name)
        valid_location_ids: dict[str, int | None] = get_location_ids(world, list(locations.keys()))
        region.add_locations(valid_location_ids, SolarVoltageLocation)

        for location, rulesets in locations.items():
            if location in valid_location_ids.keys():
                process_access_point(world, world.get_location(location), rulesets)


def get_location_ids(world: World, locations: list[str]) -> dict[str, int | None]:
    # get the ids for each location in the list as long as they aren't excluded
    # if the location is an event, create it with a None id
    # otherwise add its id from the name_to_id list
    ids: dict[str, int | None] = {}
    for location in locations:
        if location not in world.location_exclusion_list:
            ids[location] = world.location_name_to_id[location]

    return ids


def apply_connection_rules(world: World):
    # for each region in connection rules, and for each connecting region, 
    # create an entrance and call process_access_point
    for region_name, connections in connection_rules.items():
        region = world.get_region(region_name)
        id = 1
        for connection, rulesets in connections.items():
            entrance_name = region_name + "_to_" + connection + "_" + str(id)
            id += 1
            region.connect(world.get_region(connection), entrance_name)
            access_point = world.get_entrance(entrance_name)
            process_access_point(world, access_point, rulesets)


def process_access_point(world: World, access_point: Location | Entrance, rulesets: dict[str, list[list[str | tuple[str, int]]]]):
    # preface with a false so all other rules can be combined with OR
    set_rule(access_point, lambda state: False)

    # for each ruleset in the location/entrance, call process_ruleset
    for ruleset_name, ruleset in rulesets.items():
        if ruleset_name in world.logic_sets:
            process_ruleset(world, access_point, ruleset)


def process_ruleset(world: World, access_point: Location | Entrance, ruleset: list[list[str | tuple[str, int]]]):
    # for each access set in the ruleset, call process_access_set
    for access_set in ruleset:
        process_access_set(world, access_point, access_set)

def process_access_set(world: World, access_point: Location | Entrance, access_set: list[str | tuple[str, int]]):
    # add the rule for the access set list using solarvoltage_has
    # this line needs to be in a separate function from the previous for loop in order to work properly 
    # (likely lambda function strangeness)
    add_rule(access_point, lambda state: all(solarvoltage_has(world, state, item) for item in access_set), "or")
            
    
def solarvoltage_has(world: World, state: CollectionState, item: str | tuple[str, int]) -> bool:
    options: SolarVoltageOptions = cast(SolarVoltageOptions, world.options)

    if type(item) == str:
        if item in item_dict.keys():
            # handles normal abilities like Dash, Climb, Wind, etc.
            return state.has(item, world.player)
        
        elif item == "Free":
            return True
        
        else:
            return False
    else:
        return state.has(item[0], world.player, int(item[1]))

    return False


def solarvoltage_has_all(state: CollectionState, items: Set[str], player: int) -> bool:
    return all(state.has(item, player) if type(item) == str else state.has(item[0], player, int(item[1]))
               for item in items)


def at_least(conditions: list[bool], amount: int) -> bool:
    count: int = 0
    for flag in conditions:
        if flag:
            count += 1
    return count >= amount                                 