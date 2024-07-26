#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2];

fs.readFile(filePath, 'utf-8', (err, data) => {
    if (err) {
        console.error({
            message: err.message,
            errno: err.errno,
            code: err.code,
            syscall: err.syscall,
            path: err.path
        });
        return;
    }
    console.log(data);
});
