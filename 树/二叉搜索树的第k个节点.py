# 给定一棵二叉搜索树，请找出其中的第k小的结点。例如， （5，3，7，2，4，6，8）    中，按结点数值大小顺序第三小结点的值为4。
# 二叉搜索树，直接中序排列就可以得到排序后的列表
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        if not pRoot:
            return None
        if k < 1 or k > len(self.midTraverse(pRoot)):
            return None
        return self.midTraverse(pRoot)[k - 1]

    def midTraverse(self, pRoot):
        res = []
        if not pRoot:
            return res
        # if pRoot.left:这里的if可以不再判别了 显得更加简洁
        res += self.midTraverse(pRoot.left)
        res.append(pRoot.val)
        # if pRoot.right:
        res += self.midTraverse(pRoot.right)
        return res


if __name__ == '__main__':
    n1 = TreeNode(8)
    n2 = TreeNode(6)
    n3 = TreeNode(10)
    n4 = TreeNode(5)
    n5 = TreeNode(7)
    n6 = TreeNode(9)
    n7 = TreeNode(11)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    s = Solution()
    print(s.KthNode(n1, 1))
