/**
 * @param {number[]} candies
 * @param {number} extraCandies
 * @return {boolean[]}
 */
var kidsWithCandies = function(candies, extraCandies) {
    let X = 0;
    for (let i = 0; i < candies.length; i++) {
        if (candies[i] > X) {
            X = candies[i];
        }
    }
    const result = [];
    for (let i = 0; i < candies.length; i++) {
        if (candies[i] + extraCandies >= X) {
            result.push(true);
        } else {
            result.push(false);
        }
    }
    return result;
};