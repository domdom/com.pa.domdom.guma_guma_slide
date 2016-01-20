import utils

def run():
    unit_list = utils.load_base_json('/pa/units/unit_list.json')
    _list = []
    for unit in unit_list['units']:
        # skip the units which are not commanders
        if '/pa/units/commanders/' not in unit: continue
        _list.append(unit)

    _list = _list + [
        "/pa/units/land/assault_bot/assault_bot.json",
        "/pa/units/land/bot_factory/bot_factory.json",
        "/pa/units/land/fabrication_bot_combat/fabrication_bot_combat.json",
        "/pa/units/land/radar/radar.json",
        "/pa/units/land/energy_plant/energy_plant.json",
        "/pa/units/land/metal_extractor/metal_extractor.json"
    ]

    return {
        "target" : "/pa/units/unit_list.json",
        "patch" : [
            {"op": "replace", "path" : "/units", "value" : _list}
        ]
    }