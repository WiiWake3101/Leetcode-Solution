/**
 * @param {string} name
 * @param {string} typed
 * @return {boolean}
 */
var isLongPressedName = function(name, typed) {
    let i = 0;
    let j = 0;
    const nlen = name.length;
    const tlen = typed.length;

    while (i < nlen && j < tlen) {
        if (name[i] === typed[j]) {
            i++;
            j++;
        } else if (j > 0 && typed[j] === typed[j - 1]) {
            j++;
        } else {
            return false;
        }
    }

   
    while (j < tlen && typed[j] === name[nlen - 1]) {
        j++;
    }

    return i === nlen && j === tlen;
};
