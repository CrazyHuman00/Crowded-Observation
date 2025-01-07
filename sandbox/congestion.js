/** opencv.jsを使う */

function onOpenCvReady() {
    console.log('OpenCV.js is ready.');
    main();
}

// OpenCV.jsの読み込み
function loadImage(src, callback) {
    let img = new Image();
    img.crossOrigin = "Anonymous";
    img.onload = () => callback(img);
    img.src = src;
}


// 画像の比較
function compareImages(img1, img2) {
    let mat1 = cv.imread(img1);
    let mat2 = cv.imread(img2);
    let diff = new cv.Mat();
    cv.absdiff(mat1, mat2, diff);
    cv.cvtColor(diff, diff, cv.COLOR_RGBA2GRAY, 0);

    let congestion = updateCongestion(diff);

    let result = new cv.Mat();
    cv.threshold(diff, result, 50, 255, cv.THRESH_BINARY);
    cv.imshow('canvasOutput', result);
    mat1.delete();
    mat2.delete();
    diff.delete();
    result.delete();

    return congestion;
}


// 画像の差分を計算
function updateCongestion(diff) {
    let sum = 0;
    for (let i = 0; i < diff.rows; i++) {
        for (let j = 0; j < diff.cols; j++) {
            sum += diff.ucharPtr(i, j)[0];
        }
    }
    console.log(`Difference sum: ${sum}`);
    return sum;
}


// 混雑度を更新
function updateCongestionTable(congestion) {
    const table = document.getElementById('congestionTable');
    const rows = table.getElementsByTagName('tr');
    for (let i = 1; i < rows.length; i++) {
        const cells = rows[i].getElementsByTagName('td');
        const percentage = Math.min(100, Math.max(0, congestion % 100)); // 0-100の範囲に制限
        cells[2].innerText = `${percentage}%`;
    }
}

function main() {
    const image1Path = 'miyako2/S-HE2F-miya-2-1.jpg';
    const image2Path = 'miyako2/S-HE2F-miya-2-3.jpg';

    loadImage(image1Path, (img1) => {
        loadImage(image2Path, (img2) => {
            const congestion = compareImages(img1, img2);
            updateCongestionTable(congestion);
        });
    });

    setTimeout(main, 2000);
}