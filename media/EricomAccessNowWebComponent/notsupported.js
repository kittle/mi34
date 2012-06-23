var appName = location.search.substring(1) || "start";
if ("WebSocket" in window || "MozWebSocket" in window)
    location.replace(appName + ".html");

$(function () {
    if (appName === "view") {
        document.title = "AccessNow&trade; for VMware View&trade;";
        $(".title").html(document.title);
    }
    $("#support").append(message(browser())).show();
});

function browser() {
    var match, result = {}, ua = navigator.userAgent;
    do {
        match = ua.match(/^Opera.+Version.(.+)$/);
        if (match !== null) {
            result.name = "Opera";
            break;
        }

        match = ua.match(/Chrome.(\S+)/);
        if (match !== null) {
            result.name = "Chrome";
            break;
        }

        match = ua.match(/Version.(\S+)\sSafari/);
        if (match !== null) {
            result.name = "Safari";
            break;
        }

        match = ua.match(/Firefox.(\S+)/);
        if (match !== null) {
            result.name = "Firefox";
            break;
        }

        match = ua.match(/MSIE (\S+)/);
        if (match !== null) {
            result.name = "Internet Explorer";
            break;
        }

        match = ua.match(/\sMobile\s/);
        if (match !== null) {
            result.name = "Mobile";
            break;
        }

        result.name = "unknown";
    } while (false);
    result.version = match && match.length > 1 ? parseFloat(match[1]) : 0;
    return result;
}

var message = (function () {
    var msgs = {
        'Chrome': function (version) {
            return 'You are using an older version of Google Chrome (version ' + version + ') that does not support <a href="http://en.wikipedia.org/wiki/WebSockets">HTML5 WebSockets</a>. ' +
            'Please <a href="http://www.google.com/chrome">upgrade to the latest version of Google Chrome</a>.';
        },

        'Safari': function (version) {
            return 'You are using an older version of Apple Safari (version ' + version + ') that does not support <a href="http://en.wikipedia.org/wiki/WebSockets">HTML5 WebSockets</a>. ' +
                'Please <a href="http://www.apple.com/safari/">upgrade to the latest version of Apple Safari</a>.';
        },

        'Firefox': function (version) {
            return 'You are using an older version of Firefox web-browser (version ' + version + ') that does not support <a href="http://en.wikipedia.org/wiki/WebSockets">HTML5 WebSockets</a>.<br />' +
                '<a href="http://www.mozilla.com/">Please upgrade to Firefox 6 or later.</a>.';
        },

        'Internet Explorer': function () {
            return isCanvasSupported() ?
                'You are using Microsoft Internet Explorer, which does not natively support <a href="http://en.wikipedia.org/wiki/WebSockets">HTML5 WebSockets</a>. ' +
                'Use the Ericom Secure Gateway to connect using HTTPS, or install <a href="http://code.google.com/chrome/chromeframe/">Google Chrome Frame</a>.' :
                'You are using Microsoft Internet Explorer.' +
                'To use Microsoft Internet Explorer please install <a href="http://code.google.com/chrome/chromeframe/">Google Chrome Frame</a>.';
        },

        'Opera': function (version) {
            return version >= 11 ?
                'Opera version ' + version + ' disables <a href="http://en.wikipedia.org/wiki/WebSockets">HTML5 WebSockets</a> by default.<br />' +
                'Use the Ericom Secure Gateway to connect using HTTPS<br />' +
                'Or enable WebSockets:<ol>' +
                    '<li>Type <strong>opera:config</strong> in the Address field.</li>' +
                    '<li>In the Quick find box type: <strong>websocket</strong></li>' +
                    '<li>Enable the checkbox</li>' +
                    '<li>Click on the Save button</li>' +
                    '<li>Close the browser (all windows / tabs) and launch it again</li>' +
                '</ol>Note that browser updates may reset these values.' :
                'You are using an older version of Opera web-browser (version ' + version + ') that does not support <a href="http://en.wikipedia.org/wiki/WebSockets">HTML5 WebSockets</a>.<br />' +
                '<a href="http://www.opera.com/">Please upgrade to the latest version of Opera</a>.';
        },

        'Mobile': function () {
            return isCanvasSupported() ?
                'This mobile browser does not support <a href="http://en.wikipedia.org/wiki/WebSockets">HTML5 WebSockets</a>.<br />' +
                'Use the Ericom Secure Gateway to connect using HTTPS.' :
                'You are using an unsupported mobile device.';
        },

        'unknown': function () {
            return 'You are using an unsupported web-browser. ' +
            'For this product to work you must use a different web-browser such as the latest versions of <a href="http://www.google.com/chrome">Google Chrome</a> or <a href="http://www.apple.com/safari/">Apple Safari</a>.';
        }
    };
    return function (b) {
        return msgs[b.name](b.version);
    };
})();

function isCanvasSupported() {
    var elem = document.createElement('canvas');
    return !!(elem.getContext && elem.getContext('2d'));
}
