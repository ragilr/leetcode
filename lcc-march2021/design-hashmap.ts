class MyHashMap {
    private _map:number[];
    constructor() {
        this._map = new Array<1000001>();
        console.log("init");
    }

    put(key: number, value: number): void {
        this._map[key]=value;
        // console.log("put",key,value,this._map);
    }

    get(key: number): number {
        let ret:number = this._map[key]!=null ? this._map[key] : -1;
        // console.log("get",key,this._map);
        return ret;
    }

    remove(key: number): void {
        this._map[key]=undefined;
        // console.log("remove",key,this._map);
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * var obj = new MyHashMap()
 * obj.put(key,value)
 * var param_2 = obj.get(key)
 * obj.remove(key)
 */
