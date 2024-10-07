function getCookie(name) {
  var value = '; ' + document.cookie;
  var parts = value.split('; ' + name + '=');
  if (parts.length === 2) return parts.pop().split(';').shift();
}
window.plausible = window.plausible || function() { (window.plausible.q = window.plausible.q || []).push(arguments); }
function prepareUrl(params) {
  var url = new URL(location.href);
  var queryParams = new URLSearchParams(location.search);
  var customUrl = url.protocol + "//" + url.hostname + url.pathname.replace(/\/$/, '');
  for (var paramName of params) {
    var paramValue = queryParams.get(paramName);
    if (paramValue !== null) customUrl = customUrl + '/' + paramName + ':' + paramValue;
  }
  return customUrl
}
function trackPageView() {
  plausible('pageview', {u: prepareUrl(["nav", "tags", "both", "edit", "view", "template", "create-team", "create-paid-team", "signup"]) + window.location.search, props: {user_id: getCookie('userid'), logged_in: getCookie('loginstate')}});
}
trackPageView()
document.addEventListener('mousedown', function (e) {
  if (e.target && e.target.className && e.target.className.indexOf('ui-') !== -1) {
    plausible('ui_click', {props: {class_name: e.target.className, text: e.target.outerText ? e.target.outerText.substr(0, 200) : "", html: e.target.outerText ? e.target.outerHTML.substr(0, 200) : ""}});
  } else if (e.target && e.target.parentElement && e.target.parentElement.className && e.target.parentElement.className.indexOf('ui-') !== -1) {
    plausible('ui_click', {props: {class_name: e.target.parentElement.className, text: e.target.parentElement.outerText ? e.target.parentElement.outerText.substr(0, 200) : "", html: e.target.parentElement.outerText ? e.target.parentElement.outerHTML.substr(0, 200) : ""}});
  }
});
window.addEventListener('popstate', function (e) {
  trackPageView();
});
window.history.pushState = new Proxy(window.history.pushState, {
  apply: (target, thisArg, argArray) => {
    setTimeout(function () {
      trackPageView();
    }, 1);
    return target.apply(thisArg, argArray);
  },
});
