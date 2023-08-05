function maximumWealth(accounts: number[][]): number {
    let l = -1;
    let b;
    let m = accounts.length;
    let n = accounts[0].length;
    for(let i=0;i<m;++i){
        b=0;
        for(let j=0;j<n;++j){
            b = b + accounts[i][j];
        }
        l = b>l ? b : l;
    }
    return l;
};
