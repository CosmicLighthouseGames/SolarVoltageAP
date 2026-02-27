from BaseClasses import Location


class SolarVoltageLocation(Location):
    game: str = "Solar Voltage"


location_dict: dict[str, list[str]] = {
	"MainGem/108.70/vanilla/newhub/tutorial2": ["MainGem", "vanilla/newhub/tutorial2"],
	"MainGem/19.29/vanilla/newhub/tutorial2": ["MainGem", "vanilla/newhub/tutorial2"],
	"MainGem/97.53/vanilla/newhub/tutorial2": ["MainGem", "vanilla/newhub/tutorial2"],
	"MainGem/34.18/vanilla/newhub/tutorial2": ["MainGem", "vanilla/newhub/tutorial2"],
	"MainGem/114.161/vanilla/snow0": ["MainGem", "vanilla/snow0"],
	"RedCoin/13.84/vanilla/snow0": ["RedCoin", "vanilla/snow0"],
	"MainGem/145.131/vanilla/snow0": ["MainGem", "vanilla/snow0"],
	"RedCoin/81.162/vanilla/snow0": ["RedCoin", "vanilla/snow0"],
	"MainGem/135.120/vanilla/snow0": ["MainGem", "vanilla/snow0"],
	"MainGem/10.111/vanilla/snow0": ["MainGem", "vanilla/snow0"],
	"RedCoin/108.208/vanilla/snow0": ["RedCoin", "vanilla/snow0"],
	"CoinGem/vanilla/snow0": ["CoinGem", "vanilla/snow0"],
	"ArchipelagoExtra/32.62/vanilla/snow0__1": ["ArchipelagoExtra", "vanilla/snow0__1"],
	"RedCoin/150.38/vanilla/snow1": ["RedCoin", "vanilla/snow1"],
	"MainGem/144.117/vanilla/snow1": ["MainGem", "vanilla/snow1"],
	"MainGem/59.35/vanilla/snow1": ["MainGem", "vanilla/snow1"],
	"RedCoin/66.35/vanilla/snow1": ["RedCoin", "vanilla/snow1"],
	"MainGem/72.45/vanilla/snow1": ["MainGem", "vanilla/snow1"],
	"RedCoin/95.156/vanilla/snow1": ["RedCoin", "vanilla/snow1"],
	"MainGem/61.94/vanilla/snow1": ["MainGem", "vanilla/snow1"],
	"CoinGem/vanilla/snow1": ["CoinGem", "vanilla/snow1"],
	"ArchipelagoExtra/25.18/vanilla/snow1__2": ["ArchipelagoExtra", "vanilla/snow1__2"],
	"MainGem/166.91/vanilla/snow2": ["MainGem", "vanilla/snow2"],
	"MainGem/58.102/vanilla/snow2": ["MainGem", "vanilla/snow2"],
	"RedCoin/197.41/vanilla/snow2": ["RedCoin", "vanilla/snow2"],
	"MainGem/69.21/vanilla/snow2": ["MainGem", "vanilla/snow2"],
	"RedCoin/119.73/vanilla/snow2": ["RedCoin", "vanilla/snow2"],
	"RedCoin/30.19/vanilla/snow2": ["RedCoin", "vanilla/snow2"],
	"MainGem/117.65/vanilla/snow2": ["MainGem", "vanilla/snow2"],
	"CoinGem/vanilla/snow2": ["CoinGem", "vanilla/snow2"],
	"ArchipelagoExtra/10.14/vanilla/snow2__3": ["ArchipelagoExtra", "vanilla/snow2__3"],
	"MainGem/122.105/vanilla/desert0": ["MainGem", "vanilla/desert0"],
	"RedCoin/131.87/vanilla/desert0": ["RedCoin", "vanilla/desert0"],
	"MainGem/37.72/vanilla/desert0": ["MainGem", "vanilla/desert0"],
	"RedCoin/23.4/vanilla/desert0": ["RedCoin", "vanilla/desert0"],
	"RedCoin/211.111/vanilla/desert0": ["RedCoin", "vanilla/desert0"],
	"MainGem/28.69/vanilla/desert0": ["MainGem", "vanilla/desert0"],
	"MainGem/137.33/vanilla/desert0": ["MainGem", "vanilla/desert0"],
	"CoinGem/vanilla/desert0": ["CoinGem", "vanilla/desert0"],
	"ArchipelagoExtra/20.20/vanilla/desert0__1": ["ArchipelagoExtra", "vanilla/desert0__1"],
	"MainGem/131.107/vanilla/desert1": ["MainGem", "vanilla/desert1"],
	"RedCoin/125.46/vanilla/desert1": ["RedCoin", "vanilla/desert1"],
	"RedCoin/67.19/vanilla/desert1": ["RedCoin", "vanilla/desert1"],
	"RedCoin/26.91/vanilla/desert1": ["RedCoin", "vanilla/desert1"],
	"MainGem/72.29/vanilla/desert1": ["MainGem", "vanilla/desert1"],
	"MainGem/50.73/vanilla/desert1": ["MainGem", "vanilla/desert1"],
	"MainGem/156.83/vanilla/desert1": ["MainGem", "vanilla/desert1"],
	"CoinGem/vanilla/desert1": ["CoinGem", "vanilla/desert1"],
	"ArchipelagoExtra/15.9/vanilla/desert1__2": ["ArchipelagoExtra", "vanilla/desert1__2"],
	"MainGem/97.77/vanilla/desert2": ["MainGem", "vanilla/desert2"],
	"MainGem/132.20/vanilla/desert2": ["MainGem", "vanilla/desert2"],
	"MainGem/44.105/vanilla/desert2": ["MainGem", "vanilla/desert2"],
	"MainGem/13.26/vanilla/desert2": ["MainGem", "vanilla/desert2"],
	"RedCoin/28.85/vanilla/desert2": ["RedCoin", "vanilla/desert2"],
	"RedCoin/44.145/vanilla/desert2": ["RedCoin", "vanilla/desert2"],
	"RedCoin/48.20/vanilla/desert2": ["RedCoin", "vanilla/desert2"],
	"CoinGem/vanilla/desert2": ["CoinGem", "vanilla/desert2"],
	"ArchipelagoExtra/28.38/vanilla/desert2__3": ["ArchipelagoExtra", "vanilla/desert2__3"],
	"MainGem/90.79/vanilla/computer0": ["MainGem", "vanilla/computer0"],
	"MainGem/25.21/vanilla/computer0": ["MainGem", "vanilla/computer0"],
	"MainGem/127.138/vanilla/computer0": ["MainGem", "vanilla/computer0"],
	"MainGem/103.22/vanilla/computer0": ["MainGem", "vanilla/computer0"],
	"RedCoin/43.115/vanilla/computer0": ["RedCoin", "vanilla/computer0"],
	"RedCoin/25.60/vanilla/computer0": ["RedCoin", "vanilla/computer0"],
	"RedCoin/14.76/vanilla/computer0": ["RedCoin", "vanilla/computer0"],
	"CoinGem/vanilla/computer0": ["CoinGem", "vanilla/computer0"],
	"ArchipelagoExtra/15.10/vanilla/computer0__1": ["ArchipelagoExtra", "vanilla/computer0__1"],
	"MainGem/60.79/vanilla/computer1": ["MainGem", "vanilla/computer1"],
	"RedCoin/97.66/vanilla/computer1": ["RedCoin", "vanilla/computer1"],
	"RedCoin/28.21/vanilla/computer1": ["RedCoin", "vanilla/computer1"],
	"RedCoin/34.140/vanilla/computer1": ["RedCoin", "vanilla/computer1"],
	"MainGem/49.128/vanilla/computer1": ["MainGem", "vanilla/computer1"],
	"MainGem/13.59/vanilla/computer1": ["MainGem", "vanilla/computer1"],
	"MainGem/91.108/vanilla/computer1": ["MainGem", "vanilla/computer1"],
	"ArchipelagoExtra/12.27/vanilla/computer1__2": ["ArchipelagoExtra", "vanilla/computer1__2"],


}

tagged_locations_dict : dict[str, list[str]] = {}

for location, tags in location_dict.items():
    for tag in tags:
        if tag in tagged_locations_dict.keys():
            tagged_locations_dict[tag].append(location)
        else:
            tagged_locations_dict[tag] = [location]
