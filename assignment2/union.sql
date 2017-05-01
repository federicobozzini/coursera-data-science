SELECT count(*) FROM (
  SELECT term
  from frequency
  where docid in('10398_txt_earn')
  and count = 1
  union
  SELECT term
  from frequency
  where docid in('925_txt_trade')
  and count = 1
) x;
