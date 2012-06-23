// Configuration settings for Ericom AccessNow
var defaults = {
    overrideSaved: false,               // These settings override saved user settings
//     onlyHTTPS: true,                 // Don't use WebSockets - go straight to HTTPS 
//     noHTTPS: true,                   // Don't allow using HTTPS instead of WebSockets (HTTPS requires Ericom Secure Gateway)
    autostart: false,                   // Start session automatically
    oldStyleProtocol: false,            // Set to true to use version 1.0 protocol
    singlePort: true,
    wsport: 8080,                       // AccessNow Server port
    gwport: 443,                        // Ericom Secure Gateway port
    showAddress: false,                  // Show server address in error dialogs
    dialogTimeoutMinutes: 2,            // Dialog timeouts
    sessionTimeoutMinutes: 0,           // Zero disables feature
    hiddenUpdateRateSeconds: 20,
    keepAliveRateSeconds: 30,
    executeTimeout: 1000,
    minSendInterval: 100,
    clipboard: true,
    clipboardTimeoutSeconds: 15,
    clipboardUseFlash: true,
    clipboardKey: 12,                   // Key to open clipboard paste dialog. Set to false to disable
    printing: true,
    fileDownload: true,
    fileUpload: true,
    specialKeys: true,                  // See http://support.microsoft.com/kb/186624
    chromeKeys: true,
    rightToLeft: false,
    noEndDialog: false,                 // Do not display end of session dialog
//     message: "",
    leaveMessage: "Leaving this page will disconnect Ericom AccessNow",
//     keyboard_locale: "00000409",
//     convert_unicode_to_scancode: true,
//     endURL: "",                      // URL to go to when session has ended (# value closes window; ^ prefix to assign to window instead of top)
//     address: "",                     // address of AccessNow server 
//     full_address: "",                // address of RDP host
//     username: "",
//     password: "",                    // plain text
//     domain: "",
//     remember: false,                 // password
//     encryption: false,
//     blaze_acceleration: true,
//     blaze_image_quality: 40,
//     resolution: "1024,768",
//     use_gateway: false,
//     gateway_address: "",
//     audiomode:0,
//     remoteapplicationmode: false,
//     alternate_shell: "",             // startup application
//     shell_working_directory: "",
//     console: false,
//     settingsURL: "resources/blaze.txt", // URL from which to download connection settings
//     hidden: "remember",                 // Advanced button is showAdvanced
//     restrictHost: "127.*,localhost",
    _last: 0
};
