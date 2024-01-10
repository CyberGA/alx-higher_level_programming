#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 1 && h > 1) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = this.height; i > 0; i--) {
      console.log('X'.repeat(this.width));
    }
  }
};
