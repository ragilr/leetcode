function minimumLengthEncoding(words: string[]): number {
    words.sort((a,b)=>{return (b.length-a.length);});
    let len = words[0].length + 1
    let flag;
    // console.log(words);
    for(let i=1;i<words.length;++i){
        let flag;
        for(let j=i-1;j>-1&&!flag;--j){
            flag = words[j].endsWith(words[i]);
            // console.log(words[i],words[j],len,flag);
        }
        len = !flag ? len+words[i].length+1 : len;
    }
    return len;
};
