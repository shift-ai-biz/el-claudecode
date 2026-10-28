const { convertLength, convertWeight, celsiusToFahrenheit } = require("./converter");

console.log("1.5 km =", convertLength(1.5, "km", "m"), "m");
console.log("200 g =", convertWeight(200, "g", "kg"), "kg");
console.log("25 C =", celsiusToFahrenheit(25), "F");
