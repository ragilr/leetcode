const sumOddLengthSubarrays = (arr: number[]): number => {
            const n = arr.length;
            let ret = 0;
            for (let i = 0; i < n; ++i) {
                // console.log((((i + 1) * (n - i) + 1) / 2));
                ret = ret + Math.floor((((i + 1) * (n - i) + 1) / 2)) * arr[i];
            }
            return ret;
        };
