#!/usr/bin/node

try {
	const request = require('request');
	console.log('Request module available');
} catch (err) {
	console.log('Request module missing');
}
