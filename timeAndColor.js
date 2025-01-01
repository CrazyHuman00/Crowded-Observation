// 現在の日付を取得する
function getToday() {
    var today = new Date();
    var year = today.getFullYear();
    var month = today.getMonth() + 1;
    var week = today.getDay();
    var day = today.getDate();
    var week_ja = new Array("日", "月", "火", "水", "木", "金", "土");
    document.getElementById("date").innerHTML =
        year + "年" + month + "月" + day + "日 " + week_ja[week] + "曜日";
}

// 現在の時刻を取得する
function getTime() {
    var time = new Date();
    var hour = time.getHours();
    var minute = time.getMinutes();
    document.getElementById("time").innerHTML = hour + "時" + minute + "分";
}

// 混雑度合いによって背景色を変える
function updateTableColors() {
    const rows = document.querySelectorAll("#congestionTable .congestion");
    rows.forEach((row) => {
        const value = parseInt(row.textContent);
        if (value < 30) {
            row.className = "low";
        } else if (value < 50) {
            row.className = "medium";
        } else if (value < 79) {
            row.className = "high";
        } else {
            row.className = "super-high";
        }
    });
}

// 1秒ごとに日付と時刻を更新する
function updateTimeAndColor() {
    getToday();
    getTime();
    updateTableColors();
    setTimeout(updateTimeAndColor, 2000);
}
