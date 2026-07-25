class Solution {
public:
    bool isAnagram(string s, string t) {
        std::unordered_map<char, int> seen;
        std::unordered_map<char, int> teen;

        for(char c: s){
            if(seen.find(c) != seen.end()){
                seen[c]++;
            }else{
                seen[c] = 1;
            }
        }

        for(char c: t){
            if(teen.find(c) != teen.end()){
                teen[c]++;
            }else{
                teen[c] = 1;
            }
        }

        return seen == teen;
    }
};
