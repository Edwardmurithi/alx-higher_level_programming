#!/usr/bin/node

let number_args = process.argv.length - 2;

if (number_args === 0) {
	console.log("No argument");
} else if(number_args === 1) {
	console.log("Argument found");
} else {
	console.log("Arguments found");
}
