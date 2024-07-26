#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2];
const stringToWrite = process.argv[3];

fs.writeFile(filePath, stringToWrite, 'utf-8', (err) => {
    if (err) {
        console.error(`{ 
            Error: ${err.code}: ${err.message}\n  at Error (native)\n  
            errno: ${err.errno},\n  code: '${err.code}',\n  
            syscall: '${err.syscall}',\n  
            path: '${err.path}' 
}`);
        return;
    }
});
