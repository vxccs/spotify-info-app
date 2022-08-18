// hide the destination url from the status bar
$(function () {
  $("a.hidelink").each(function (index, element) {
    var href = $(this).attr("href");
    $(this).attr("hiddenhref", href);
    $(this).removeAttr("href");
  });
  $("a.hidelink").click(function () {
    url = $(this).attr("hiddenhref");
    window.open(url, "_self");
  });
});

// disable contextmenu and interaction with images
$(function () {
  $("img").on("contextmenu", function (e) {
    return false;
  });
  $("img").mousedown(function (e) {
    e.preventDefault();
  });
});

// resize full height on mobile
function appHeight() {
  const doc = document.documentElement;
  doc.style.setProperty("--vh", window.innerHeight * 0.01 + "px");
}

window.addEventListener("resize", appHeight);
appHeight();
