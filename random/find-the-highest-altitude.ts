function largestAltitude(gain: number[]): number {
    let h = 0;
    let c = 0;
    for (let i of gain){
        // console.log(i)
        c = Number(i)+c;
        // console.log(c)
        if(c>h)
            h=c;
    }
    return h;
};
