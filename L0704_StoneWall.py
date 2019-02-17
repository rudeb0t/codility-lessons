# The problem statement for this exercise is terribly written and does not seem
# to describe the "Manhattan Skyline" problem properly. The lesson is about
# stacks and queues and so using a stack the algorithm goes like this:
#
# 1. Start with height at index 0, block count 1. Store this height in stack.
#
# 2. Next height.
#
# 3. Compare it with the height at the top of the stack if there are heights on
#    the stack. If the height at the top of the stack is higher than our
#    current height, we pop the height from the stack. Repeat this step, until
#    we meet a height that is either smaller or equal to our height, or we run
#    out of stack items.
#
# 4. If we still have items on the stack, check if the top item is equal to our
#    current height. If the heights are equal then this means we can extend the
#    end of the previous wall segment, we don't need a new block. Otherwise, we
#    don't have any more heights on stack or the current height is smaller than
#    the height at the top of our stack. We push the current wall height to the
#    stack. We need a new block with the current height, so we increase our
#    block count.
#
# 5. If there are more heights in our list, then go to step 2.
# 
def solution(H):
    walls = list()
    blocks = 0
    for h in H:
        while walls and walls[-1] > h:
            # Remove all wall blocks taller than our stacked blocks until we
            # run out of walls or we meet a wall shorter than or equal to h.
            walls.pop()

        if walls and walls[-1] == h:
            # Height is same as last wall block height. Move on to the next
            # block.
            continue
        else:
            # New height, push this to the stack of walls and increment blocks
            blocks += 1
            walls.append(h)

    return blocks


def test_example1():
    # Scanning the "wall" from left to right.
    #
    # The first segment, is 8 can be merged with second segment also 8. So 1
    # block.
    #
    # The third segment is 5, so 2 blocks now needed.
    #
    # Fourth segment is 7, so 3 blocks now needed.
    #
    # Fifth segment is 9 so 4 blocks now needed.
    #
    # Sixth segment is 8, is lower than fifth, fourth and third, so we need 5
    # blocks.
    #
    # Seventh segment is 7, is lower than sixth and fifth, but can be covered
    # by fourth segment 7 which we can extend. So no need for a new block.
    #
    # Eighth block is 4, which is lower than all the other blocks up to fourth
    # segment, so we must start a new block and need 6 blocks now.
    #
    # Ninth block is 8 which is higher than eighth block of 4 so we need 7 blocks.
    assert 7 == solution([8, 8, 5, 7, 9, 8, 7, 4, 8])
