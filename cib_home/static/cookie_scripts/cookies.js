$(function () {
	var GA_TRACKING_ID = 'GTM-5ZLL77G';
	var PREFERENCES_TIMEOUT = 365;
	function _delete_analytics_cookies() {
		__cookiejs_delete_cookie('_ga');
		__cookiejs_delete_cookie('_gid');
		__cookiejs_delete_cookie('_gat');
		__cookiejs_delete_cookie('_gat([^=]+)');
	}

	var analytics_cookies = __cookiejs_get_cookie("analytics_cookies");
	if (analytics_cookies === "true") {
		$("#cookiecheck").prop('checked', true);
		__cookiejs_load_google_analytics(GA_TRACKING_ID);
	} else if (analytics_cookies === "false") {
		_delete_analytics_cookies();
		$("#cookiecheck").prop('checked', false);
	} else {
		$("#cookies-banner").show();
	}
	$("#accept-cookies-btn").click(function () {
		__cookiejs_set_cookie("analytics_cookies", true, PREFERENCES_TIMEOUT);
		$("#cookies-banner").hide();
	});
	$("#save-cookies-btn").click(function () {
		analytics_cookies = $("#cookiecheck").is(":checked");
		__cookiejs_set_cookie("analytics_cookies", analytics_cookies, PREFERENCES_TIMEOUT);
		if (analytics_cookies)
			__cookiejs_load_google_analytics(GA_TRACKING_ID);
		else
			_delete_analytics_cookies();
		$("#cookies-banner").hide();
	});
});
