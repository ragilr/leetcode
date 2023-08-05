function arrayPairSum(nums: number[]): number {
    nums.sort((a,b)=> { return(a-b); });
    let s = 0;
    for(let i=0;i<nums.length;i+=2){
        s += nums[i];
    }
    return s;
};
