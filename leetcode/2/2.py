#! /usr/bin/env python
# Copyright (c) 2014 LightKeeper Advisors LLC
# ANY REDISTRIBUTION OR COPYING OF THIS MATERIAL WITHOUT THE EXPRESS CONSENT
# OF LIGHTKEEPER ADVISORS IS PROHIBITED.
# All rights reserved.
#

#Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import math
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        cur1 = l1
        cur2 = l2

        breakpoint()
        num1 = parseNum(cur1)
        num2 = parseNum(cur2)
        ans = num1 + num2

        l3 = createList(reverseNum(ans))

        return l3

def createList(num):
    num = str(num)
    l1 = ListNode(val=int(num[-1]))
    for i in range(len(num)-2, -1, -1):
        l1 = ListNode(val=int(num[i]), next=l1)
    return l1

def reverseNum(num):
    return ''.join(reversed(str(num)))

def parseNum(cur):
    parsed, i = 0, 0
    while cur:
        parsed = parsed + cur.val * 10 ** i
        print(f'cur: {cur}, parsed: {parsed}, i: {i}')
        cur = cur.next
        i += 1
    return int(parsed)



if __name__ == "__main__":
    s = Solution()
    # a1 = s.addTwoNumbers(createList(reverseNum(342)), createList(reverseNum(465)))
    #a2 = s.addTwoNumbers(createList(reverseNum(0), createList(reverseNum(0)))
    #a3 = s.addTwoNumbers(createList(reverseNum(9999999), createList(reverseNum(9999)))
    #a4 =  s.addTwoNumbers(createList(reverseNum(942)), createList(reverseNum(9465)))
    #a5 =  s.addTwoNumbers(createList(reverseNum(65)), createList(reverseNum(945)))
    # a6 =  s.addTwoNumbers(createList(reverseNum(753865680)), createList(reverseNum(798580876)))
    a7 =  s.addTwoNumbers(createList(reverseNum(1000000000000000000000000000001)), createList(reverseNum(465)))
    breakpoint()