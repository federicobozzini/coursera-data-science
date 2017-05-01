SELECT count(*) FROM (
  SELECT distinct docid
  from frequency
  where docid in(
        SELECT distinct docid
        from frequency
        where term in('transactions'))
  and docid in(
        SELECT distinct docid
        from frequency
        where term in('world'))
) x;
