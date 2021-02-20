function countGoodTriplets(arr: number[], a: number, b: number, c: number): number {
    const l = arr.length
    let count = 0;
    for(let i=0; i<l; ++i){
        for(let j=i+1; j<l; ++j){
            if(Math.abs(arr[i]-arr[j])>a){
            continue;
            }
            for(let k=j+1; k<l; ++k){
                if(Math.abs(arr[j]-arr[k])>b){
                continue;
            }
                if(Math.abs(arr[i]-arr[k])<=c){
                    ++count;
                }
            }
        }
    }
     return count;
};
