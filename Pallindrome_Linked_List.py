# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        temp=head
        c=""
        while(temp!=None):
            c+=str(temp.val)
            temp=temp.next
        h=c[-1::-1]
        if(c==h):
            return True
        else:
            return False
        