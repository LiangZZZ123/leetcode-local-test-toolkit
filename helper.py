from typing import (
    Any,
    Callable,
    Collection,
    Deque,
    Iterable,
    List,
    Optional,
    Sequence,
    Union,
)


class Test:
    def __init__(self, func: Callable):
        """A Test class that integrates test process of a function.

        Args:
            func (Callable): the function to be tested

        Instance methods for testing:
        - self.add_test_case
        - self.print_test_cases
        - self.test
        
        Static methods for testing:
        - Test.time_the_func
        """
        self.func = func
        self.case_index = 0
        self.wrong_case_count = 0
        self.case_list: List[Any] = []
        # self.correct_case_count = 0

    def add_test_case(self, *case_input, case_output=None):
        """
        Unpack all input args except the last one to a tuple, naming it case_input;
        then store all the info as (case_input, case_output) into a list.

        If no "case_output" is provided, case_output will be the last parameter from "*case_input".
        """
        if case_output is None:
            case_output = case_input[-1]
            case_input = case_input[:-1]
        else:
            # If case_output is not None, then just use the original case_output
            pass
        self.case_list.append((case_input, case_output))
        self.case_index += 1

    def print_test_cases(self):
        print("------PRINT ALL TEST CASES BELOW------")
        for case in self.case_list:
            print(f"{' '.join(str(item) for item in case[0])} -> {case[1]}")

    def test(
        self,
        res_format_func: Callable[[Any], Any] = None,
        test_customize_func: Callable[[Any, Any], bool] = None,
    ):
        """
        Run test for all cases stored in self.case_list, generate failed test cases and test report
        
        Transform the res to the formatted res if needed.
        
        Customize the test function if needed.
        """
        import sys
        import os

        file_name = os.path.basename(sys.argv[0])
        print(f"------TEST RESULT FOR {file_name} SHOWS BELOW------")

        case_index = 0
        for case in self.case_list:
            case_index += 1
            res_real = self.func(*case[0])

            # Format the res_real to make it suitable for test
            if res_format_func is not None:
                res_real = res_format_func(res_real)

            res_expected = case[1]
            test_res: bool
            # Customize the way to test if res_real == res_expected
            if test_customize_func is None:
                test_res = res_real == res_expected
            else:
                test_res = test_customize_func(res_real, res_expected)

            if test_res is True:
                print(f"Case {case_index} passed.")
            else:
                # Note: it the function-to-be-test change the input in-place, then the "Input" here
                # might be different from the original input.
                self.wrong_case_count += 1
                if_correct = Color.RED + "WRONG" + Color.END

                error_info = f"""Case {case_index}
        Input:           {' '.join(str(item) for item in case[0])}
        Res_real:        {res_real}
        Should be:       {res_expected}     {if_correct}"""

                print(error_info)

        if self.wrong_case_count == 0:
            summary = (
                Color.GREEN + f"TOTALLY {self.case_index} CASES, ALL PASSED" + Color.END
            )
        else:
            summary = Color.RED + f"{self.wrong_case_count} CASES FAILED" + Color.END

        print(
            f"""SUMMARY: {summary}
---------------------------------------------------------"""
        )

    @staticmethod
    def time_the_func(func: Callable, *args, repeat_times: int = 1000):
        import time

        start = time.perf_counter()
        for i in range(repeat_times):
            func(*args)
        end = time.perf_counter()
        print(
            f"{func.__name__} ran {repeat_times} times; average time: {((end-start)*1000, 2)} msec"
        )


class Color:
    PURPLE = "\033[1;35;48m"
    CYAN = "\033[1;36;48m"
    BOLD = "\033[1;37;48m"
    BLUE = "\033[1;34;48m"
    GREEN = "\033[1;32;48m"
    YELLOW = "\033[1;33;48m"
    RED = "\033[1;31;48m"
    BLACK = "\033[1;30;48m"
    UNDERLINE = "\033[4;37;48m"
    END = "\033[1;37;0m"


class TreeNode:
    def __init__(
        self,
        val: Optional[Any] = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    @staticmethod
    def build_tree(array: Sequence) -> Optional["TreeNode"]:
        """
        Build a tree from level_order_traversed_sequence.
        """
        from collections import deque

        # if building a tree with array = [], then just return None
        if len(array) == 0:
            return None

        queue: Deque = deque()
        i = 0
        # print(array, i)
        if array[i] is None:
            t = None
        else:
            t = TreeNode(array[i])

        root = t
        queue.append(root)
        i += 1

        while len(queue) > 0 and i < len(array):
            t1 = queue.popleft()
            if t1 is not None:
                t1.left = None if array[i] is None else TreeNode(array[i])
                queue.append(t1.left)
                i += 1

                # discard all trailing None from array
                if i >= len(array):
                    break

                t1.right = None if array[i] is None else TreeNode(array[i])
                queue.append(t1.right)
                i += 1

        # self.print_level_order(root)
        return root

    @staticmethod
    def return_level_order(root: TreeNode) -> List[Any]:
        """Return the list representation of a binary tree.

        Args:
            root (TreeNode): the root node of the binary tree

        Returns:
            List[Any]: the list which contains the node.val of all nodes from the binary tree by layer-order traverse
        """
        from collections import deque

        queue: Deque[Optional[TreeNode]] = deque()
        queue.append(root)
        res_list: List[Any] = []

        while len(queue) > 0:
            t = queue.popleft()

            if t is None:
                res_list.append(None)
            else:
                res_list.append(t.val)
                queue.append(t.left)
                queue.append(t.right)

        # Remove all trailing None in res_list
        i = len(res_list) - 1
        while i > -1:
            if res_list[i] is None:
                res_list.pop(i)
                i -= 1
            else:
                break

        return res_list

    @staticmethod
    def print_level_order(root):
        res_list = Tree.return_level_order(root)
        print(", ".join(str(val) for val in res_list))


# ======================================================================
# ======================================================================
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"ListNode<val={self.val}, next={self.next}>"


class LinkedList:
    @staticmethod
    def head_to_list(head: "ListNode") -> List:
        array = []
        while head is not None:
            array.append(head.val)
            head = head.next

        return array

    @staticmethod
    def list_to_head(array: List) -> Union[ListNode, None]:
        if len(array) == 0:
            return None

        head = pre_node = ListNode(array[0])
        for i in range(1, len(array)):
            cur_node = ListNode(array[i])
            pre_node.next = cur_node

            pre_node = cur_node
        return head

    # def __repr__(self) -> str:
    #     return f"Linkedlist<{self.array}>"


if __name__ == "__main__":
    ...
    # root = Tree.build_tree([1, None, 2, 3])
    # Tree.print_level_order(root)
    # root = Tree.build_tree([5, 4, 7, 3, None, 2, None, -1, None, 9])
    # Tree.print_level_order(root)

