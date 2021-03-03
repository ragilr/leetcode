function findErrorNums(nums: number[]): number[] {
    const l = nums.length;
    let missing=-1;
    let rep;
    let map = new Map();
    for(let i=0;i<l;++i){
        if(map.has(nums[i])){
            rep = nums[i];
        }
        map.set(nums[i],1);
    }
    // console.log(map)
    for(let i=0;i<l;++i){
        if(!map.has(i+1)){
            missing = i+1;
            break;
        }
    }
    return [rep,missing];
};
