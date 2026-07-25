class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> seen;
        int n = nums.size();
        for(int i = 0; i < n; ++i){
            seen[nums[i]] = i;
        }

        for(int i = 0; i < n; ++i){
            int difference = target - nums[i];
            if(seen.find(difference) != seen.end() &&  seen[difference] != i){
                return {i, seen[difference]};
            }

        }
        return {};
    }
};
