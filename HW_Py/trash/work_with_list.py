# elements = [0, 1, 2, -3, 0, 4, 5, 0, 1]
#
# print(sum(element for i, element in enumerate(elements) if not i & 1))
#
# l_index = elements.index(0) + 1
# r_index = len(elements) - 1 - elements[::-1].index(0)
# sub_elements = elements[l_index: r_index]
#
# print(sorted(sub_elements, key=lambda x: x < 0))


