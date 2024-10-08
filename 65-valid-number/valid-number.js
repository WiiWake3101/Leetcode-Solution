/**
 * @param {string} s
 * @return {boolean}
 */
var isNumber = function(s) {
    let exp = false, sign = false, num = false, dec = false;
    for (let c of s) {  // Changed 'S' to 's'
        if (c >= '0' && c <= '9') num = true;     
        else if (c === 'e' || c === 'E') {
            if (exp || !num) return false;
            else exp = true, sign = false, num = false, dec = false;
        }
        else if (c === '+' || c === '-') {
            if (sign || num || dec) return false;
            else sign = true;
        }
        else if (c === '.') {
            if (dec || exp) return false;
            else dec = true;
        }
        else return false;
    }
    return num;
};