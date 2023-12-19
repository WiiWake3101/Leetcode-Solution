class Solution(object):
    def imageSmoother(self, img):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(img)
        n = len(img[0])
        result = [[i for i in row] for row in img]
        for i in range(m):
            for j in range(n):
                total = img[i][j]
                count = 1
                if i > 0:
                    total += img[i-1][j]
                    count += 1
                if j > 0:
                    total += img[i][j - 1]
                    count += 1
                if i < m - 1:
                    total += img[i+1][j]
                    count += 1
                if j < n - 1:
                    total += img[i][j+1]
                    count += 1
                if i > 0 and j > 0:
                    total += img[i-1][j-1]
                    count += 1
                if i < m - 1 and j < n - 1:
                    total += img[i+1][j+1]
                    count += 1
                if i > 0 and j < n - 1:
                    total += img[i-1][j+1]
                    count += 1
                if i < m - 1 and j > 0:
                    total += img[i+1][j-1]
                    count += 1
                result[i][j] = total / count
        return result  