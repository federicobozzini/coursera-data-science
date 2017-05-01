import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    matrix = record[0]
    val = record[3]
    i = record[1]
    j = record[2]
    if matrix==u"a":
        for k in range(5):
            mr.emit_intermediate((i, k), (matrix, i, j, val))
    else:   
        for k in range(5):
            mr.emit_intermediate((k, j), (matrix,i, j, val))
        
def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    prods = [val1*val2 for (m1, i, j1, val1) in list_of_values for (m2, j2, k, val2) in list_of_values if m1 =="a" and m2 == "b" and j1 == j2]
    res = reduce(lambda x, y: x+y, prods, 0)
    mr.emit((key+(res,)))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
