class Solution {
public:
    void sortColors(vector<int>& nums) {
        vector<int> counts = {0, 0, 0};
        for (int n : nums) {
            counts[n] += 1;
        }
        int c = 0;
        for (int i = 0; i < counts.size(); i++) {
            for (int j = 0; j < counts[i]; j++) {
                nums[c] = i;
                c++;
            }
        }
    }
};