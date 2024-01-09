#!/usr/bin/node
if (isNaN(process.argv[2])) console.log('Missing size');
else {
  for (let i = Number(process.argv[2]); i > 0; i--) {
    console.log('X'.repeat(process.argv[2]));
  }
}
