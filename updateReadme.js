const fs = require('fs');
const https = require('https');

var arr = ["GFG_1", "GeeksForGeeks",
    "Geeks", "Computer Science Portal"
];

function readAndWrite() {
    const articles = `\n - [${arr[Math.floor(Math.random() * arr.length)]}]\n \n`;

    fs.readFile('README.md', 'utf-8', (err, data) => {
        if (err) {
            throw err;
        }
        const updatedMd = data.replace(
            /(?<=I'm writing:\n)[\s\S]*(?=\!\[Build)/gim,
            articles
        );

        fs.writeFile('README.md', updatedMd, 'utf-8', (err) => {
            if (err) {
                throw err;
            }
            console.log('README update complete.');
        });
    });
};

readAndWrite();