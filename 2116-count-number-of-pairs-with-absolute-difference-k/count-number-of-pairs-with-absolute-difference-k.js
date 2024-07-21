/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var countKDifference = function(nums, k) {
    let count = 0;
    for (let i = 0; i < nums.length; i++) {
        for (let j = i + 1; j < nums.length; j++) {
            let difference = nums[i] - nums[j];
            if (difference < 0) {
                difference = -difference;
            }

            if (difference === k) {
                count++;
            }
        }
    }
    return count;
};