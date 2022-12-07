const eventEmitter = require('events');

const myEmitter = new eventEmitter();

myEmitter.on("newSale", ()=>{
  console.log("Paisa aaya");
})

myEmitter.on("newSale", () =>{
  console.log("Adarsh hai bey");
})

myEmitter.on("demand", ()=>{
  console.log("Aanewala hai");
})

myEmitter.emit("newSale");
myEmitter.emit("demand");
myEmitter.emit("newSale");
