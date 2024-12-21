#!/usr/bin/node
const arg = process.argv.slice(2);

if (process.arg.length === 2) {
	console.log('No argument');
} else if (process.arg.length === 3) {
	console.log('Argument found');
} else {
	console.log('Arguments found');
}
