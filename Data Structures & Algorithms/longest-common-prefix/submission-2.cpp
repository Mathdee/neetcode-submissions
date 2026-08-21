class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if(strs.empty()){
            return "";
        }

        std::string first_word = strs[0];
        std::vector<std::string> prefixes;
        std::string current_string = "";
        std::string result = "";
        for(char c: first_word){
            current_string += c;
            prefixes.push_back(current_string);
        }

        for(std::string prefix: prefixes){
            bool found_all = true;
            for(int i = 1; i < strs.size(); ++i){
                
                if(strs[i].find(prefix) != 0){
                    found_all = false;
                    break;
                }
            }

            if(found_all){
                result = prefix;
            }
        }
        return result;

    
    }
};