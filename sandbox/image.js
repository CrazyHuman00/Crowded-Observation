/* 画像を保存する */
const https = require('https');
const fs = require('fs');
const path = require('path');

// 画像を保存する
function downloadImage(url, filepath) {
    const file = fs.createWriteStream(filepath);

    https.get(url, (response) => {
        response.pipe(file);
        file.on('finish', () => {
            file.close();
            console.log(`Downloaded and saved: ${filepath}`);
        });
    }).on('error', (err) => {
        fs.unlink(filepath);
        console.error(`Error downloading image: ${err.message}`);
    });
}

// 3分毎に画像をダウンロードする関数
function startDownloading(url, filepath, interval) {
    setInterval(() => {
        downloadImage(url, filepath);
    }, interval);
}


// function main() {
//     const yasaiImageUrl = process.env.YASAI_URL;
//     const miyakoImageUrl = process.env.MIYAKO_1_URL;
//     const miyakoImageUrl2 = process.env.MIYAKO_2_URL;
//     const FUJI_1_URL = process.env.FUJI_1_URL;
//     const MUSUBI_1_URL = process.env.MUSUBI_1_URL;
//     const MUSUBI_2_URL = process.env.MUSUBI_2_URL;
//     const ICHIBARIKI_URL = process.env.ICHIBARIKI_URL;


//     //const interval = 3 * 60 * 1000;
//     const interval = 60;

//     startDownloading(yasaiImageUrl, path.join(__dirname + '/yasai', 'yasai.jpg'), interval);
//     startDownloading(miyakoImageUrl, path.join(__dirname + '/miyako1', 'miyako1.jpg'), interval);
//     startDownloading(miyakoImageUrl2, path.join(__dirname + '/miyako2', 'miyako2.jpg'), interval);
//     startDownloading(FUJI_1_URL, path.join(__dirname + '/fujikatsu', 'fuji1.jpg'), interval);
//     startDownloading(MUSUBI_1_URL, path.join(__dirname + '/musubi1', 'musubi1.jpg'), interval);
//     startDownloading(MUSUBI_2_URL, path.join(__dirname + '/musubi2', 'musubi2.jpg'), interval);
//     startDownloading(ICHIBARIKI_URL, path.join(__dirname + '/ichibariki', 'ichibariki.jpg'), interval);
// }