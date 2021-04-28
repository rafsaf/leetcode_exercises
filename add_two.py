from typing import Optional
from xml.dom.NodeFilter import NodeFilter


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def node_to_int(list_node: ListNode) -> int:
            current_node: ListNode = list_node
            result = 0
            i = 1
            while True:
                result += current_node.val * i
                if current_node.next is None:
                    break
                current_node = current_node.next
                i *= 10
            return result

        def int_to_node(number: int) -> ListNode:
            result_node: Optional[ListNode] = None
            node_str = reversed(str(number))
            current_node: Optional[ListNode] = None
            for val in node_str:
                new_node = ListNode(int(val))
                if not result_node:
                    result_node = new_node
                if current_node:
                    current_node.next = new_node
                current_node = new_node
            if result_node:
                return result_node
            raise ValueError()

        int1: int = node_to_int(l1)
        int2: int = node_to_int(l2)
        return int_to_node(int1 + int2)


l3 = ListNode(3)
l2 = ListNode(4, l3)
l1 = ListNode(2, l2)
g3 = ListNode(4)
g2 = ListNode(6, l3)
g1 = ListNode(5, l2)
sol = Solution().addTwoNumbers(l1, g1)
print(sol.next.val)
