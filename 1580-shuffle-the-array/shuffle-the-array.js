/**
 * @param {number[]} nums
 * @param {number} n
 * @return {number[]}
 */
var shuffle = function(nums, n) {
    var result = new Array(2 * n);
    var index = 0;
    for (var i = 0; i < n; i++) {
        result[index] = nums[i];
        index++;
        result[index] = nums[i + n];
        index++;
    }
    return result;
};