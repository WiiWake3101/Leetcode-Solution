/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var uniquePaths = function(m, n) {
    let a = Array(n).fill(1);
    for (let i = 1; i < m; i++) {
        let b = Array(n).fill(1);
        for (let j = 1; j < n; j++) {
            b[j] = b[j - 1] + a[j];
        }
        a = b;
    }
    return a[n - 1]; 
};