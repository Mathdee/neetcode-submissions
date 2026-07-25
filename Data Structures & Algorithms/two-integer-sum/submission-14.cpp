class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        std::unordered_map<int, int> seen;

        for(int i = 0; i < n; ++i){
            seen[nums[i]] = i;
        }

        for(int i = 0; i < n; ++i){
            int difference = target - nums[i];
            if(seen.count(difference) && seen[difference] != i){
                return {i, seen[difference]};
            }
        }
        return {};
    }
};
