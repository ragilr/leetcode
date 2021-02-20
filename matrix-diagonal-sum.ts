function diagonalSum(mat: number[][]): number {
    const l = mat.length;
    let sum = 0;
    for(let i=0;i<l;++i){
        sum += mat[i][i];
    }
    for(let i=0;i<l;++i){
        sum += mat[l-i-1][i];
    }
    if(l%2 === 1){
        sum -= mat[Math.floor(l/2)][Math.floor(l/2)]
    }
    return sum;
};
