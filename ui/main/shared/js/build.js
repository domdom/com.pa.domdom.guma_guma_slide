
function BuildHotkeyModel() {
    var self = this;

    self.SpecIdToGridMap = ko.observable(
        {
            "/pa/units/land/radar/radar.json": ["factory", 13],
            "/pa/units/land/bot_factory/bot_factory.json": ["factory", 14],
			"/pa/units/land/energy_plant/energy_plant.json": ["factory", 12],
			"/pa/units/land/metal_extractor/metal_extractor.json": ["factory", 11],

			"/pa/units/land/assault_bot/assault_bot.json": ["bot", 11],
            "/pa/units/land/fabrication_bot_combat/fabrication_bot_combat.json": ["bot", 12],
        }
    );
};
