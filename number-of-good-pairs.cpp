class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        int index[101];
        int goodPairs=0;
        for (auto& it : index) {
            it=0;
        }
        for (auto& it : nums) {
            index[it]++;
        }
        for (auto& it : index) {
            if(it>0)
                goodPairs += ((it*(it-1))/2);
        }
        return goodPairs;
    }
};
