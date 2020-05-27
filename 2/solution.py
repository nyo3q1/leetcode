# https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        li1 = getList(l1, [])
        #print(l1)
        li1.reverse()
        li1 = int("".join(map(str, li1)))
        #print(li1)
        
        li2 = getList(l2, [])
        li2.reverse()
        #print(li2)
        li2 = int("".join(map(str, li2)))
        print(li1,li2)
        ans = li1+li2
        print(ans)
        ansL = [x for x in str(ans)]
        ansL.reverse()
        ansLn =  setList(ansL)
        print(ansLn)
        setList(None)#reset
        return ansLn
        
def setList(l: list):
    if l is None:
        return
    ln = ListNode(l.pop(0))
    if len(l) > 0:
        ln.next = setList(l)
    return ln

def getList(ln, l=[]):
    # listは参照渡しだからバグを抱えている
    l.append(ln.val)
    if ln.next:
        l = getList(ln.next, l)
    return l
