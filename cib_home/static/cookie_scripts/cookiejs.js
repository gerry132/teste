// ----------------------------------------------------------------------------
// Polyfills
// ----------------------------------------------------------------------------

// Source: https://gist.github.com/eirikbacker/2864711
(function (window, document, listeners_prop_name) {
    if ((!window.addEventListener || !window.removeEventListener) && window.attachEvent && window.detachEvent) {
        /**
         * @param {*} value
         * @return {boolean}
         */
        var is_callable = function (value) {
            return typeof value === 'function';
        };
        /**
         * @param {!Window|HTMLDocument|Node} self
         * @param {EventListener|function(!Event):(boolean|undefined)} listener
         * @return {!function(Event)|undefined}
         */
        var listener_get = function (self, listener) {
            var listeners = listener[listeners_prop_name];
            if (listeners) {
                var lis;
                var i = listeners.length;
                while (i--) {
                    lis = listeners[i];
                    if (lis[0] === self) {
                        return lis[1];
                    }
                }
            }
        };
        /**
         * @param {!Window|HTMLDocument|Node} self
         * @param {EventListener|function(!Event):(boolean|undefined)} listener
         * @param {!function(Event)} callback
         * @return {!function(Event)}
         */
        var listener_set = function (self, listener, callback) {
            var listeners = listener[listeners_prop_name] || (listener[listeners_prop_name] = []);
            return listener_get(self, listener) || (listeners[listeners.length] = [self, callback], callback);
        };
        /**
         * @param {string} methodName
         */
        var docHijack = function (methodName) {
            var old = document[methodName];
            document[methodName] = function (v) {
                return addListen(old(v));
            };
        };
        /**
         * @this {!Window|HTMLDocument|Node}
         * @param {string} type
         * @param {EventListener|function(!Event):(boolean|undefined)} listener
         * @param {boolean=} useCapture
         */
        var addEvent = function (type, listener, useCapture) {
            if (is_callable(listener)) {
                var self = this;
                self.attachEvent(
                    'on' + type,
                    listener_set(self, listener, function (e) {
                        e = e || window.event;
                        e.preventDefault = e.preventDefault || function () { e.returnValue = false };
                        e.stopPropagation = e.stopPropagation || function () { e.cancelBubble = true };
                        e.target = e.target || e.srcElement || document.documentElement;
                        e.currentTarget = e.currentTarget || self;
                        e.timeStamp = e.timeStamp || (new Date()).getTime();
                        listener.call(self, e);
                    })
                );
            }
        };
        /**
         * @this {!Window|HTMLDocument|Node}
         * @param {string} type
         * @param {EventListener|function(!Event):(boolean|undefined)} listener
         * @param {boolean=} useCapture
         */
        var removeEvent = function (type, listener, useCapture) {
            if (is_callable(listener)) {
                var self = this;
                var lis = listener_get(self, listener);
                if (lis) {
                    self.detachEvent('on' + type, lis);
                }
            }
        };
        /**
         * @param {!Node|NodeList|Array} obj
         * @return {!Node|NodeList|Array}
         */
        var addListen = function (obj) {
            var i = obj.length;
            if (i) {
                while (i--) {
                    obj[i].addEventListener = addEvent;
                    obj[i].removeEventListener = removeEvent;
                }
            } else {
                obj.addEventListener = addEvent;
                obj.removeEventListener = removeEvent;
            }
            return obj;
        };

        addListen([document, window]);
        if ('Element' in window) {
            /**
             * IE8
             */
            var element = window.Element;
            element.prototype.addEventListener = addEvent;
            element.prototype.removeEventListener = removeEvent;
        } else {
            /**
             * IE < 8
             */
            //Make sure we also init at domReady
            document.attachEvent('onreadystatechange', function () { addListen(document.all) });
            docHijack('getElementsByTagName');
            docHijack('getElementById');
            docHijack('createElement');
            addListen(document.all);
        }
    }
})(window, document, 'x-ms-event-listeners');


Array.isArray = function (obj) {
    return Object.prototype.toString.call(obj) === "[object Array]";
};

// ----------------------------------------------------------------------------
// Languages
// ----------------------------------------------------------------------------

var __COOKIESJS_CONTROLLER;


// ----------------------------------------------------------------------------
// Languages
// ----------------------------------------------------------------------------

var __COOKIEJS_DEFAULT_LANGUAGE = 'en';
var __COOKIEJS_CURRENT_LANGUAGE;


// ----------------------------------------------------------------------------
// Cookies
// ----------------------------------------------------------------------------

var __COOKIEJS_COOKIE_NAME = 'cookiejs_preferences';
var __COOKIEJS_COOKIE_VARIABLE_NAME = 'cookiejs_cookie_values';
var __COOKIEJS_PREFERENCE_DAYS = 180;
var __COOKIEJS_PREFERENCES_SELECTED_NAME = 'preferences_selected';
var __COOKIEJS_PREFERENCES_VARIABLE_NAME = 'cookiejs_preferences';


// ----------------------------------------------------------------------------
// Base css value
// ----------------------------------------------------------------------------

var __COOKIEJS_CSS_BACKGROUND_COLOR_A = '#F6F6F2';
var __COOKIEJS_CSS_BACKGROUND_COLOR_B = '#004D44';
var __COOKIEJS_CSS_BACKGROUND_COLOR_C = '#FFFFFF';
var __COOKIEJS_CSS_BACKGROUND_COLOR_D = '#DDDDDD';
var __COOKIEJS_CSS_BACKGROUND_COLOR_E = '#DDDDDD';
var __COOKIEJS_CSS_BUTTON_COLOR_A = '#A39161';
var __COOKIEJS_CSS_BUTTON_COLOR_B = '#009C3C';
var __COOKIEJS_CSS_BUTTON_COLOR_C = '#DDDDDD';
var __COOKIEJS_CSS_TEXT_COLOR_A = '#000000';
var __COOKIEJS_CSS_TEXT_COLOR_B = '#FFFFFF';
var __COOKIEJS_CSS_TEXT_COLOR_C = '#FFFFFF';
var __COOKIEJS_CSS_DEFAULT_FONT = 'Arial';
var __COOKIEJS_CSS_MAX_WIDTH = '100%';


// ----------------------------------------------------------------------------
// Class names
// ----------------------------------------------------------------------------

var __COOKIEJS_CLASSNAME_PREFIX = 'cookiejs-'

// Banner
var __COOKIEJS_CLASSNAME_BANNER_WRAPPER = __COOKIEJS_CLASSNAME_PREFIX + 'banner-wrapper';
var __COOKIEJS_CLASSNAME_BANNER = __COOKIEJS_CLASSNAME_PREFIX + 'banner';
var __COOKIEJS_CLASSNAME_BANNER_HEADING = __COOKIEJS_CLASSNAME_PREFIX + 'banner-heading';
var __COOKIEJS_CLASSNAME_BANNER_TEXT = __COOKIEJS_CLASSNAME_PREFIX + 'banner-text';
var __COOKIEJS_CLASSNAME_BANNER_UL = __COOKIEJS_CLASSNAME_PREFIX + 'banner-ul';
var __COOKIEJS_CLASSNAME_BANNER_LI = __COOKIEJS_CLASSNAME_PREFIX + 'banner-li';
var __COOKIEJS_CLASSNAME_BANNER_LINK = __COOKIEJS_CLASSNAME_PREFIX + 'banner-link';

// Footer
var __COOKIEJS_CLASSNAME_FOOTER_WRAPPER = __COOKIEJS_CLASSNAME_PREFIX + 'footer-wrapper';
var __COOKIEJS_CLASSNAME_FOOTER = __COOKIEJS_CLASSNAME_PREFIX + 'footer';
var __COOKIEJS_CLASSNAME_FOOTER_HEADING = __COOKIEJS_CLASSNAME_PREFIX + 'footer-heading';
var __COOKIEJS_CLASSNAME_FOOTER_TEXT = __COOKIEJS_CLASSNAME_PREFIX + 'footer-text';
var __COOKIEJS_CLASSNAME_FOOTER_UL = __COOKIEJS_CLASSNAME_PREFIX + 'footer-ul';
var __COOKIEJS_CLASSNAME_FOOTER_LI = __COOKIEJS_CLASSNAME_PREFIX + 'footer-li';
var __COOKIEJS_CLASSNAME_FOOTER_LINK = __COOKIEJS_CLASSNAME_PREFIX + 'footer-link';

// Modal
var __COOKIEJS_CLASSNAME_MODAL = __COOKIEJS_CLASSNAME_PREFIX + 'modal';
var __COOKIEJS_CLASSNAME_MODAL_CONTENT = __COOKIEJS_CLASSNAME_PREFIX + 'modal-content';
var __COOKIEJS_CLASSNAME_MODAL_HEADER = __COOKIEJS_CLASSNAME_PREFIX + 'modal-header';
var __COOKIEJS_CLASSNAME_MODAL_HEADING = __COOKIEJS_CLASSNAME_PREFIX + 'modal-heading';
var __COOKIEJS_CLASSNAME_MODAL_BODY = __COOKIEJS_CLASSNAME_PREFIX + 'modal-body';
var __COOKIEJS_CLASSNAME_MODAL_TABLE = __COOKIEJS_CLASSNAME_PREFIX + 'modal-table';
var __COOKIEJS_CLASSNAME_MODAL_FOOTER = __COOKIEJS_CLASSNAME_PREFIX + 'modal-footer';
var __COOKIEJS_CLASSNAME_MODAL_FOOTER_LINK_A = __COOKIEJS_CLASSNAME_PREFIX + 'modal-footer-link-a';
var __COOKIEJS_CLASSNAME_MODAL_FOOTER_LINK_B = __COOKIEJS_CLASSNAME_PREFIX + 'modal-footer-link-b';


// ----------------------------------------------------------------------------
// Translations
// ----------------------------------------------------------------------------

// Banner
var __COOKIEJS_TRANSLATION_BANNER_HEADING = {'en': 'A notice about cookies', 'ga': 'FÃƒÂ³gra maidir le cuacha'};
var __COOKIEJS_TRANSLATION_BANNER_TEXT = {
    'en': 'This website uses cookies to collect information about how you use this site. This information is used to make the website work as well as possible.',
};
var __COOKIEJS_TRANSLATION_BANNER_ALLOW_ALL = {'en': 'Allow all', 'ga': 'Glac le gach ceann'};
var __COOKIEJS_TRANSLATION_BANNER_SET_PREFERENCES = {'en': 'Set preferences', 'ga': 'Roghnaigh'};

// Footer
var __COOKIEJS_TRANSLATION_FOOTER_HEADING = {'en': 'Manage cookie preferences', 'ga': 'Eagraigh fianÃƒÂ¡in'};
var __COOKIEJS_TRANSLATION_FOOTER_SET_PREFERENCES = {'en': 'Manage preferences', 'ga': 'Do rogha fianÃƒÂ¡n'};

// Modal
var __COOKIEJS_TRANSLATION_MODAL_HEADING = {'en': 'Cookie preferences', 'ga': 'Roghanna fianÃƒÂ¡n'};
var __COOKIEJS_TRANSLATION_MODAL_SAVE = {'en': 'Save preferences', 'ga': 'SÃƒÂ¡bhÃƒÂ¡il do roghanna'};
var __COOKIEJS_TRANSLATION_MODAL_CLOSE = {'en': 'Close', 'ga': 'DÃƒÂºn'};
var __COOKIEJS_TRANSLATION_MODAL_ALL = {'en': 'Allow', 'ga': 'Ceadaigh'};
var __COOKIEJS_TRANSLATION_MODAL_DESCRIPTION = {'en': 'Description', 'ga': 'Cur sÃƒÂ­os'};


// ----------------------------------------------------------------------------
// Common preferences translations
// ----------------------------------------------------------------------------

var __COOKIEJS_TRANSLATION_PREFERENCE_GOOGLE_ANALYTICS = {
        'en': '<h2>Cookies that measure website use</h2>' +
            '<p>We use Google Analytics to measure how you use the website so we can <br> improve it based on user needs. We do not allow Google to use or share the <br> data about how you use this site.' +
            '</p><p>Google Analytics sets cookies that store anonymised information about:</p>' +
            '<ul><li>how you got to the site</li><li>the pages you visit on this site and how long <br> you spend on each page</li><li>what you click on while you\'re visiting the site</li> </ul>',
};
var __COOKIEJS_TRANSLATION_PREFERENCE_IFRAMES = {
    'en': '<h2>Cookies that help with our communications</h2><p>These cookies may be set by third party websites and do things like measure <br> how you view YouTube videos that are on this site.</p>',
};

//
//
//

var __COOKIEJS_TRANSLATION_IFRAME_TEXT = {
    'en': 'Please change your cookie preferences to see this content.'
}


// ----------------------------------------------------------------------------
// Device breakpoints
// ----------------------------------------------------------------------------

var __COOKIEJS_BREAKPOINT_MOBILE = 479;
var __COOKIEJS_BREAKPOINT_TABLET = 991;


// ----------------------------------------------------------------------------
// Window helpers
// ----------------------------------------------------------------------------

function __CookieJsWindow(){
    this.document_width = function(){ return document.width };
    this.screen_width = function(){ return window.innerWidth };
}


// ----------------------------------------------------------------------------
// User device helpers
// ----------------------------------------------------------------------------

function __CookieJsUserDevice(){
    this.screen_size = new __CookieJsWindow().screen_width();
    this.tablet_break_point = function(){ return __COOKIEJS_BREAKPOINT_TABLET };
    this.mobile_break_point = function(){ return __COOKIEJS_BREAKPOINT_MOBILE };
    this.is_desktop = function(){
        var self = this;
        if (self.screen_size > self.tablet_break_point()){
            return true;
        }
        return false;
    };
    this.is_tablet = function(){
        var self = this;
        if (self.screen_size > self.mobile_break_point() && self.screen_size < self.tablet_break_point()){
            return true;
        }
        return false;
    };
    this.is_mobile = function(){
        var self = this;
        if (self.screen_size < self.mobile_break_point()){
            return true;
        }
        return false;
    };
};


// ----------------------------------------------------------------------------
// Cookie jar function
// ----------------------------------------------------------------------------

function __cookiejs_days_to_date(days){
    var d = new Date();
    d.setTime(d.getTime() + (days * 24 * 60 * 60 * 1000));
    return d.toUTCString();
};


function __cookiejs_get_cookie_key_value_pair(regex){
    var value = document.cookie.match(new RegExp("(^| )" + regex + "=([^;]+)"));
    if (value === null) { return null };
    return value[0].split('=');
}


function __cookiejs_get_cookie(cname){
    var values = __cookiejs_get_cookie_key_value_pair(cname);
    if (values === null) { return null };
    return values[1] || null;
};


function __cookiejs_get_cookie_as_json(name){
    var value = __cookiejs_get_cookie(name);
    if (value === null) { return {} };
    return JSON.parse(value);
};


function __cookiejs_get_hostname(){
    var hostname = location.hostname;
    //if (hostname.substring(0,4) !== 'www.'){
    //    hostname = '.' + hostname;
    //}
    return hostname;
}


function __cookiejs_set_cookie(cname, value, days) {
    var date_string = __cookiejs_days_to_date(days);
    document.cookie = cname + "=" + value + ";" + "expires=" + date_string + ";domain=" + __cookiejs_get_hostname() + ";path=/";
};


function __cookiejs_reset_cookie(days){
    __cookiejs_set_cookie(
        __COOKIEJS_COOKIE_NAME,
        JSON.stringify(window[__COOKIEJS_COOKIE_VARIABLE_NAME]),
        __COOKIEJS_PREFERENCE_DAYS
    );
};


function __cookiejs_delete_cookie(cname){
    var values = __cookiejs_get_cookie_key_value_pair(cname);
    if (values !== null) { document.cookie = values[0] + '=; Max-Age=-99999999;domain='+ __cookiejs_get_hostname() +';path=/' };
};


function __cookiejs_add_preferences(array){
    if (window[__COOKIEJS_PREFERENCES_VARIABLE_NAME] === undefined) {
        window[__COOKIEJS_PREFERENCES_VARIABLE_NAME] = [];
    };

    if (Array.isArray(array) !== true){ array = [] };

    for (var i = 0; i < array.length; i++){
        window[__COOKIEJS_PREFERENCES_VARIABLE_NAME].push(array[i]);
    };

};


// ----------------------------------------------------------------------------
// Utils
// ----------------------------------------------------------------------------

function __cookiejs_cookie_preferences_selected(){
    return window[__COOKIEJS_COOKIE_VARIABLE_NAME][__COOKIEJS_PREFERENCES_SELECTED_NAME] || false;
}


// ----------------------------------------------------------------------------
// Translations
// ----------------------------------------------------------------------------

function __CookieJsTranslation(translation_dict){
    this.translation_dict = translation_dict;
    this.get_translation = function(){
        var self = this;

        default_language = __COOKIEJS_DEFAULT_LANGUAGE;
        current_language = __COOKIEJS_CURRENT_LANGUAGE;

        var default_translation = self.translation_dict[default_language];

        var language = current_language || default_language;
        if (language === default_language){
            return default_translation;
        };

        var requested_translation = self.translation_dict[language];
        if (requested_translation === undefined) {
            return default_translation;
        };

        return requested_translation;

    };
};


// ----------------------------------------------------------------------------
// Preference
// ----------------------------------------------------------------------------

function __CookieJsPreference(translation_dict, key, callback){
    this.translations = new __CookieJsTranslation(translation_dict);
    this.key = key;
    this.callback = callback;
    //
    this.create_element = function(){
        var self = this;

        var input_element = document.createElement('input');
        input_element.type = 'checkbox';
        input_element.addEventListener('click', function(){ self.toggle_value() });

        var element = document.createElement('tr');

        var col_1 = document.createElement('td');
        col_1.appendChild(input_element);

        var col_2 = document.createElement('td');
        col_2.innerHTML = self.translations.get_translation();

        element.appendChild(col_1);
        element.appendChild(col_2);

        //
        return element;
    };
    //
    this.toggle_value = function(){
        var self = this;
        var current_value = window[__COOKIEJS_COOKIE_VARIABLE_NAME][key] || false;
        window[__COOKIEJS_COOKIE_VARIABLE_NAME][key] = !current_value;
    };
    this.listener = function(){
        var self = this;
        self.toggle_value();
    };
    this.update_element = function(){
        var self = this;
        this.element.querySelectorAll('input')[0].checked = window[__COOKIEJS_COOKIE_VARIABLE_NAME][self.key] || false;
    };
    this.trigger_callback = function(){
        var self = this;
        var value = window[__COOKIEJS_COOKIE_VARIABLE_NAME][self.key] || false;
        if (self.callback !== undefined){ self.callback(value) };
    };
    //
    this.element = this.create_element();
};


// ----------------------------------------------------------------------------
// Preferences modal
// ----------------------------------------------------------------------------

function __CookieJsPreferencesModal(controller){
    this.controller = controller;
    // fn
    this.open = function(){
        var self = this;
        for (var i = 0; i < window[__COOKIEJS_PREFERENCES_VARIABLE_NAME].length; i++){
            window[__COOKIEJS_PREFERENCES_VARIABLE_NAME][i].update_element();
        };
        self.element.style.display = 'block';
    };
    this.close = function(){
        var self = this;
        self.element.style.display = 'none';
    };
    this.trigger_callbacks = function(){
        for (var i = 0; i < window[__COOKIEJS_PREFERENCES_VARIABLE_NAME].length; i++){
            window[__COOKIEJS_PREFERENCES_VARIABLE_NAME][i].trigger_callback();
        };
    };
    this.save_listener = function(){
        var self = this;
        window[__COOKIEJS_COOKIE_VARIABLE_NAME][__COOKIEJS_PREFERENCES_SELECTED_NAME] = true;
        __cookiejs_reset_cookie();
        self.trigger_callbacks();
        self.close();
        self.controller.banner.element.style.display = 'none';
        self.controller.footer.element.style.display = 'block';
        location.reload();
    };
    // element
    this.get_element = function(){
        var self = this;

        var user_device = new __CookieJsUserDevice();

        var _CLOSE = new __CookieJsTranslation(__COOKIEJS_TRANSLATION_MODAL_CLOSE);
        var _HEADING = new __CookieJsTranslation(__COOKIEJS_TRANSLATION_MODAL_HEADING);
        var _SAVE = new __CookieJsTranslation(__COOKIEJS_TRANSLATION_MODAL_SAVE);

        var _ALLOW = new __CookieJsTranslation(__COOKIEJS_TRANSLATION_MODAL_ALL);
        var _DESCRIPTION = new __CookieJsTranslation(__COOKIEJS_TRANSLATION_MODAL_DESCRIPTION);

        var inline_style = document.createElement('style');
        inline_style.innerHTML = '.' + __COOKIEJS_CLASSNAME_MODAL + ' {';
        inline_style.innerHTML += 'font-family: ' + __COOKIEJS_CSS_DEFAULT_FONT + ';';
        inline_style.innerHTML += 'background-color: rgba(0, 0, 0, 0.7);';
        inline_style.innerHTML += 'position: fixed;';
        inline_style.innerHTML += 'z-index: 10000000;';
        inline_style.innerHTML += 'padding-top: 50px;';
        inline_style.innerHTML += 'left: 0;';
        inline_style.innerHTML += 'top: 0;';
        inline_style.innerHTML += 'width: 100%;';
        inline_style.innerHTML += 'height: 100%;';
        inline_style.innerHTML += 'overflow: auto;';
        inline_style.innerHTML += '}';
        inline_style.innerHTML += '.' + __COOKIEJS_CLASSNAME_MODAL_CONTENT + ' {';
        inline_style.innerHTML += 'background-color: ' + __COOKIEJS_CSS_BACKGROUND_COLOR_C + ';';
        inline_style.innerHTML += 'position: relative;';
        inline_style.innerHTML += 'margin: auto;';
        inline_style.innerHTML += 'padding: 0;';
        inline_style.innerHTML += '}';
        inline_style.innerHTML += '.' + __COOKIEJS_CLASSNAME_MODAL_HEADER + ' {';
        inline_style.innerHTML += 'background-color: ' + __COOKIEJS_CSS_BACKGROUND_COLOR_B + ';';
        inline_style.innerHTML += 'padding-top: 20px;';
        inline_style.innerHTML += 'padding-bottom: 20px;';
        inline_style.innerHTML += 'width: 100%;';
        inline_style.innerHTML += '}';
        inline_style.innerHTML += '.' + __COOKIEJS_CLASSNAME_MODAL_HEADING + ' {';
        inline_style.innerHTML += 'color: ' + __COOKIEJS_CSS_TEXT_COLOR_B + ';';
        inline_style.innerHTML += 'font-size: 21px !important;';
        inline_style.innerHTML += 'font-weight: bold !important;';
        inline_style.innerHTML += 'font-family: ' + __COOKIEJS_CSS_DEFAULT_FONT + ' !important;';
        inline_style.innerHTML += 'margin: 0px !important;';
        inline_style.innerHTML += 'padding: 0px !important;';
        inline_style.innerHTML += 'padding-left: 20px !important;';
        inline_style.innerHTML += 'border: 0px !important;';
        inline_style.innerHTML += '}';
        inline_style.innerHTML += '.' + __COOKIEJS_CLASSNAME_MODAL_BODY + ' {';
        inline_style.innerHTML += 'height: 70vh;';
        inline_style.innerHTML += 'width: 100%;';
        inline_style.innerHTML += 'overflow-y: scroll;';
        inline_style.innerHTML += '}';
        inline_style.innerHTML += '.' + __COOKIEJS_CLASSNAME_MODAL_TABLE + ' {';
        inline_style.innerHTML += 'width: 100% !important;';
        inline_style.innerHTML += 'background-color: ' + __COOKIEJS_CSS_BACKGROUND_COLOR_C + ' !important;';
        inline_style.innerHTML += 'border: none !important;';
        inline_style.innerHTML += '}';
        inline_style.innerHTML += '.' + __COOKIEJS_CLASSNAME_MODAL_TABLE + ' tr {';
        inline_style.innerHTML += 'text-align: left !important;';
        inline_style.innerHTML += 'background-color: ' + __COOKIEJS_CSS_BACKGROUND_COLOR_C + ' !important;';
        inline_style.innerHTML += 'margin-bottom: 20px !important;';
        inline_style.innerHTML += '}';
        inline_style.innerHTML += '.' + __COOKIEJS_CLASSNAME_MODAL_TABLE + ' th {';
        inline_style.innerHTML += 'padding: 20px 0px 20px 20px !important;';
        inline_style.innerHTML += 'text-align: left !important;';
        inline_style.innerHTML += 'vertical-align: top !important;';
        inline_style.innerHTML += 'font-size: 16px !important;';
        inline_style.innerHTML += '}';
        inline_style.innerHTML += '.' + __COOKIEJS_CLASSNAME_MODAL_TABLE + ' td {';
        inline_style.innerHTML += 'padding: 20px 0px 20px 20px !important;';
        inline_style.innerHTML += 'text-align: left !important;';
        inline_style.innerHTML += 'vertical-align: top !important;';
        inline_style.innerHTML += '}';
        inline_style.innerHTML += '.' + __COOKIEJS_CLASSNAME_MODAL_TABLE + ' td h2 {';
        inline_style.innerHTML += 'margin: 0px !important;';
        inline_style.innerHTML += 'padding: 0px !important;';
        inline_style.innerHTML += 'font-size: 24px !important;';
        inline_style.innerHTML += 'font-weight: bold !important;';
        inline_style.innerHTML += 'border-width: 0px !important;';
        inline_style.innerHTML += 'margin-bottom: 20px !important;';
        inline_style.innerHTML += '}';
        inline_style.innerHTML += '.' + __COOKIEJS_CLASSNAME_MODAL_TABLE + ' td h3 {';
        inline_style.innerHTML += 'margin: 0px;';
        inline_style.innerHTML += 'padding: 0px;';
        inline_style.innerHTML += 'font-size: 21px;';
        inline_style.innerHTML += 'font-weight: bold;';
        inline_style.innerHTML += 'border-width: 0px;';
        inline_style.innerHTML += '}';
        inline_style.innerHTML += '.' + __COOKIEJS_CLASSNAME_MODAL_TABLE + ' td ul {';
        inline_style.innerHTML += 'margin: 0px;';
        inline_style.innerHTML += 'padding: 0px;';
        inline_style.innerHTML += 'font-size: 16px !important;';
        inline_style.innerHTML += '}';
        inline_style.innerHTML += '.' + __COOKIEJS_CLASSNAME_MODAL_TABLE + ' td li {';
        inline_style.innerHTML += 'margin-left: 20px;';
        inline_style.innerHTML += 'font-size: 16px !important;';
        inline_style.innerHTML += '}';
        inline_style.innerHTML += '.' + __COOKIEJS_CLASSNAME_MODAL_TABLE + ' td p {';
        inline_style.innerHTML += 'font-size: 16px !important;';
        inline_style.innerHTML += 'margin-bottom: 20px;';
        inline_style.innerHTML += '}';
        inline_style.innerHTML += '.' + __COOKIEJS_CLASSNAME_MODAL_FOOTER + ' {';
        inline_style.innerHTML += 'padding: 20px;';
        inline_style.innerHTML += 'width: 100%;';
        inline_style.innerHTML += '}';
        inline_style.innerHTML += '.' + __COOKIEJS_CLASSNAME_MODAL_FOOTER_LINK_A + ' {';
        inline_style.innerHTML += 'background-color: ' + __COOKIEJS_CSS_BUTTON_COLOR_A + ';';
        inline_style.innerHTML += 'padding: 10px !important;';
        inline_style.innerHTML += 'font-size: 16px !important;';
        inline_style.innerHTML += 'text-decoration: none;';
        inline_style.innerHTML += 'margin-right: 10px;';
        inline_style.innerHTML += 'color: ' + __COOKIEJS_CSS_TEXT_COLOR_B + ' !important;';
        inline_style.innerHTML += '}';
        inline_style.innerHTML += '.' + __COOKIEJS_CLASSNAME_MODAL_FOOTER_LINK_A + ':hover {';
        inline_style.innerHTML += 'color: ' + __COOKIEJS_CSS_TEXT_COLOR_B + ' !important;';
        inline_style.innerHTML += 'text-decoration: underline;';
        inline_style.innerHTML += '}';
        inline_style.innerHTML += '.' + __COOKIEJS_CLASSNAME_MODAL_FOOTER_LINK_B + ' {';
        inline_style.innerHTML += 'background-color: ' + __COOKIEJS_CSS_BUTTON_COLOR_C + ';';
        inline_style.innerHTML += 'padding: 10px !important;';
        inline_style.innerHTML += 'font-size: 16px !important;';
        inline_style.innerHTML += 'text-decoration: none;';
        inline_style.innerHTML += 'color: ' + __COOKIEJS_CSS_TEXT_COLOR_A + ' !important;';
        inline_style.innerHTML += '}';
        inline_style.innerHTML += '.' + __COOKIEJS_CLASSNAME_MODAL_FOOTER_LINK_B + ':hover {';
        inline_style.innerHTML += 'color: ' + __COOKIEJS_CSS_TEXT_COLOR_A + ' !important;';
        inline_style.innerHTML += 'text-decoration: underline;';
        inline_style.innerHTML += '}';

        // Modal
        var element = document.createElement('div');
        element.style['display'] = 'none';
        element.className = __COOKIEJS_CLASSNAME_MODAL;

        // Modal contents
        var content = document.createElement('div');
        content.className = __COOKIEJS_CLASSNAME_MODAL_CONTENT;
        if (user_device.is_mobile() === true || user_device.is_tablet() === true){
            content.style['width'] = '80%';
        } else {
            content.style['width'] = '1000px';
        };

        // Modal header
        var header = document.createElement('div');
        header.className = __COOKIEJS_CLASSNAME_MODAL_HEADER;

        //Modal Header H2
        var header_h2 = document.createElement('h2');
        header_h2.className = __COOKIEJS_CLASSNAME_MODAL_HEADING;
        header_h2.innerHTML = _HEADING.get_translation();

        //Modal Body
        var body = document.createElement('div');
        body.className = __COOKIEJS_CLASSNAME_MODAL_BODY;

        // Table
        var table = document.createElement('table');
        table.className = __COOKIEJS_CLASSNAME_MODAL_TABLE;

        var header_row = document.createElement('tr');
        header_row.style['background-color'] = __COOKIEJS_CSS_BACKGROUND_COLOR_D;

        var header_col_1 = document.createElement('th');
        header_col_1.innerHTML = _ALLOW.get_translation();
        header_col_1.width = '15%';

        var header_col_2 = document.createElement('th');
        header_col_2.innerHTML = _DESCRIPTION.get_translation();

        header_row.appendChild(header_col_1);
        header_row.appendChild(header_col_2);

        table.appendChild(header_row);

        var preferences = window[__COOKIEJS_PREFERENCES_VARIABLE_NAME] || [];
        for (var i = 0; i < preferences.length; i++) {
            table.appendChild(preferences[i].element);
        };

        // Modal footer
        var footer = document.createElement('div');
        footer.className = __COOKIEJS_CLASSNAME_MODAL_FOOTER;

        var a_element_1 = document.createElement('a');
        a_element_1.className = __COOKIEJS_CLASSNAME_MODAL_FOOTER_LINK_A;
        a_element_1.href = '#';
        a_element_1.innerHTML = _SAVE.get_translation();
        a_element_1.addEventListener('click', function(){ self.save_listener() });

        var a_element_2 = document.createElement('a');
        a_element_2.className = __COOKIEJS_CLASSNAME_MODAL_FOOTER_LINK_B;
        a_element_2.href = '#';
        a_element_2.innerHTML = _CLOSE.get_translation();
        a_element_2.addEventListener('click', function(){ self.close() });

        // Append elements
        header.appendChild(header_h2);
        footer.appendChild(a_element_1);
        footer.appendChild(a_element_2);
        body.appendChild(table);
        content.appendChild(header);
        content.appendChild(body);
        content.appendChild(footer);
        element.appendChild(inline_style);
        element.appendChild(content);

        return element;
    };
    this.element = this.get_element();
};


// ----------------------------------------------------------------------------
// Cookie banner
// ----------------------------------------------------------------------------

function __CookieJsBanner(controller){
    this.controller = controller;
    this.show = !__cookiejs_cookie_preferences_selected();
    // fn
    this.select_all_listener = function(){
        var self = this;
        // mark preferences true
        var preferences = window[__COOKIEJS_PREFERENCES_VARIABLE_NAME] || [];
        for (var i = 0; i < preferences.length; i++){
            var key = preferences[i].key;
            window[__COOKIEJS_COOKIE_VARIABLE_NAME][key] = true;
        };
        // preferences selected
        window[__COOKIEJS_COOKIE_VARIABLE_NAME][__COOKIEJS_PREFERENCES_SELECTED_NAME] = true;
        // hide elements
        this.element.style.display = 'none';
        this.controller.footer.element.style.display = 'block';
        //
        this.controller.modal.trigger_callbacks();
        __cookiejs_reset_cookie();
    };
    // element
    this.get_element = function(){
        var self = this;

        var _HEADING = new __CookieJsTranslation(__COOKIEJS_TRANSLATION_BANNER_HEADING);
        var _TEXT = new __CookieJsTranslation(__COOKIEJS_TRANSLATION_BANNER_TEXT);
        var _ALLOW_ALL = new __CookieJsTranslation(__COOKIEJS_TRANSLATION_BANNER_ALLOW_ALL);
        var _SET_PREFERENCES = new __CookieJsTranslation(__COOKIEJS_TRANSLATION_BANNER_SET_PREFERENCES);

        var inline_style = document.createElement('style');
        inline_style.innerHTML = '.' + __COOKIEJS_CLASSNAME_BANNER_WRAPPER + ' {';
        inline_style.innerHTML += 'font-family: ' + __COOKIEJS_CSS_DEFAULT_FONT + ' !important;';
        inline_style.innerHTML += 'background-color: ' + __COOKIEJS_CSS_BACKGROUND_COLOR_A + ' !important;';
        inline_style.innerHTML += 'padding: 10px 10px 10px 10px !important;';
        inline_style.innerHTML += 'width: 100% !important;';
        inline_style.innerHTML += 'color: ' + __COOKIEJS_CSS_TEXT_COLOR_B + ' !important;';
        inline_style.innerHTML += '}';
        inline_style.innerHTML += '.' + __COOKIEJS_CLASSNAME_BANNER + ' {';
        inline_style.innerHTML += 'width: ' + __COOKIEJS_CSS_MAX_WIDTH + ' !important;';
        inline_style.innerHTML += 'margin: auto !important;';
        inline_style.innerHTML += '}';
        inline_style.innerHTML += '.' + __COOKIEJS_CLASSNAME_BANNER_HEADING + ' {';
        inline_style.innerHTML += 'color: ' + __COOKIEJS_CSS_TEXT_COLOR_A + ' !important;';
        inline_style.innerHTML += 'font-size: 21px !important;';
        inline_style.innerHTML += 'font-weight: bold !important;';
        inline_style.innerHTML += 'margin: 0px !important;';
        inline_style.innerHTML += 'padding: 0px !important;';
        inline_style.innerHTML += 'margin-bottom: 5px !important;';
        inline_style.innerHTML += 'border-width: 0px !important;';
        inline_style.innerHTML += '}';
        inline_style.innerHTML += '.' + __COOKIEJS_CLASSNAME_BANNER_TEXT + ' {';
        inline_style.innerHTML += 'color: ' + __COOKIEJS_CSS_TEXT_COLOR_A + ' !important;';
        inline_style.innerHTML += 'font-size: 16px !important;';
        inline_style.innerHTML += 'margin-bottom: 15px !important;';
        inline_style.innerHTML += '}';
        inline_style.innerHTML += '.' + __COOKIEJS_CLASSNAME_BANNER_UL + ' {';
        inline_style.innerHTML += 'margin: 0px !important;';
        inline_style.innerHTML += 'padding: 0px !important;';
        inline_style.innerHTML += 'margin-bottom: 10px !important;';
        inline_style.innerHTML += '}';
        inline_style.innerHTML += '.' + __COOKIEJS_CLASSNAME_BANNER_LI + ' {';
        inline_style.innerHTML += 'display: inline-block !important;';
        inline_style.innerHTML += 'margin-right: 10px !important;';
        inline_style.innerHTML += '}';
        inline_style.innerHTML += '.' + __COOKIEJS_CLASSNAME_BANNER_LINK + ' {';
        inline_style.innerHTML += 'background-color: ' + __COOKIEJS_CSS_BUTTON_COLOR_B + ' !important;';
        inline_style.innerHTML += 'font-size: 16px !important;';
        inline_style.innerHTML += 'padding: 10px !important;';
        inline_style.innerHTML += 'text-decoration: none;';
        inline_style.innerHTML += 'color: ' + __COOKIEJS_CSS_TEXT_COLOR_B + ' !important;';
        inline_style.innerHTML += '}';
        inline_style.innerHTML += '.' + __COOKIEJS_CLASSNAME_BANNER_LINK + ':hover {';
        inline_style.innerHTML += 'text-decoration: underline;';
        inline_style.innerHTML += '}';

        // Wrapper
        var element = document.createElement('div');
        element.className = __COOKIEJS_CLASSNAME_BANNER_WRAPPER;
        element.style['display'] = 'none';
        if (self.show === true) { element.style.display = 'block' };

        // Content
        var div_element = document.createElement('div');
        div_element.className = __COOKIEJS_CLASSNAME_BANNER;

        // Heading
        h2_element = document.createElement('h2');
        h2_element.className = __COOKIEJS_CLASSNAME_BANNER_HEADING;
        h2_element.innerHTML = _HEADING.get_translation();

        // Paragraph
        p_element = document.createElement('p');
        p_element.className = __COOKIEJS_CLASSNAME_BANNER_TEXT;
        p_element.innerHTML = _TEXT.get_translation();

        // List
        var ul_element = document.createElement('ul');
        ul_element.className = __COOKIEJS_CLASSNAME_BANNER_UL;
        ul_element.role = 'navigation';

        // List element 1
        var li_element_1 = document.createElement('li');
        li_element_1.className = __COOKIEJS_CLASSNAME_BANNER_LI;

        // List element 2
        var li_element_2 = document.createElement('li');
        li_element_2.className = __COOKIEJS_CLASSNAME_BANNER_LI;

        // Link 1
        var a_element_1 = document.createElement('a');
        a_element_1.className = __COOKIEJS_CLASSNAME_BANNER_LINK;
        a_element_1.href = '#';
        a_element_1.innerHTML = _ALLOW_ALL.get_translation();
        a_element_1.addEventListener('click', function(){ self.select_all_listener() });

        // Link 2
        var a_element_2 = document.createElement('a');
        a_element_2.className = __COOKIEJS_CLASSNAME_BANNER_LINK;
        a_element_1.style['color'] = __COOKIEJS_CSS_TEXT_COLOR_A;
        a_element_2.href = '#';
        a_element_2.innerHTML = _SET_PREFERENCES.get_translation();
        a_element_2.addEventListener('click', function(){ self.controller.modal.open() });

        //
        li_element_1.appendChild(a_element_1);
        li_element_2.appendChild(a_element_2);
        ul_element.appendChild(li_element_1);
        ul_element.appendChild(li_element_2);
        div_element.appendChild(h2_element);
        div_element.appendChild(p_element);
        div_element.appendChild(ul_element);
        element.appendChild(inline_style);
        element.appendChild(div_element);
        //
        return element;
    };
    this.element = this.get_element();
};


// ----------------------------------------------------------------------------
// Cookie footer
// ----------------------------------------------------------------------------

function __CookieJsFooter(controller){
    this.controller = controller;
    // element
    this.get_element = function(){
        var self = this;

        var _SHOW = __cookiejs_cookie_preferences_selected();

        var _HEADING = new __CookieJsTranslation(__COOKIEJS_TRANSLATION_FOOTER_HEADING);
        var _SET_PREFERENCES = new __CookieJsTranslation(__COOKIEJS_TRANSLATION_FOOTER_SET_PREFERENCES);

        var inline_style = document.createElement('style');
        inline_style.innerHTML = '.' + __COOKIEJS_CLASSNAME_FOOTER_WRAPPER + ' {';
        inline_style.innerHTML += 'font-family: ' + __COOKIEJS_CSS_DEFAULT_FONT + ' !important;';
        inline_style.innerHTML += 'background-color: ' + __COOKIEJS_CSS_BACKGROUND_COLOR_B + ' !important;';
        inline_style.innerHTML += 'padding: 20px 0px 30px 0px !important;';
        inline_style.innerHTML += 'width: 100% !important;';
        inline_style.innerHTML += 'color: ' + __COOKIEJS_CSS_TEXT_COLOR_B + ' !important;';
        inline_style.innerHTML += '}';
        inline_style.innerHTML += '.' + __COOKIEJS_CLASSNAME_FOOTER_HEADING + ' {';
        inline_style.innerHTML += 'color: ' + __COOKIEJS_CSS_TEXT_COLOR_B + ';';
        inline_style.innerHTML += 'font-size: 21px !important;';
        inline_style.innerHTML += 'font-weight: bold !important;';
        inline_style.innerHTML += 'margin: 0px !important;';
        inline_style.innerHTML += 'padding: 0px !important;';
        inline_style.innerHTML += 'padding-left: 20px !important;';
        inline_style.innerHTML += 'margin-bottom: 15px !important;';
        inline_style.innerHTML += 'border-width: 0px !important;';
        inline_style.innerHTML += '}';
        inline_style.innerHTML += '.' + __COOKIEJS_CLASSNAME_FOOTER + ' {';
        inline_style.innerHTML += 'width: ' + __COOKIEJS_CSS_MAX_WIDTH + ' !important;';
        inline_style.innerHTML += 'margin: auto !important;';
        inline_style.innerHTML += '}';
        inline_style.innerHTML += '.' + __COOKIEJS_CLASSNAME_FOOTER_UL + ' {';
        inline_style.innerHTML += 'margin: 0px !important;';
        inline_style.innerHTML += 'padding: 0px !important;';
        inline_style.innerHTML += 'padding-left: 20px !important;';
        inline_style.innerHTML += '}';
        inline_style.innerHTML += '.' + __COOKIEJS_CLASSNAME_FOOTER_LI + ' {';
        inline_style.innerHTML += 'display: inline-block !important;';
        inline_style.innerHTML += 'margin-right: 10px !important;';
        inline_style.innerHTML += '}';
        inline_style.innerHTML += '.' + __COOKIEJS_CLASSNAME_FOOTER_LINK + ' {';
        inline_style.innerHTML += 'background-color: ' + __COOKIEJS_CSS_BUTTON_COLOR_A + ' !important;';
        inline_style.innerHTML += 'padding: 10px !important;';
        inline_style.innerHTML += 'font-size: 16px !important;';
        inline_style.innerHTML += 'text-decoration: none;';
        inline_style.innerHTML += 'color: ' + __COOKIEJS_CSS_TEXT_COLOR_B + ' !important;';
        inline_style.innerHTML += '}';
        inline_style.innerHTML += '.' + __COOKIEJS_CLASSNAME_FOOTER_LINK + ':hover {';
        inline_style.innerHTML += 'color: ' + __COOKIEJS_CSS_TEXT_COLOR_B + ' !important;';
        inline_style.innerHTML += 'text-decoration: underline;';
        inline_style.innerHTML += '}';

        // Wrapper
        var element = document.createElement('div');
        element.className = __COOKIEJS_CLASSNAME_FOOTER_WRAPPER;
        element.style['display'] = 'none';
        if (_SHOW === true) { element.style.display = 'block' };

        // Content
        var div_element = document.createElement('div');
        div_element.className = __COOKIEJS_CLASSNAME_FOOTER;

        // Heading
        h2_element = document.createElement('h2');
        h2_element.className = __COOKIEJS_CLASSNAME_FOOTER_HEADING;
        h2_element.innerHTML = _HEADING.get_translation();

        // Unordered list
        var ul_element = document.createElement('ul');
        ul_element.className = __COOKIEJS_CLASSNAME_FOOTER_UL;
        ul_element.role = 'navigation';

        // List element 1
        var li_element_1 = document.createElement('li');
        li_element_1.className = __COOKIEJS_CLASSNAME_FOOTER_LI;

        // Link 1
        var a_element_1 = document.createElement('a');
        a_element_1.className = __COOKIEJS_CLASSNAME_FOOTER_LINK;
        a_element_1.href = '#';
        a_element_1.innerHTML = _SET_PREFERENCES.get_translation();
        a_element_1.addEventListener('click', function(){ self.controller.modal.open() });

        // Append children
        li_element_1.appendChild(a_element_1);
        ul_element.appendChild(li_element_1);
        div_element.appendChild(h2_element);
        div_element.appendChild(ul_element);
        element.appendChild(inline_style);
        element.appendChild(div_element);

        //
        return element;
    };
    this.element = this.get_element();
};


// ----------------------------------------------------------------------------
// Cookie plugin controller
// ----------------------------------------------------------------------------

function __CookieJsController(){
    this.modal = new __CookieJsPreferencesModal(this);
    this.banner = new __CookieJsBanner(this);
    this.footer = new __CookieJsFooter(this);
};


// ----------------------------------------------------------------------------
// Init
// ----------------------------------------------------------------------------

function __cookiejs_set_preferences_plugin(){

    if (window[__COOKIEJS_PREFERENCES_VARIABLE_NAME] === undefined) {
        window[__COOKIEJS_PREFERENCES_VARIABLE_NAME] = [];
    };

    // Gather init cookies
    window[__COOKIEJS_COOKIE_VARIABLE_NAME] = __cookiejs_get_cookie_as_json(__COOKIEJS_COOKIE_NAME);

    // init controller
    __COOKIESJS_CONTROLLER = new __CookieJsController();

    // Do dom manipulations
    var body = document.querySelectorAll('body')[0];

    if (body.insertBefore === undefined){
        // This code makes page flicker
        // < IE9 "fix"
        var existing_body_nodes = [].slice.call(body.children);

        body.innerHTML = '';

        body.appendChild(__COOKIESJS_CONTROLLER.banner.element);
        for (var i = 0; i < existing_body_nodes.length; i++){
            body.appendChild(existing_body_nodes[i])
        };
    } else {
        body.insertBefore(__COOKIESJS_CONTROLLER.banner.element, body.firstChild);
    }

    body.appendChild(__COOKIESJS_CONTROLLER.modal.element);
    body.appendChild(__COOKIESJS_CONTROLLER.footer.element);

    // Trigger callbacks for init script loading

    for (var i = 0; i < window[__COOKIEJS_PREFERENCES_VARIABLE_NAME].length; i++){
        window[__COOKIEJS_PREFERENCES_VARIABLE_NAME][i].trigger_callback();
    };

};


// ----------------------------------------------------------------------------
// Helper functions for developers
// ----------------------------------------------------------------------------

function __cookiejs_load_google_tagmanager(id){
    (function(w,d,s,l,i){
        w[l] = w[l] || [];
        w[l].push({'gtm.start': new Date().getTime(), event:'gtm.js'});
        var f = d.getElementsByTagName(s)[0];
        var j = d.createElement(s);
        var dl = l != 'dataLayer'?'&l='+l:'';
        j.async = true;
        j.src = 'https://www.googletagmanager.com/gtm.js?id='+i+dl;
        f.parentNode.insertBefore(j,f);
    })(window,document,'script','dataLayer',id)
}


function __cookiejs_load_google_analytics(id) {
    if(id.substring(0,2) === "UA"){
        var imported = document.createElement('script');
        imported.src = "https://www.googletagmanager.com/gtag/js?id=" + id;
        document.head.appendChild(imported);
        window.dataLayer = window.dataLayer || [];
        function gtag() {
            dataLayer.push(arguments);
        }
        gtag('js', new Date());
        gtag(
            'config',
            id,
            {
                'anonymize_ip': true,
                'cookie_domain': location.hostname,
            }
        );
    } else {
        __cookiejs_load_google_tagmanager(id);
    }
};


function __cookiesjs_add_placeholder(element){
    element.style['background-color'] = __COOKIEJS_CSS_BACKGROUND_COLOR_E;

    _TEXT = new __CookieJsTranslation(__COOKIEJS_TRANSLATION_IFRAME_TEXT);

    var a_element = document.createElement('a');
    a_element.href = '#';
    a_element.innerHTML = _TEXT.get_translation();
    a_element.style['z-index'] = 100000;
    a_element.style['position'] = 'absolute';
    a_element.style['font-weight'] = 'bold';
    a_element.addEventListener('click', function(){ __COOKIESJS_CONTROLLER.modal.open() });

    if (element.insertBefore !== undefined){
        element.parentNode.insertBefore(a_element, element)
    };

};


function __cookiejs_load_google_custom_search(id){
    (function () {
        var gcse = document.createElement('script');
        gcse.type = 'text/javascript';
        gcse.async = true;
        gcse.src = 'https://cse.google.com/cse.js?cx=' + id;
        var s = document.getElementsByTagName('script')[0];
        s.parentNode.insertBefore(gcse, s);
    })();
};


function __cookiejs_url_matches_patterns(url, patterns){
    for (var i = 0; i < patterns.length; i++){
        var regexp = new RegExp(patterns[i]);
        var matches = url.match(regexp);
        if (matches !== null){
            return true
        };
    };
    return false;
};


function __cookiejs_load_iframes(){
    var iframes = document.getElementsByTagName('iframe');
    for (var i = 0; i < iframes.length; i++){
        var src = iframes[i].getAttribute('data-src') || null;
        if (src !== null){
            iframes[i].src = src;
        }
    };
};


function __cookiejs_hide_iframes(array){
    var url_patterns_array = array || [];
    var iframes = document.getElementsByTagName('iframe');

    for (var i = 0; i < iframes.length; i++){

        var src = iframes[i].getAttribute('data-src') || null;
        var hide = false;

        if (url_patterns_array.length > 0 && src !== null){
            hide = __cookiejs_url_matches_patterns(src, url_patterns_array);
        }

        if (hide === true){
            __cookiesjs_add_placeholder(iframes[i]);
        } else {
            iframes[i].src = src;
        }

    };
};


function __cookiejs_init(){
    __cookiejs_set_preferences_plugin();
}

//window.addEventListener('load', __cookiejs_init)
