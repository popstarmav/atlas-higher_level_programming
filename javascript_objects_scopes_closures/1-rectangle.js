#!/usr/bin/node
class Rectangle {
    constructor (w, h) {
      this.width = w;
      this.height = h;
    }
  
    print () {
      console.log(`
        Instance width: ${this.width} - height: ${this.height}`);
    }
  }
  
  module.exports = Rectangle;