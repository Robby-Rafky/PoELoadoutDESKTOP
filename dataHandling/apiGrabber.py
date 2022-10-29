import requests
import json

HEADERS = {"content-type": "PoE_Loadout_Tool/0.1"}
current_league = "Kalandra"
api_url = {
    "curr": "https://poe.ninja/api/data/CurrencyOverview?league="+current_league+"&type=Currency",
    "frag": "https://poe.ninja/api/data/CurrencyOverview?league="+current_league+"&type=Fragment&language=en",
    "arti": "https://poe.ninja/api/data/ItemOverview?league="+current_league+"&type=Artifact&language=en",
    "oil": "https://poe.ninja/api/data/ItemOverview?league="+current_league+"&type=Oil&language=en",
    "wep": "https://poe.ninja/api/data/ItemOverview?league="+current_league+"&type=UniqueWeapon&language=en",
    "armour": "https://poe.ninja/api/data/ItemOverview?league="+current_league+"&type=UniqueArmour&language=en",
    "accessory": "https://poe.ninja/api/data/ItemOverview?league="+current_league+"&type=UniqueAccessory&language=en",
    "jewel": "https://poe.ninja/api/data/ItemOverview?league="+current_league+"&type=UniqueJewel&language=en",
    "cluster": "https://poe.ninja/api/data/ItemOverview?league="+current_league+"&type=ClusterJewel&language=en",
    "blighted": "https://poe.ninja/api/data/ItemOverview?league="+current_league+"&type=BlightedMap&language=en",
    "ravaged": "https://poe.ninja/api/data/ItemOverview?league="+current_league+"&type=BlightRavagedMap&language=en",
    "deli": "https://poe.ninja/api/data/ItemOverview?league="+current_league+"&type=DeliriumOrb&language=en",
    "scarab": "https://poe.ninja/api/data/ItemOverview?league="+current_league+"&type=Scarab&language=en",
    "fossil": "https://poe.ninja/api/data/ItemOverview?league="+current_league+"&type=Fossil&language=en",
    "reso": "https://poe.ninja/api/data/ItemOverview?league="+current_league+"&type=Resonator&language=en",
    "essence": "https://poe.ninja/api/data/ItemOverview?league="+current_league+"&type=Essence&language=en",
    "beast": "https://poe.ninja/api/data/ItemOverview?league="+current_league+"&type=Beast&language=en",
    "card": "https://poe.ninja/api/data/ItemOverview?league="+current_league+"&type=DivinationCard&language=en"
}


def update_prices():
    for item in api_url:
        response = requests.get(api_url[item], headers=HEADERS)
        data = response.json()
        f = open("RawData/"+item+".json", "w")
        f.write(json.dumps(data, indent=2))
        f.close()


update_prices()
