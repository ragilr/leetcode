class OrderedStream {
    private stream:string[];
    private lastO: number;
    constructor(n: number) {
        this.stream = new Array(n);
        this.lastO = -1;
    }

    insert(id: number, value: string): string[] {
        this.stream[id-1] = value;
        // console.log("stream "+this.stream);
        let i= this.lastO+1;
        while(i < this.stream.length){
            if (!this.stream[i]){
                break;
            }
            ++i;
        }
        // console.log("i:"+i+" lastO:"+this.lastO);
        if(i!==this.lastO+1){
            let output = this.stream.slice(this.lastO+1,i);
            this.lastO = i-1;
            // console.log("updated lastO:"+this.lastO);
            return output;
        }
        return [];
    }
}

/**
 * Your OrderedStream object will be instantiated and called as such:
 * var obj = new OrderedStream(n)
 * var param_1 = obj.insert(id,value)
 */
