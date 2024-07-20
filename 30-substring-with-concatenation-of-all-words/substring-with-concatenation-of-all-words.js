/**
 * @param {string} s
 * @param {string[]} words
 * @return {number[]}
 */
var findSubstring = function(s, words) {
      const wordLength = words[0].length;
  const wordsCount = words.length;
  const totalLength = wordLength * wordsCount;
  const result = [];

  if (s.length < totalLength) {
    return result;
  }

  const wordMap = new Map();
  for (const word of words) {
    wordMap.set(word, (wordMap.get(word) || 0) + 1);
  }

  for (let i = 0; i < wordLength; i++) {
    let left = i;
    let right = i;
    let count = 0;
    const currentMap = new Map();

    while (right + wordLength <= s.length) {
      const word = s.substring(right, right + wordLength);
      right += wordLength;

      if (wordMap.has(word)) {
        currentMap.set(word, (currentMap.get(word) || 0) + 1);
        count++;

        while (currentMap.get(word) > wordMap.get(word)) {
          const leftWord = s.substring(left, left + wordLength);
          currentMap.set(leftWord, currentMap.get(leftWord) - 1);
          left += wordLength;
          count--;
        }

        if (count === wordsCount) {
          result.push(left);
        }
      } else {
        currentMap.clear();
        count = 0;
        left = right;
      }
    }
  }

  return result;
};