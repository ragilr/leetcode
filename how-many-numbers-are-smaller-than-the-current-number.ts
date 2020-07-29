function smallerNumbersThanCurrent(nums: number[]): number[] {
    const count:number[] = new Array(100).fill(0);
    const ret:number[] = new Array(nums.length);
    for (const n of nums) {
        count[n]++;
    }
    for (let i = 1; i < count.length; i++) {
        count[i] += count[i-1];
    }
    // console.log(count);
    for (const [i,n] of nums.entries()) {
        ret[i] = (Number(n) !== 0)? count[n-1]  : 0; 
        // ret[i] = count[n]-1;
    }
    return ret;
};
