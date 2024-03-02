#!/usr/bin/node
// a class Rectangle that defines a rectangle
module.exports = class Rectangle {
	constructor(w, h) {
		if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
		// If w or h is equal to 0 or not a positive integer, create an empty object
		return {};
		}
		// Initialize instance attributes width and height
		this.width = w;
		this.height = h;
	}
}
