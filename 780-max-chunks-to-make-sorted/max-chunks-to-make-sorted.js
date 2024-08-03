/**
 * @param {number[]} arr
 * @return {number}
 */
var maxChunksToSorted = function(arr) {
    let maxSeen = 0;
    let chunks = 0;

    for (let i = 0; i < arr.length; i++) {
        maxSeen = Math.max(maxSeen, arr[i]);
        if (maxSeen === i) {
            chunks++;
        }
    }

    return chunks;
};
