# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            curr.next = ListNode(val)

            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
    
if __name__ == "__main__":

    def create_linked_list(list):
    
        dummy = ListNode()
        curr = dummy
        for num in list:
            curr.next = ListNode(num)
            curr = curr.next
        return dummy.next

    def print_linked_list(node):
        """Print linked list"""
        nums = []
        while node:
            nums.append(str(node.val))
            node = node.next
        print(" -> ".join(nums))

    def main():
        # Take input from user
        l1_input = input("Enter first number as space-separated digits (e.g. 2 4 3): ")
        l2_input = input("Enter second number as space-separated digits (e.g. 5 6 4): ")

        # Convert input string to list of integers
        l1_list = list(map(int, l1_input.strip().split()))
        l2_list = list(map(int, l2_input.strip().split()))

        # Create linked lists
        l1 = create_linked_list(l1_list)
        l2 = create_linked_list(l2_list)

        # Solve
        sol = Solution()
        result = sol.addTwoNumbers(l1, l2)

        # Print output
        print("\nResulting Linked List:")
        print_linked_list(result)

main()




