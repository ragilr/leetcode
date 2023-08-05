/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function getIntersectionNode(headA: ListNode | null, headB: ListNode | null): ListNode | null {
    let ptr1:ListNode = headA;
    let ptr2:ListNode = headB;
    if(ptr1===null || ptr2===null){
        return null;
    }
    while (ptr1 !== ptr2) { 
  
        ptr1 = ptr1.next; 
        ptr2 = ptr2.next; 
  
        if (ptr1 === ptr2) { 
            return ptr1; 
        } 
      
        if (ptr1 === null) { 
            ptr1 = headB; 
        } 

        if (ptr2 === null) { 
            ptr2 = headA; 
        } 
    }
    return ptr1;
};
