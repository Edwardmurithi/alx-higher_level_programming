#!/usr/bin/node
const arguments = process.argv;
// check if argument exists and printing it
if (process.argv[2] !== undefined) {
	console.log(process.argv[2]);
} else {
	console.log('No argument');
}
