select sum(a.count*b.count)
from frequency2 a join frequency b on a.term = b.term
where a.docid = 'q'
group by b.docid
order by sum(a.count*b.count) desc
limit 1;
