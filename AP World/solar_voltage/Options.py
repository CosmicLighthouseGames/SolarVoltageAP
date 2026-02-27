from dataclasses import dataclass

from Options import Toggle, Choice, Range, PerGameCommonOptions


class GemCount(Range):
    """The number of power cells required to beat the game"""
    display_name = "Power Cell Requirement"
    range_start = 1
    range_end = 52
    default = 25
    
class GemMax(Range):
    """The total number of power cells"""
    display_name = "Power Cell Total"
    range_start = 1
    range_end = 52
    default = 52

@dataclass
class SolarVoltageOptions(PerGameCommonOptions):
    gem_required: GemCount
    gem_max: GemMax

slot_data_options: list[str] = [
    "gem_required",
    "gem_max",
]
