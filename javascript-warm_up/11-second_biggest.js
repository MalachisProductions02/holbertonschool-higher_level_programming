#!/usr/bin/node
function secondBiggest(nums) {
    if (nums.length < 2) return 0;
  
    let max = -Infinity;
    let secondMax = -Infinity;
  
    for (const num of nums) {
      if (num > max) {
        secondMax = max;
        max = num;
      } else if (num > secondMax && num < max) {
        secondMax = num;
      }
    }
  
    return secondMax === -Infinity ? 0 : secondMax;
  }
  
  const args = process.argv.slice(2).map(n => parseInt(n, 10));
  console.log(secondBiggest(args));
  