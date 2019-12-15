"use strict"
// Source : https://medium.com/@bretcameron/9-javascript-interview-questions-48416366852b

// 4. How Does a Function Expression Differ from a Function Declaration?

// Function declaration
// Function declaration is hoisted 
// Which means it moves to the top of their scope
// So you can declare function anywhere in your code 
// function sum(x, y) {
//     return x + y;
// }

// Function Expression: ES5
// Not hoisted
// Can be called only in linear sequence
var sum = function(x, y) {
  return x + y;
}

sum = function(x, y) {
    return x * y * 100
}

console.log(sum(2,5))

// // Function Expression: ES6+
// const sum = (x, y) => {
//     return x + y;
// }

// 5. What are the differences between var, let and const?
// 1) Assignment
// - "let" and "var" can be re-assigned where "const" cannot
// - "const" is the variable for functions or values that don't have to change
// - "const" allows for variable mutation.
//     - if it represents an array or Object, it can change

const arr1 = ["hello", "world"];
// Cannot re assign
// arr1 = [ 'hello', 'world', 'hamin' ]

// But can mutate
arr1.push("Dog", "Cat")
// Remove specific part of the array
arr1.splice(0,1)

const str1 = "hello";

const str2 = " world";

let res = str1.concat(str2);

console.log(res);

res = res.replace("world", "Hamin");

console.log(res)

console.log(arr1)

// 2) Hoisting
// let and var called inside a function is overriden globally when re-assigned
// but let is not hoisted to the top
// 

// 3) Scope
// - var => function-scoped
// - let and const are block-scoped
//     - block is within {} => functions, conditional statements, loops
var a = 0; 
let b = 0;
const c = 0;
if (true) {
  var a = 1; // function scoped
  let b = 1; // block scoped
  const c = 1;
}
console.log(a); // 1
console.log(b); // 0
console.log(c); // 0

// 6. What happens if you assign a variable without a keyword?
// hamin = 1
// console.log(typeof(hamin))
// It is window.hamin = 1 => causes memeory leak
// To prevent this "use strict" mode => introduced in ES5

// 7. What’s the difference between Object Oriented Programming (OOP) and Functional Programming (FP)?
function Student(number, name, age){
    this.number = number;
    this.name = name;
    this.age = age;
}

const s1 = new Student(10000, 'hamin', 15);

const s2 = new Student(2000, 'hdamin', 15);


console.log(Student[1]);
console.log(s1, s2)

const num1 = 1000;
const num2 = 1000;

console.log(10 == 10);
console.log(10 === 10);

// Functional Programming
// FP is based around the concept of “pure functions”, which avoid shared state, mutable data and side-effects
const num = {
  val: 1
}; 

const add5 = () => Object.assign({}, num, {val: num.val + 5}); 
const multiply5 = () => Object.assign({}, num, {val: num.val * 5}); 

console.log(add5(num).val)


console.log(num.val)

// 8. What’s the difference between imperative and declarative programming?
// FP is an example of declarative programming and OOP is an example of impertive programming

// OOP => impertive concerned with how you do something
    // -> for, while loops, if and switch statements
const sumTwoArray = (array, array2) => {
  let result = 0;
  for (let i = 0; i < array.length; i++) { 
    result += array[i] + array2[i];
  }; 
  return result;
}

console.log(sumTwoArray([1,2,3], [4,5,6]));

// Delcarative => concerned with **what** to do
//          => Often results in more consise code
const sumArray = (array, arr1) => {
    return array.reduce((x,y) => x + y) + arr1.reduce((x,y)=> x+ y);
}

console.log(sumArray([1,2,3,55,66,77], [4,5,6]));

// 9. What is Prototype-Based Inheritance?
// Array ops map, reduce, splice
// JS OOP uses prototype based inheritence
// function Person() {};
// Person.prototype.name = "hamin";
// Person.prototype.age = 23;
// console.log(Person.prototype);
// Person.prototype.name = "nana";
// Person.prototype.age = 244;
// console.log(Person.prototype);

// DONT override prototype => write function or class that inherits this concept

// p1 = new Person();
// console.log(p1)
console.log(77 == '77')
console.log(77 === '77')