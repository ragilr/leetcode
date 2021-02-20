function maxProduct(nums: number[]): number {
    let h1 = Math.max(nums[0]-1,nums[1]-1);
    let h2 = Math.min(nums[0]-1,nums[1]-1);
    let num;
    for(let i=2;i<nums.length;++i){
        num = nums[i]-1;
        if(num===h1){
            h2 = h1;
        }else if(num>h1){
            h2 = h1;
            h1 = num;
        }else if(num>h2){
            h2 = num;
        }
    }
    return h1*h2;
};
