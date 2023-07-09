import os
import json

card_url = "https://web.poecdn.com/image/divination-card/"


def trim_data():
    """Trims the raw item data and creates trimmed item and variant JSON files.

    The function reads the raw item data from the "RawData" directory, trims the data based on specific conditions,
    and creates two JSON files: "trimmedItems.json" containing the trimmed item data and
    "trimmedVariants.json" containing the variant data.
    """
    all_files = [e for e in os.listdir("RawData") if e not in ("curr.json", "frag.json")]
    trimmed_data = {}
    variant_data = {}
    trimmed_f = open("TrimmedData/trimmedItems.json", "w")
    variant_f = open("TrimmedData/trimmedVariants.json", "w")
    for file in all_files:
        f = open("RawData/"+file)
        data = json.load(f)
        for item in data["lines"]:
            name = item["name"]
            variant = "Base"

            if "links" in item:
                variant = str(item["links"]) + " Link "
            if "variant" in item:
                if (file != "blighted.json") and (file != "ravaged.json"):
                    variant = variant + item["variant"]

            if item["itemClass"] == 9:
                variant = "Foil" if variant == "Base" else "Foil " + variant

            if file == "cluster.json":
                variant = variant[4:] + ", item level (" + str(item["levelRequired"])+")"

            if name not in trimmed_data:
                trimmed_data[name] = {}

            variant_data[name] = {} if (not_present := name not in variant_data) else variant_data[name]

            if not_present or trimmed_data[name]["chaosValue"] > item["chaosValue"]:
                trimmed_data[name]["chaosValue"] = item["chaosValue"]
                trimmed_data[name]["exaltedValue"] = item["exaltedValue"]
                trimmed_data[name]["divineValue"] = item["divineValue"]

            if variant not in variant_data[name]:
                variant_data[name][variant] = {}

            variant_data[name][variant]["icon"] = item["icon"]
            variant_data[name][variant]["rarity"] = item["itemClass"]
            variant_data[name][variant]["chaosValue"] = item["chaosValue"]
            variant_data[name][variant]["exaltedValue"] = item["exaltedValue"]
            variant_data[name][variant]["divineValue"] = item["divineValue"]

            if file == "card.json":
                variant_data[name][variant]["icon"] = card_url + item["artFilename"] + ".png"

        f.close()
    trimmed_f.write(json.dumps(trimmed_data, indent=2))
    trimmed_f.close()
    variant_f.write(json.dumps(variant_data, indent=2))
    variant_f.close()


def trim_currency():
    """Trims the raw currency data and creates a trimmed currency JSON file.

    The function reads the raw currency data from the "RawData" directory, trims the data based on specific conditions,
    and creates a JSON file named "trimmedCurrency.json" containing the trimmed currency data.
    """
    currency_data = ("curr.json", "frag.json")
    trimmed_currency = {}
    trimmed_currency_f = open("TrimmedData/trimmedCurrency.json", "w")
    for file in currency_data:
        f = open("RawData/"+file)
        data = json.load(f)

        for currency in data["lines"]:
            name = currency["currencyTypeName"]
            if name not in trimmed_currency:
                trimmed_currency[name] = {}
            trimmed_currency[name]["chaosPay"] = 0 if "pay" not in currency else 1/currency["pay"]["value"]
            trimmed_currency[name]["chaosReceive"] = 0 if "receive" not in currency else currency["receive"]["value"]

        for currency_icon in data["currencyDetails"]:
            name = currency_icon["name"]
            if name == "Chaos Orb":
                continue
            if name not in trimmed_currency:
                continue
            trimmed_currency[name]["icon"] = currency_icon["icon"] if "icon" in currency_icon else None
        f.close()

    trimmed_currency_f.write(json.dumps(trimmed_currency, indent=2))
    trimmed_currency_f.close()


trim_data()
trim_currency()
