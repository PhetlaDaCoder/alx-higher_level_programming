#!/usr/bin/node
const dict = require('./101-data').dict;

const total_list = Object.entries(dict);
const vals = Object.values(dict);
const valsUniq = [...new Set(vals)];
const newDict = {};
for (const j in valsUniq) {
  const list = [];
  for (const k in total_list) {
    if (totalist[k][1] === valsUniq[j]) {
      list.unshift(total_list[k][0]);
    }
  }
  newDict[valsUniq[j]] = list;
}
console.log(newDict);
