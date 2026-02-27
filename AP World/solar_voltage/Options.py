from dataclasses import dataclass

from Options import Toggle, Choice, Range, PerGameCommonOptions


class GemCount(Range):
    """The number of power cells required to beat the game"""
    display_name = "Power Cell Requirement"
    range_start = 1
    range_end = 50
    default = 25
    
class GemMax(Range):
    """The total number of power cells"""
    display_name = "Power Cell Total"
    range_start = 1
    range_end = 50
    default = 50

class TutorialUnlock(Range):
    """Number of power cells required to unlock the tutorial area"""
    display_name = "Tutorial Access"
    range_start = 0
    range_end = 50
    default = 50

class SnowUnlock(Range):
    """Number of power cells required to unlock the snow area"""
    display_name = "Snow Access"
    range_start = 0
    range_end = 50
    default = 50

class DesertUnlock(Range):
    """Number of power cells required to unlock the desert area"""
    display_name = "Desert Access"
    range_start = 0
    range_end = 50
    default = 50

class DarkUnlock(Range):
    """Number of power cells required to unlock the dark area"""
    display_name = "Dark Access"
    range_start = 0
    range_end = 50
    default = 50

class RandomizeMechanics(Range):
    """Choose how to randomize level mechanics
    None: All mechanics are enabled by default.
    Normal: Mechanics must be unlocked through items."""
    display_name = "Randomize Level Mechanics"
    option_none = 0
    option_normal = 1
    default = 0

class RandomizeAbilities(Choice):
    """Number of power cells required to unlock the dark area
    None: All abilities are enabled by default.
    Normal: Volt's basic moveset is locked behind items.
    Advanced: Volt's basic and advanced moveset is locked behind items."""
    display_name = "Randomize Volt Abilities"
    option_none = 0
    option_normal = 1
    option_advanced = 2
    default = 0

@dataclass
class SolarVoltageOptions(PerGameCommonOptions):
    gem_required: GemCount
    gem_max: GemMax
    tutorial_unlock: TutorialUnlock
    snow_unlock: SnowUnlock
    desert_unlock: DesertUnlock
    dark_unlock: DarkUnlock
    randomize_mechanics: RandomizeMechanics
    randomize_abilities: RandomizeAbilities

slot_data_options: list[str] = [
    "gem_required",
    "gem_max",
    "tutorial_unlock",
    "snow_unlock",
    "desert_unlock",
    "dark_unlock",
    "randomize_mechanics",
    "randomize_abilities",
]
