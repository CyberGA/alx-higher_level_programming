#!/usr/bin/node

const { argv } = process;
const argc = argv.length - 2;

if (argc <= 1) console.log(0);
else {
  const argss = [];
  for (let i = 2; i < argv.length; i++) {
    argss.push(Number(argv[i]));
  }
  argss.sort((a, b) => b - a);
  console.log(argss[1]);
}
