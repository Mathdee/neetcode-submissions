class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::vector<std::vector<std::string>> result;
        std::unordered_map<std::string, std::vector<std::string>> curr;

        for(std::string& s: strs){
            std:string key = s;
            std::sort(key.begin(), key.end());
            curr[key].push_back(s);
        }

        for(auto& c: curr){
            result.push_back(c.second);
        }

        return result;
        
    }
};
