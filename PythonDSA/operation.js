//  O(1) – Constant Time
let arr = [10, 20, 30];
console.log(arr[0]);   // Always takes same time


// O(n) – Linear Time
for (let i = 0; i < arr.length; i++) {
    console.log(arr[i]);
}


// O(k) – Depends on a Fixed Value
for (let i = 0; i < 10; i++) {
   console.log(i);
}