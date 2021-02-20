function minTimeToVisitAllPoints(points: number[][]): number {
    let x = points[0][0];
    let y = points[0][1];
    let total = 0;
    let len = points.length;
    let d;
    for(let i=1 ; i<len; ++i){
        d = Math.max(Math.abs(points[i][0]-x),Math.abs(points[i][1]-y));
        total= total + d;
        x = points[i][0];
        y = points[i][1];
    }
    return total;
};
