function maxDepth(s: string): number {
    let d = 0,max=0;
    for(let c of s){
        switch(c){
            case '(':
                d++;
                break;
            case ')':
                d--;
                break;
        }
        max = d > max ? d : max;
    }
    return max;
};
