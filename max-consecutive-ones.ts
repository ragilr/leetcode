function findMaxConsecutiveOnes(nums: number[]): number {
    let c = 0,max=0;
    for(let b of nums){
        if(b===1){
            c++;
        }else{
            c=0;
        }
        max = c > max ? c : max;
    }
    return max;
};
