/**
 * @param {number[]} arr
 * @return {number}
 */
var maxChunksToSorted = function(arr) {
    let max = 0;
    let count =0;
    for(let i=0;i<arr.length;i++){
        max = Math.max(arr[i],max);
        if(i === max){
            count++;
        }
    }
    return count;
};