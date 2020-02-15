class Polygon {
  constructor(width, height) {
   var width = width;
   var height = height;
  }
}

class Rectangle extends Polygon {
  constructor(width, height) {
   super(width, height);
     this._color = '';
     this._area = this.height * this.width;
  }

  get area() {
    return this._area;
  }
  get color() {
    return this._color;
  }
  set color(value) {
    this._color = value;
  }
}

class Square extends Rectangle {
  constructor(side) {
    super(side, side);
    this._color = '';
  }

  get area() {
   return super.area;
  }
  get color() {
    return this._color;
  }
  set color(value) {
    this._color = value;
  }
}
let r1 = new Rectangle(2,3);

/* console message #1 */
console.log('area = ' + r1.area);

r1.color = 'red';

/* console message #2 */
console.log('color = ' + r1.color);

let s1 = new Square(10);

/* console message #3 */
console.log('square side = ' + s1.side);

/* console message #4 */
console.log('square area = ' + s1.area);

var gg = 1.5;
var hh = 0.2;
var x = Math.round(gg%hh * 100) / 100;
console.log(x, gg%hh);

function test(a, b) {
    return (a * b)+(a + b);
}

var a = 1;
var b = 2;
var c = test(a,b);
console.log(c)

console.log("The initial type of function = " + typeof tfunc);
function tfunc(I) {   }
console.log("The type of function after call = " + typeof tfunc);

var x = 3;
var y = 0;

function testY() {
    y++;
    return true;
}

if (x>=3 && testY()) { y++; }
if (x<3 || testY()) { y++; }
if (x<3 && testY()) { y++; }
if (x>=3 || testY()) { y++; }

var z = y;
console.log(z)


var message = 'This is a "' + 'message' + '"';

console.log(message)

var a = [99,87,,9,928374];

a.find(function(value, index) {
    if (index == 2) {
    delete a[2];
    }
    console.log(index);
});

function test(x, y)
{
    return (Math.sqrt(x*x + y*y));
}
function test2(x, y)
{
    return (x ^ y);
}
console.log(test2(test(3,4),3));