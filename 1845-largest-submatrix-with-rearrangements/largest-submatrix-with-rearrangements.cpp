class Solution 
{
public:
    int largestSubmatrix(vector<vector<int>>& matrix) 
    {
        int m = matrix.size();
        int n = matrix[0].size();
        vector<int>hist(n,0);
        int ret = 0;
        for (int i=0; i<m; i++)
        {
            for (int j=0; j<n; j++)
            {
                if (matrix[i][j]==1)
                    hist[j] = hist[j]+1;
                else
                    hist[j] = 0;                    
            }
            auto h = hist;
            sort(h.begin(), h.end());
            reverse(h.begin(), h.end());
            for (int j=0; j<n; j++)
                ret = max(ret, h[j]*(j+1));
        }
        return ret;        
    }
};
