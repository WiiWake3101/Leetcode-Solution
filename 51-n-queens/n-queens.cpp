class Solution {
private:
    int n;
    vector<vector<string>> ans;
    int fd = 0, bd = 0, col = 0;
    void f(int i,vector<string> &v){
        if(i==n){
            ans.push_back(v);
            return;
        }
        for(int j=0;j<n;++j){
            if(fd&(1<<(i+j)) || bd&(1<<(i+n-1-j)) || col&(1<<j)) continue;
            fd |= 1<<(i+j), bd |= 1<<(i+n-1-j), col |= 1<<j;
            v[i][j] = 'Q';
            f(i+1,v);
            v[i][j] = '.';
            fd &= ~(1<<(i+j)), bd &= ~(1<<(i+n-1-j)), col &= ~(1<<j);
        }
    }
public:
    vector<vector<string>> solveNQueens(int n) {
        if(n==1) return {{"Q"}};
        if(n<=3) return {};
        this->n = n;
        string s(n,'.');
        vector<string> v;
        for(int i=0;i<n;++i) v.push_back(s);
        f(0,v);
        return ans;
    }
};