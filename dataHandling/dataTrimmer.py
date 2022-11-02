import os
import json

card_url = "https://web.poecdn.com/image/divination-card/"

def trim_data():
    all_files = [e for e in os.listdir("RawData") if e not in ("curr.json", "frag.json")]
    for file in all_files:
        f = open("RawData/"+file)
        trimmed_f = open("TrimmedData/"+file, "w")
        data = json.load(f)
        trimmed_data = {}
        for item in data["lines"]:
            name = item["name"]
            variant = "Base"

            if item["itemClass"] == 9:
                variant = "Foil"
            if "links" in item:
                variant = str(item["links"]) + " Link"
            if "variant" in item:
                if (file != "blighted.json") and (file != "ravaged.json"):
                    variant = variant + " " + item["variant"]

            if file == "cluster.json":
                variant = variant[5:] + " ilvl " + str(item["levelRequired"])

            if name not in trimmed_data:
                trimmed_data[name] = {}

            trimmed_data[name]["name"] = name
            trimmed_data[name]["icon"] = item["icon"]
            trimmed_data[name]["rarity"] = item["itemClass"]

            if file == "card.json":
                trimmed_data[name]["icon"] = card_url + item["artFilename"] + ".png"

            if "chaosValue" not in trimmed_data[name]:
                trimmed_data[name]["chaosValue"] = {}
            if "exaltedValue" not in trimmed_data[name]:
                trimmed_data[name]["exaltedValue"] = {}
            if "divineValue" not in trimmed_data[name]:
                trimmed_data[name]["divineValue"] = {}

            trimmed_data[name]["chaosValue"][variant] = item["chaosValue"]
            trimmed_data[name]["exaltedValue"][variant] = item["exaltedValue"]
            trimmed_data[name]["divineValue"][variant] = item["divineValue"]

        trimmed_f.write(json.dumps(trimmed_data, indent=2))
        trimmed_f.close()
        f.close()


def trim_currency():
    currency_data = ("curr.json", "frag.json")
    trimmed_currency = {}
    trimmed_currency_f = open("TrimmedData/currency.json", "w")
    for file in currency_data:
        f = open("RawData/"+file)
        data = json.load(f)

        for currency in data["lines"]:
            name = currency["currencyTypeName"]
            if name not in trimmed_currency:
                trimmed_currency[name] = {}
            trimmed_currency[name]["name"] = name
            if "chaosValue" not in trimmed_currency[name]:
                trimmed_currency[name]["chaosValue"] = {}
            if "pay" not in currency:
                trimmed_currency[name]["chaosValue"]["buy"] = 0
            else:
                trimmed_currency[name]["chaosValue"]["buy"] = 1/currency["pay"]["value"]
            if "receive" not in currency:
                trimmed_currency[name]["chaosValue"]["sell"] = 0
            else:
                trimmed_currency[name]["chaosValue"]["sell"] = currency["receive"]["value"]

        for currency_icon in data["currencyDetails"]:
            name = currency_icon["name"]
            if name == "Chaos Orb":
                continue
            if name not in trimmed_currency:
                continue
            if "icon" in currency_icon:
                trimmed_currency[name]["icon"] = currency_icon["icon"]
            else:
                trimmed_currency[name]["icon"] = None
        f.close()

    trimmed_currency_f.write(json.dumps(trimmed_currency, indent=2))
    trimmed_currency_f.close()


trim_data()
trim_currency()
