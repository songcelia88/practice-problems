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

    def is_valid(self, min_val=None, max_val=None):
        """Is this tree a valid BST?"""
        
        # check self against min or max
        if min_val and self.data < min_val:
            return False
        if max_val and self.data > max_val:
            return False

        # check the left side
        if self.left is None:
            l_valid = True
        else:
            l_valid = self.left.is_valid(min_val=min_val, max_val=self.data)

        # check the right side
        if self.right is None:
            r_valid = True
        else:
            r_valid = self.right.is_valid(min_val=self.data, max_val=max_val)

        
        return l_valid and r_valid

    def all_nodes(self):
        """return all the nodes in order"""
        if self.left is None and self.right is None:
            return [self.data]

        return self.left.all_nodes() + [self.data] + self.right.all_nodes()

    def is_valid_alt(self):
        allnodes = self.all_nodes()
        current = allnodes[0]
        for val in allnodes[1:]:
            if val < current:
                return False
            current = val

        return True

if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; THAT'S VALID!\n")

    # False Tree
    y = Node(4,
           Node(2, Node(1), Node(3)),
           Node(6, Node(1), Node(7))
    )

    # False Tree
    x = Node(4,
           Node(2, Node(3), Node(3)),
           Node(6, Node(5), Node(7))
    )

    # True Tree
    t = Node(4,
           Node(2, Node(1), Node(3)),
           Node(6, Node(5), Node(7))
    )
