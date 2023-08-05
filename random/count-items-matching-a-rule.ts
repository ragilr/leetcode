function countMatches(items: string[][], ruleKey: string, ruleValue: string): number {
    let index:number;
    switch(ruleKey){
        case "type":
            index = 0;
            break;
        case "color":
            index = 1;
            break;
        default:
            index = 2;            
    }
    let c = 0;
    for(const s of items){
        if(s[index]===ruleValue){
            ++c;
        }
    }
    return c;
};
