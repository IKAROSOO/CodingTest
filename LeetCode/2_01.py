class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_ary = []
        l2_ary = []

        while l1 is not None:
            l1_ary.insert(0, l1.val)
            l1 = l1.next

        while l2 is not None:
            l2_ary.insert(0, l2.val)
            l2 = l2.next
        
        l1_int = 0
        l2_int = 0

        for i in range(len(l1_ary)):
            l1_int += l1_ary[i]*(10**(len(l1_ary) - i - 1))
        
        for i in range(len(l2_ary)):
            l2_int += l2_ary[i]*(10**(len(l2_ary) - i - 1))

        answer = l1_int + l2_int
        answer_ary = []

        for i in range(len(str(answer))):
            answer_ary.insert(0, int(str(answer)[i]))

        return answer_ary