SELECT count(*) FROM (
  SELECT distinct docid
  from frequency
  where term='parliament'
) x;
