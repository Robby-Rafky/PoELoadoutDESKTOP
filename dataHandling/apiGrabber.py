import requests
import json

HEADERS = {"content-type": "PoE_Loadout_Tool/0.1"}
api_url = {
    "curr": "https://poe.ninja/api/data/CurrencyOverview?league=Sentinel&type=Currency",
    "frag": "https://poe.ninja/api/data/CurrencyOverview?league=Sentinel&type=Fragment&language=en",
    "arti": "https://poe.ninja/api/data/ItemOverview?league=Sentinel&type=Artifact&language=en",
    "oil": "https://poe.ninja/api/data/ItemOverview?league=Sentinel&type=Oil&language=en",
    "wep": "https://poe.ninja/api/data/ItemOverview?league=Sentinel&type=UniqueWeapon&language=en",
    "armour": "https://poe.ninja/api/data/ItemOverview?league=Sentinel&type=UniqueArmour&language=en",
    "accessory": "https://poe.ninja/api/data/ItemOverview?league=Sentinel&type=UniqueAccessory&language=en",
    "jewel": "https://poe.ninja/api/data/ItemOverview?league=Sentinel&type=UniqueJewel&language=en",
    "cluster": "https://poe.ninja/api/data/ItemOverview?league=Sentinel&type=ClusterJewel&language=en",
    "blighted": "https://poe.ninja/api/data/ItemOverview?league=Sentinel&type=BlightedMap&language=en",
    "ravaged": "https://poe.ninja/api/data/ItemOverview?league=Sentinel&type=BlightRavagedMap&language=en",
    "deli": "https://poe.ninja/api/data/ItemOverview?league=Sentinel&type=DeliriumOrb&language=en",
    "scarab": "https://poe.ninja/api/data/ItemOverview?league=Sentinel&type=Scarab&language=en",
    "fossil": "https://poe.ninja/api/data/ItemOverview?league=Sentinel&type=Fossil&language=en",
    "reso": "https://poe.ninja/api/data/ItemOverview?league=Sentinel&type=Resonator&language=en",
    "essence": "https://poe.ninja/api/data/ItemOverview?league=Sentinel&type=Essence&language=en",
    "beast": "https://poe.ninja/api/data/ItemOverview?league=Sentinel&type=Beast&language=en",
    "card": "https://poe.ninja/api/data/ItemOverview?league=Sentinel&type=DivinationCard&language=en"
}


def update_prices():
    for item in api_url:
        response = requests.get(api_url[item], headers=HEADERS)
        data = response.json()
        f = open("RawData/"+item+".json", "w")
        f.write(json.dumps(data, indent=2))
        f.close()


update_prices()
