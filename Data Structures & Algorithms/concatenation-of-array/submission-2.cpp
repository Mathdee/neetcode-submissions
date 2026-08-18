class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        std::vector<int> result;
        for(int i = 0; i < 2; ++i){
            for(int num: nums){
                result.push_back(num);
            }
        }
        return result;
    }
};