// Finding the union and intersection of two arrays using JavaScript 

arr1 = [1,2,3,4,5,6]
arr2 = [3,4,5,7]

const arr_intersect = arr1.filter((ele) => {
    return arr2.includes(ele)
})
console.log('This is the intersection of the array:-', arr_intersect)

const arr_union = [...new Set([...arr1, ...arr2])]

console.log('This is the union of the arrays:-', arr_union)

// Set-Timeout :- 
/* Between a set-Timeout with 0ms as time and a console.log, A console.log would always be executed first cuz setTimeout() is handled by event loop. */

// Shocking Inner Details:- 

console.log(400.4 === 200.2*2) // Gives output True
console.log(900.9 === 300.3*3) // Gives output False

/* This is due to the fact because JS uses IEEE-754 standards for mathematical operations. It treats decimals as floating point numbers. 
 It uses 64-bit floating point numbers and thus might lead to such precision checks. After all, Decimal is a 10-bit representation and computers use Binary
 which is a 2-bit representation. A simple hack could be writing the second statement as */ 
console.log((900.9 === 300*10*3)/10) 

/* Datatypes:- Primitive Datatypes are the ones which are not objects and have no methods defined on them. They are stored as values and are immutable while
               Non-Primitive Datatypes are the ones which are objects and are stored by reference and have methods defined on them. They are mostly mutable. */

// Detecting Arrays cuz they are still objects uk :- 

console.log(typeof([])) // Gives object as an output cuz arrays are still non-primitive and an object basically
console.log([] instanceof Array) // Gives true cuz instance of is a method to check. We can also use Array.isArray method here

// Strings vs Objects :- 

let myName = "Adarsh";
let channelName = myName;

myName = "Rohit"
console.log(channelName) // Gives Adarsh as an output. Since string is a primitive datatype, pass by value acts here and once the value is passed nothing matters.
// While in the case of an object and its methods, reference is passed and thus updating the original variable will also update the new one being talked about.


// Objects once again:- 

let arrName = [ {"Name" : "Adarsh", "lname" : "Dubey"}, {"Name" : "Rohit", "lname" : "Bansal"}]
console.log(arrName.indexOf({"Name" : "Rohit", "lname" : "Bansal"}) // Gives -1. 
/* Since indexOf gives -1 when it can't find the desired value. But here, instead of passing the same value its giving -1 cuz we've passed an object and thus 
the reference is passed and hence its searching by reference and so two objects cannot be equal (And they never are in JS) and hence -1 */
			
// Non-Primitive and pass by ref once again:- 
let arr1 = [1,2,3]
let arr2 = arr1;
arr2.push(4)

console.log(arr1) // Gives [1,2,3,4] Since we did pass the reference to arr1, modifying arr2 changed arr1 as well
console.log(arr2) // Gives [1,2,3,4] 

// Equality and Strict-Equality:- 
let a = 5;
let b = "5";
console.log(a == b) /* Gives True inspite of one being string and one a number. It is because JS does inherently convert the datatype to match each other
    before a comparision assignment. While if === would have been used, it would have returned false as it checks the datatype too and doesn't convert. */

// Hoisting :- 

var myName = "Adarsh"

const newName = () => {
  console.log(myName)     //Gives undefined (Due to hoisting of variable and thus no definite value)
  var myName = "Dubey"
  console.log(myName)    // Gives Dubey  (Variable gets redefined with value Dubey)
}
console.log(myName)      // Gives Adarsh (Runs before even the function is executed)
newName();
console.log(myName)      /* Gives Adarsh since the redifining was done to a varibale created with var keyword inside the function. Would have given Dubey if
 var keyword would not have been used in defining the myName keyword inside the function */ 

// Console.time() and Console.timeEnd() are two methods which can be used to monitor the time taken by the program to execute. 







               



    
