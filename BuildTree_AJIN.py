def buildTree_pre_in(self, preorder, inorder):
    """
    :type preorder: List[int]
    :type inorder: List[int]
    :rtype: TreeNode
    """
    """finish point"""
    if not inorder:
        return
    """
    pre-in: left first and right second, value - lefttree - righttree
    use the inorder to judge the structure and use the preorder to find the next root
    if use pastorder and inorder, change the left and right
    """
    value = preorder.pop(0)
    left_tree = self.buildTree_pre_in(preorder, inorder[:inorder.index(value)])
    right_tree = self.buildTree_pre_in(preorder, inorder[inorder.index(value) + 1:])
    return TreeNode(value, left_tree, right_tree)