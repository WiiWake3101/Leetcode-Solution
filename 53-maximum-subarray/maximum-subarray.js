/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(numbers) {
    let max = numbers[0];
    let cur = numbers[0];
    for (let i = 1; i < numbers.length; i++) {
        const value = numbers[i];
        if (cur + value >= value) {
            cur += value;
        } else {
            cur = value;
        }

        max = Math.max(cur, max);
    }

    return max;
};