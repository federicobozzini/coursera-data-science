select a.row_num, b.col_num, sum(a.value*b.value)
from A a, B b
where a.col_num = b.row_num
group by a.row_num, b.col_num
having sum(a.value*b.value) != 0;

/* That's it!  Join columns to rows, group by rows and columns, then filter to get the cell you want. */
