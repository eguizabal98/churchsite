/******/ (() => { // webpackBootstrap
var __webpack_exports__ = {};
const updateDate = () => {
    const date = new Date();
    let dayNum = date.getDay();
    let differenceToSunday = 0;
    let differenceToLastSunday = 0;
    if (dayNum >= 0) {
        differenceToSunday = Math.abs(7 - dayNum);
        differenceToLastSunday = Math.abs(0 - dayNum);
    }
    const sundayDate = new Date(date.getFullYear(), date.getMonth(), date.getDate() + differenceToSunday);
    document.getElementById("nextEvent").textContent = sundayDate.toLocaleDateString('en-US');

    const pastSundayDate = new Date(date.getFullYear(), date.getMonth(), date.getDate() - differenceToLastSunday);
    document.getElementById("lastEvent").textContent = pastSundayDate.toLocaleDateString('en-US');
}
updateDate();


var reqURL = "https://api.rss2json.com/v1/api.json?rss_url=" + encodeURIComponent("https://www.youtube.com/feeds/videos.xml?channel_id=");

function loadVideo() {
    $.getJSON(reqURL + "UC3dKXfaGzFL_YvslCMCUtdg",
        function(data) {
            var videoNumber = 0;
            var title=data.items[videoNumber].title;
            document.getElementById("lastEvent-title").innerText = title;
        }
    );
}

loadVideo()

/******/ })()
;