var _ICON_CLOSE_DARK = 'Icon_Search_Cancel.png';
var _ICON_SEARCH_OPEN = 'Icon_Search.png';
var _COLOR_GOLD = '#83764E';
var _COLOR_LIGHT_GOLD = '#DAD3C0';
function SearchDrawer(){
    this.trigger_selector = 'li[reboot-search-drawer-trigger]';
    this.target_selector = '[reboot-search-drawer]';
    this.icon_cancel = "img/" + _ICON_CLOSE_DARK;
    this.icon_open = "img/" + _ICON_SEARCH_OPEN;
    this.label_open_hex = _COLOR_LIGHT_GOLD;
    this.label_closed_hex = _COLOR_GOLD;
    this.toggle_search_icon = function(){
        var self = this;
        var src = $(self.trigger_selector).find('img').attr('src');
        var background = self.label_closed_hex;
        if ($(self.target_selector).is(':visible') === true){
            src = self.icon_cancel;
            background = self.label_open_hex;
        } else {
            src = self.icon_open;
        };
        $(self.trigger_selector).find('img').attr('src', src);
        $(self.trigger_selector).css('background', background);
    };
    this.toggle_input_focus = function(){
        var self = this;
        console.log(1235435245432)
        if ($(self.target_selector).is(':visible') === true){
            $(self.target_selector).find('input').focus();
        } else {
            $(self.target_selector).find('input').blur();
        };
    };
    this.control = function(){
        var self = this;
        $(self.target_selector).toggle();
        self.toggle_input_focus();
        //self.toggle_search_icon();
    };
    this.init = function(){
        var self = this;
        $(self.trigger_selector).click(function(){
            self.control();
        });
        $(self.trigger_selector).keyup(function(event){
            if (event.keyCode === 13) { self.control() };
        });
    };
    this.init();
};

function RebootController(){
    new SearchDrawer();
};

$(document).ready(function(){
    new RebootController();
    $(window).resize(function(){
        new RebootController();
    });
});
