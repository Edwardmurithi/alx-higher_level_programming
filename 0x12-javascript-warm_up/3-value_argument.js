#!/usr/bin/node
const count = process.argv
if (typeof process.argv[2] === 'undefined') {
	console.log('No argument');
} else {
	console.log(process.argv[2]);
}

