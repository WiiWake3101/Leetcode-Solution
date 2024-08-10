/**
 * @param {number[]} nums
 * @return {number}
 */
var firstMissingPositive = function (nums) {
    const numsLength = nums.length;
    let i = 0;
    while (i < numsLength) {
        const valAtI = nums[i] - 1;
        const belongsInRange =
            valAtI >= 0 && valAtI < numsLength;
        const isAtWrongIndex = nums[i] !== nums[valAtI];

        if (belongsInRange && isAtWrongIndex) {
            [nums[i], nums[valAtI]] = [nums[valAtI], nums[i]];
        } else {
            i++;
        }
    }
    for (let x = 0; x < numsLength; x++) {
        if (x + 1 !== nums[x]) {
            return x + 1;
        }
    }
    return numsLength + 1;
};