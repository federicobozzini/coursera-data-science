select sum(a.value*b.value)
from A a, B b
where a.row_num = 2 and b.col_num = 3 and a.col_num = b.row_num;

/* That's it!  Join columns to rows, group by rows and columns, then filter to get the cell you want. */
