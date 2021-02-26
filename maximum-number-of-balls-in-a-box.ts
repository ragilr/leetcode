function countBalls(lowLimit: number, highLimit: number): number {
    const box:number[] = new Array<number>(45);
    let i:number=lowLimit;
    let n:number;
    let s:number;
    while(i<=highLimit){
        n = i;
        s = 0;
        while(n!=0){
            s += n%10;
            n = Math.floor(n/10);
        }
        box[s-1]=box[s-1] ? box[s-1]+1 : 1;
        ++i;
    }
    return Math.max(...(box.filter(n => n)));
};
