#!/usr/bin/node
const count = process.argv;
if (process.argv[2] !== undefined) {
	console.log(process.argv[2]);
} else {
	console.log("No argument");
}
