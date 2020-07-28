/**
 * @param {number[]} candies
 * @param {number} extraCandies
 * @return {boolean[]}
 */
const kidsWithCandies = function(candies, extraCandies) {
    let g = 0; 
    for(i of candies){  // find greatest
        if(i>g){
            g=i;
        }
    }
    const ret = [];
    for(i of candies){
        ret.push(i+extraCandies>=g)
    }
    // console.log(ret);
    return ret;
};
