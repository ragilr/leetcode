function missingNumber(nums: number[]): number {
    const l:number = nums.length;
    let i=0;
    let res = 0;
    while(i<=l){
        res = res ^ i++;
    }
    for(let n of nums){
        res = res ^ n;
    }
    return res;
};
