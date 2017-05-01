select sum(a.count*b.count)
from frequency a join frequency b on a.term = b.term
where a.docid < b.docid
and a.docid in ('10080_txt_crude', '17035_txt_earn')
and b.docid in ('10080_txt_crude', '17035_txt_earn')
group by a.docid
having sum(a.count*b.count) != 0;
