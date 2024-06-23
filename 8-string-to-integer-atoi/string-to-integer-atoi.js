/**
 * @param {string} s
 * @return {number}
 */
var myAtoi = function(s) {
    const a=Number.parseInt(s);
    if(a){
       if (a<= -2147483648)return -2147483648;
       else if (a>= 2147483647)return 2147483647;
       else return a;
    }
    return 0;
};