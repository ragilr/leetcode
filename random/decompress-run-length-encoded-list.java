class Solution {
    public int[] decompressRLElist(int[] nums) {
        int tot=0;
        for(int i=0;i<nums.length;i+=2){
            tot+=nums[i];
        }
        int[] ret = new int[tot];        
        int j=0,k;
        for(int i=0;i<nums.length;i+=2){
            k=0;
            while(k++<nums[i]){
                ret[j++]=nums[i+1];
            }
        }
        return ret;
    }
}
