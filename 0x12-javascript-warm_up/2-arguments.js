#!/usr/bin/node
const argCount = process.argv.length - 2;

if (argCount === 0) {
  console.log('No arguements');
} else if (argCount === 1) {
  console.log('Argument found');
} else if (argCount > 1) {
  console.log('Arguments found');
}
