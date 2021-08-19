# leetcode-local-test-toolkit
When going through algorithm problems on LeetCode, I find it more convenient to do practice locally, and I find some data structures that have unique representation on its test cases. LeetCode transform the data behind the scene when it run tests, which is not convenient for us to do test locally.

So I make some simple scripts that makes running LeetCode problems locally more easily.

- Using `Test` class to easily see if you fail or pass some test cases.
- Using `Tree` class to transform between "the array representation of a tree" and "the root representation of a tree".
- Using `LinkedList` class to transform between "the head-node representation of a linked list" and "the array representation of a linked list".
- I will add more data structure representations on LeetCode if needed/

## Sample on Tree
```python
# [124] binary_tree_maximum_path_sum
#

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        """
        This is a tree-structure-dp problem.
        
        Ref:https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/solution/shu-xing-dpfu-tong-lei-wen-ti-by-liweiwe-wupz/
        """

        def dfs(node):
            nonlocal res
            if node is None:
                return 0

            left_subtree_sum = max(0, dfs(node.left))
            right_subtree_sum = max(0, dfs(node.right))

            res = max(res, node.val + left_subtree_sum + right_subtree_sum)

            return node.val + max(left_subtree_sum, right_subtree_sum)

        res = -float("inf")
        dfs(root)
        return res  # type:ignore


# @lc code=end

if __name__ == "__main__":
    from helper import Test, Tree

    func = Test(Solution().maxPathSum)
    func.add_test_case(Tree.build_tree([1, 2, 3]), 5)
    func.add_test_case(Tree.build_tree([-10, 9, 20, None, None, 15, 7]), 42)

    func.test()
```
will give you
```
➜  .leetcode python 124.binary_tree_maximum_path_sum.py
------TEST RESULT FOR 124.binary_tree_maximum_path_sum.py SHOWS BELOW------
Case 1 passed.
Case 2 passed.
SUMMARY: TOTALLY 2 CASES, ALL PASSED
---------------------------------------------------------
```
--------------
Now modify `func.add_test_case(Tree.build_tree([1, 2, 3]), 6)` above,
```python
# LC problem 124

if __name__ == "__main__":
    from helper import Test, Tree

    func = Test(Solution().maxPathSum)
    # 5 is the wrong answer!
    func.add_test_case(Tree.build_tree([1, 2, 3]), 5)
    func.add_test_case(Tree.build_tree([-10, 9, 20, None, None, 15, 7]), 42)

    func.test()
```
will give you(the result is colored if you run in terminal):
```
------TEST RESULT FOR 124.binary_tree_maximum_path_sum.py SHOWS BELOW------
➜  .leetcode python 124.binary_tree_maximum_path_sum.py
Case 1
        Input:           <helper.TreeNode object at 0x7fd733623898>
        Res_real:        6
        Should be:       5     WRONG
Case 2 passed.
SUMMARY: 1 CASES FAILED
```
----------------------------------------------------------------

## Sample on LinkedList
```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# @lc code=start
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        cur = head
        while cur is not None:
            temp = cur.next
            
            cur.next = prev
            prev = cur
            cur = temp
        
        return prev
# @lc code=end
if __name__ == "__main__":
    from helper import Test, LinkedList

    func = Test(Solution().reverseList)
    func.add_test_case(LinkedList.list_to_head([1,2,3,4,5]),[5,4,3,2,1])
    func.add_test_case(LinkedList.list_to_head([1,2]), [2,1])
    func.add_test_case(LinkedList.list_to_head([]), [])

    func.test(res_format_func=LinkedList.head_to_list)
```
will give you(the result is colored if you run in terminal):
```
➜  .leetcode python 206.reverse_linked_list.py
------TEST RESULT FOR 206.reverse_linked_list.py SHOWS BELOW------
Case 1 passed.
Case 2 passed.
Case 3 passed.
SUMMARY: TOTALLY 3 CASES, ALL PASSED
```