const fs = require ("fs");
const crypto = require("crypto");
const start = Date.now()
process.env.UV_THREADPOOL_SIZE = 4;

setTimeout(() => console.log("Timer 1 finished"), 0);
setImmediate(() => console.log("Immediate 1 finished"));

fs.readFile('./test-file.txt', () =>{
  console.log("I/O finished");

  setTimeout(() => console.log("Timer 2 finished"), 0);
  setTimeout(() => console.log("Timer 3 finished"), 3000);
  setImmediate(() => console.log("Immediate 2 finished"));

  process.nextTick(() => {
    console.log("Process.next running");
  })
////Crypto Module//////

  crypto.pbkdf2("password", "salt", 100000, 1024, "sha512", ()=>{
    console.log(Date.now() - start, "Encryption Done");
  })

  crypto.pbkdf2("password", "salt", 100000, 1024, "sha512", ()=>{
    console.log(Date.now() - start, "Encryption Done");
  })


})

console.log("Hey from the top level code");
