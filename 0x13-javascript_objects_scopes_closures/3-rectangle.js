#!/usr/bin/node
// a class Rectangle that defines a rectangle
module.exports = class Rectangle {
	constructor(w, h) {
		// if w or h is equal to 0 or not a positive integer, create an empty object
		if (w > 0 && h > 0) {
			this.width = w;
			this.height = h;
		}
	}
	print () {
		for (let x = 0; x < this.height; x++) {
			console.log('X'.repeat(this.width));
		}
	}
};
