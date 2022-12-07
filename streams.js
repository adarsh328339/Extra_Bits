const fs = require('fs');
const server = require('http').createServer();

server.on("request", (req, res) => {
  //// Serving the file after reading it synchronously ///////

  /*fs.readFile("./test-file.txt", (err, data) => {
    if(err) console.log("error my lord");
    res.end(data)
  */

//// Using read stream to send the data using the server //////

/* const readable = fs.createReadStream('./test-file.txt');
readable.on('data', chunk => {
  res.write(chunk);
})

readable.on("end", () =>{
  res.end();
})

readable.on("error", err =>{
  console.log(err);
  res.statusCode = 500;
  res.end("Fixing the issue")

}) */

///// Using Pipe Operator to pass the output of readable stream to input of writable stream //////

const readable = fs.createReadStream('./test-file.txt');
readable.pipe(res);
});


server.listen(8000, '127.0.0.1', () =>{
  console.log("Listening on 8000");
});
