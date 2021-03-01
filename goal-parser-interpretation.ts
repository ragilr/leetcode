function interpret(command: string): string {
    const l:number = command.length;
    const s = [];
    let i = 0;
    while(i<l){
        if(command[i]==="G"){
            s.push("G");
        }else if(command[i++]==="("&&command[i]===")"){
            s.push("o");
        }else{
            s.push("al");
            i=i+2;
        }
        ++i;
    }
    return s.join("");
};
