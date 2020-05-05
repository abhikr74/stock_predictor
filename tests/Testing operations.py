x = {'q':1, 'w':2, 'e':33, 'r':4, 't':55, 'y':6}
# print (sorted(x, key = x.values()))
print ({k: v for k, v in sorted(x.items(), key=lambda item: item[1], reverse=True)})