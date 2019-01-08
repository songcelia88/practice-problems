"""Is this binary search tree a valid BST?

A valid binary search tree follows a specific rule. In our case,
the rule is "left child must value must be less-than parent-value"
and "right child must be greater-than-parent value".

This rule is recursive, so *everything* left of a parent
must less than that parent (even grandchildren or deeper)
and everything right of a parent must be greater than.

For example, this tree is valid::

        4
     2     6
    1 3   5 7

Let's create this tree and test that::

    >>> t = Node(4,
    ...       Node(2, Node(1), Node(3)),
    ...       Node(6, Node(5), Node(7))
    ... )

    >>> t.is_valid()
    True

This tree isn't valid, as the left-hand 3 is wrong (it's less
than 2)::

        4
     2     6
    3 3   5 7

Let's make sure that gets caught::

    >>> x = Node(4,
    ...       Node(2, Node(3), Node(3)),
    ...       Node(6, Node(5), Node(7))
    ... )

    >>> x.is_valid()
    False

This tree is invalid, as the bottom-right 1 is wrong --- it is
less than its parent, 6, but it's also less than its grandparent,
4, and therefore should be left of 4::

        4
     2     6
    1 3   1 7

    >>> y = Node(4,
    ...       Node(2, Node(1), Node(3)),
    ...       Node(6, Node(1), Node(7))
    ... )

    >>> y.is_valid()
    False
"""


class Node:
    """Binary search tree node."""

    def __init__(self, data, left=None, right=None):
        """Create node, with data and optional left/right."""

        self.left = left
        self.right = right
        self.data = data

    def is_valid(self, rootdata=None, isleft=None, isright=None):
        """Is this tree a valid BST?"""
        
        # check against root node 
        if rootdata and isleft:
            if self.data > rootdata:
                return False
        if rootdata and isright:
            if self.data < rootdata:
                return False

        l_valid = True
        r_valid = True
        if rootdata is None:
            rootdata = self.data

        if self.left is None:
            l_valid = True
        elif self.left.data > self.data:
            return False
        else:
            if isleft is None:
                isleft = True

            l_valid = self.left.is_valid(rootdata, isleft = isleft)

        if self.right is None:
            r_valid = True
        elif self.right.data < self.data:
            return False
        else:
            if isright is None:
                isright = True
            r_valid = self.right.is_valid(rootdata, isright=isright)

        print("node {}, l_valid {}, r_valid {}, rootdata {}, isleft {}, isright {}".format(self.data, l_valid, r_valid, rootdata, isleft, isright))
        return l_valid and r_valid


if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; THAT'S VALID!\n")

