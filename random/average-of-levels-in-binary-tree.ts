/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */
let sumNode:number[];
let countNode:number[];
function averageOfLevels(root: TreeNode | null): number[] {
    sumNode = [];
    countNode = [];
    traverse(root,0);
    for(let i=0;i<sumNode.length;++i){
        sumNode[i] = sumNode[i]/countNode[i];
    }
    return sumNode;
};


function traverse(root: TreeNode | null,level:number): void {
    if(root===null){
        return;
    }
    // console.log(sumNode,countNode,root.val,level);
    if(!countNode[level]){
        sumNode.push(root.val);
        countNode.push(1);
    }else{
        sumNode[level]+=root.val;
        countNode[level]++;
    }
    if(root.left!==null){
        traverse(root.left,level+1);
    }
    if(root.right!==null){
        traverse(root.right,level+1);
    }
};
