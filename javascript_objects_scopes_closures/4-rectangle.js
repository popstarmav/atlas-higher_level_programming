#!/usr/bin/node

class Rectangle {
  constructor (width, height) {
    if (width <= 0 || height <= 0) {
      this.width = null;
      this.height = null;
    } else {
      this.width = width;
      this.height = height;
    }
  }

  print () {
    if (this.width === null && this.height === null) return;

    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    if (this.width !== null && this.height !== null) {
      const aux = this.width;
      this.width = this.height;
      this.height = aux;
    }
  }

  double () {
    if (this.width !== null && this.height !== null) {
      this.width *= 2;
      this.height *= 2;
    }
  }
}

module.exports = Rectangle;
