from time import process_time

boxes = [1, 2, 3, 4, 5]

def logFirstTwoBoxes(boxes):
    print(boxes[0]) # o(1)
    print(boxes[1]) # o(1)
# o(2) => o(1) + o(1) => o(1) - constant time complexity | space complexity o(1)
