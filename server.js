const express = require('express');
const { exec } = require('child_process');
const cron = require('node-cron');
const app = express();
const port = 3000;

// 定期実行のスケジュール設定（例：11時30分から14時30分まで3分毎で実行）
cron.schedule('*/3 11-14 * * *', () => {
    const currentHour = new Date().getHours();
    const currentMinute = new Date().getMinutes();
    if (currentHour === 11 && currentMinute < 30) return;
    if (currentHour === 14 && currentMinute > 30) return;

    console.log('Running scheduled task');
    exec('python py/main.py', (error, stdout, stderr) => {
        if (error) {
            console.error(`Error executing Python script: ${error.message}`);
            return;
        }
        if (stderr) {
            console.error(`Python script error: ${stderr}`);
            return;
        }
        console.log(`Python script output: ${stdout}`);
    });
});

app.get('/', (req, res) => {
    exec('python py/main.py', (error, stdout, stderr) => {
        if (error) {
            console.error(`Error executing Python script: ${error.message}`);
            return res.json({ success: false });
        }
        if (stderr) {
            console.error(`Python script error: ${stderr}`);
            return res.json({ success: false });
        }
        console.log(`Python script output: ${stdout}`);
        res.json({ success: true });
    });
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});