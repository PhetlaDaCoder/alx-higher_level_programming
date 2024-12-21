#!/usr/bin/node
const args = process.argv.slice(2);

if (process.args.length === 2) {
	console.log('No argument');
} else if (process.args.length === 3) {
	console.log('Argument found');
} else {
	console.log('Arguments found');
}
