var Build = (function() {
    var FALLBACK_ICON = 'coui://ui/main/game/live_game/img/build_bar/img_missing_unit.png';
    var pathWithoutExtensionMatch = /(.*)\.json[^\/]*$/;

    var iconForSpecId = function(id)
    {
        var match = null;
        if (id)
            match = pathWithoutExtensionMatch.exec(id);

        if (_.size(match) < 2)
            return FALLBACK_ICON;

        return 'coui:/' + match[1] + '_icon_buildbar.png';
    };

    var iconForUnit = function (unit)
    {
        if (!unit)
            return FALLBACK_ICON;
        return iconForSpecId(unit.id);
    };

    var HotkeyModel = function() {
        var self = this;

        self.SpecIdToGridMap = ko.observable(
            {
                "/pa/units/land/bot_factory/bot_factory.json": ["factory", 12],
                "/pa/units/land/metal_extractor/metal_extractor.json": ["factory", 14],
                "/pa/units/land/energy_plant/energy_plant.json": ["factory", 15],
                "/pa/units/land/radar/radar.json": ["factory", 16],

                "/pa/units/land/assault_bot/assault_bot.json": ["bot", 12],
                "/pa/units/land/fabrication_bot_combat/fabrication_bot_combat.json": ["bot", 13]
            }
        );
    };

    return {
        iconForSpecId: iconForSpecId,
        iconForUnit: iconForUnit,
        HotkeyModel: HotkeyModel,
    };
})();
