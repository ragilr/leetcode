function sortedSquares(nums: number[]): number[] {
    const l:number = nums.length;
    const sq:number[] = new Array<number>(l);
    let i=0,j=l-1,k=l-1,f,b;
    while(k>-1 && j>-1 && i<l){
        f = nums[i]**2;
        b = nums[j]**2;
        sq[k--] = f>b ? nums[i]*nums[i++] : nums[j]*nums[j--];
    }
    while(j>-1){
        sq[k--] = nums[j]*nums[j--];
    }
    while(i<l){
        sq[k--] = nums[i]*nums[i++];
    }
    return sq;
};
