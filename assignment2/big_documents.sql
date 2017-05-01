SELECT count(*) FROM (
  SELECT distinct docid
  from frequency
  group by docid
  having sum(count) > 300
) x;
