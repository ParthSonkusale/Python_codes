
class Solution(object):
    def addTwoNumbers(self, l1, l2):

        # Convert l1 linked list into a normal Python list
        list1 = []

        current = l1

        while current:
            list1.append(current.val)
            current = current.next


        # Convert l2 linked list into a normal Python list
        list2 = []

        current = l2

        while current:
            list2.append(current.val)
            current = current.next


        # Convert list1 into a number
        num1 = 0
        n = len(list1)

        for i in range(n):
            num1 = num1 * 10 + list1[(n - 1) - i]


        # Convert list2 into a number
        num2 = 0
        m = len(list2)

        for j in range(m):
            num2 = num2 * 10 + list2[(m - 1) - j]


        # Add the two numbers
        num = num1 + num2


        # Extract digits from the answer
        lo = []

        while num > 0:
            ele = num % 10
            lo.append(ele)
            num = num // 10

        if num == 0 and len(lo) == 0:
            lo.append(0)


        # Create the result linked list
        dummy = ListNode(0)
        current = dummy

        for value in lo:
            current.next = ListNode(value)
            current = current.next

        return dummy.next