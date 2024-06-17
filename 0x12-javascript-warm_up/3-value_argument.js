#!/usr/bin/node
const arguments = process.argv;
console.log(typeof process.argv[2] !== undefined ? 'No argument' : process.argv[2]);
