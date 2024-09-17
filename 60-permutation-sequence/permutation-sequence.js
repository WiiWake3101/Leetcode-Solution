/**
 * @param {number} n
 * @param {number} k
 * @return {string}
 */
var getPermutation = function (n, k) {
  const a = {0: 1};
  let arr = [];
  for (let i = 1; i <= n; i++) {
    arr.push(i);
    a[i] = a[i - 1] * i;
  }
  const b = [];
  k--;
  while (arr.length > 0) {
    const c = arr.length - 1;
    let de = Math.floor(k / a[c]);
    b.push(arr[de]);
    arr.splice(de, 1);
    const remainder = k % a[c];
    k = k % a[c];
  }

  return b.join("");
};