/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var uniquePaths = function(m, n) {
    let noOfPaths = new Array(n)
    noOfPaths.fill(1)
    for (let i = 1; i < m; i++) {
        let prev = 1
        for (let j = 1; j < n; j++) {
            noOfPaths[j] = prev + noOfPaths[j]
            prev = noOfPaths[j]
        }
    }
    return noOfPaths.pop()
};