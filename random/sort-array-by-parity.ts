function sortArrayByParity(A: number[]): number[] {
    let b = new Array<number>(A.length);
    let i=0;
    let j=A.length-1;
    for(let a of A){
        if(a%2===0){
            b[i++]=a;
        }else{
            b[j--]=a;
        }
    }
    return b;
};
