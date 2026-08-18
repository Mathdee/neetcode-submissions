class Solution {
public:
    bool isAnagram(string s, string t) {
        std::unordered_map<char, int> ss;
        std::unordered_map<char, int> tt;

        for(char c: s){
            if(ss.find(c) != ss.end()){
                ss[c]++;
            }else{
                ss[c] = 1;
            }
        }

        for(char c: t){
            if(tt.find(c) != tt.end()){
                tt[c]++;
            } else{
                tt[c] = 1;
            }
        }

        return tt == ss;
    }
};
