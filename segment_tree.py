input = [6, 2, 5, 4, 9, 3, 4, 1, 8]

n = 2
length = 1
while n < len(input):
    n = n ** 2

print(n)
seg_tree = [0 for x in range(2 * n - 1)]

low = 0
high = len(input) - 1
pos = 0


def construct_tree(input, seg_tree, low, high, pos):
    if low == high:
        seg_tree[pos] = input[low]
        return
    mid = int((low + high) / 2)

    construct_tree(input, seg_tree, low, mid, pos * 2 + 1)  # 왼쪽 자식 노드 번호
    construct_tree(input, seg_tree, mid + 1, high, pos * 2 + 2)  # 오른쪽 자식 노드 번호
    seg_tree[pos] = seg_tree[pos * 2 + 1] + seg_tree[pos * 2 + 2]


construct_tree(input, seg_tree, low, high, pos)

print(seg_tree)

# 0~7 찾을합: 1~3(2+5+4)
def range_sum(seg_tree, qlow, qhigh, low, high, pos):
    if qlow <= low and qhigh >= high:
        # 현재범위가 쿼리범위에 완전히 포함됨(total overlap)
        return seg_tree[pos]

    if qlow > high or qhigh < low:
        # 현재범위가 쿼리범위에 아예 포함 안됨(no overlap)
        return 0
    mid = int((low + high) / 2)
    return range_sum(seg_tree, qlow, qhigh, low, mid, pos * 2 + 1) + range_sum(
        seg_tree, qlow, qhigh, mid + 1, high, pos * 2 + 2
    )


print(range_sum(seg_tree, 1, 3, low, high, 0))
