const findNumbers = (nums: number[]): number => {
    return nums.reduce(numOfDigits,0);
};

const numOfDigits = (tot: number,num: number): number => {
    tot = (`${num}`.length%2 === 0) ? tot+1 : tot;
    return tot;
}
