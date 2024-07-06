/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function(digits) {
        const digitToLetters = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    };
    const generateCombinations = (index, partial, digits) => {
        if (index === digits.length) {
            result.push(partial);
            return;
        }

        const currentDigit = digits[index];
        const letters = digitToLetters[currentDigit];

        for (const letter of letters) {
            generateCombinations(index + 1, partial + letter, digits);
        }
    };

    const result = [];
    if (digits) {
        generateCombinations(0, '', digits);
    }

    return result;
};