function countConsistentStrings(allowed: string, words: string[]): number {
    const alwd = new Map();
    for(let c of allowed){
        alwd.set(c,1);
    }
    let count = words.length;
    for(let w of words){
       for(let c of w){
            if(!alwd.has(c)){
                --count;
                break;
            }
       } 
    }
    return count;
};
