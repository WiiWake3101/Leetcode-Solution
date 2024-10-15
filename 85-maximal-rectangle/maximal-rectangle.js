/**
 * @param {character[][]} matrix
 * @return {number}
 */
var maximalRectangle = function(matrix) {
   let maximalRectangle = 0
    let line = new Array(matrix[0].length).fill(0)
    for(let i=0; i< matrix.length; i++){
         for(let j=0;j<line.length;j++){
            if(matrix[i][j]==0)line[j]=0
            else line[j]+=+matrix[i][j]
         }
         for(let j=0; j<line.length;j++){
            let lineMaximal = line[j]
            if(lineMaximal*line.length>maximalRectangle){
                let left=j
                while(line[--left]>=line[j]);
                left++

                let right=j
                while(right<line.length && line[++right]>=line[j]);
                lineMaximal=(right-left)*line[j]
                if(lineMaximal>maximalRectangle)maximalRectangle=lineMaximal
            }
         }
    }
    return maximalRectangle 
};