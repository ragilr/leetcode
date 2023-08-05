function balancedStringSplit(s: string): number {
    let b = 0;
    let count = 0;
    for(let c of s){
        b += (c==='R' ? 1 : -1 );
        if(b===0){
            count++;
        }
    }
    return count;
};
