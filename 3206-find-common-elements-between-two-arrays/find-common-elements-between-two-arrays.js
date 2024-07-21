/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var findIntersectionValues = function(nums1, nums2) {
    let count1 = 0;
    let count2 = 0;
    for (let i = 0; i < nums1.length; i++) {
        if (nums2.includes(nums1[i])) {
            count1++;
        }
    }
    for (let j = 0; j < nums2.length; j++) {
        if (nums1.includes(nums2[j])) {
            count2++;
        }
    }
    let answer = [count1, count2];
    return answer;
};