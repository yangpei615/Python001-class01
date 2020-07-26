import pandas as pd
import numpy as np

pf = pd.DataFrame({'id': [1, 2, 3, 4, 5],
                           'name': ['张三', '李四', '王五', '贺六', '郭七'],
                           'age': [21, 22, 23, 24, 25]})
# 假设pf里面有很多很多行数据。
# 假设pf1和2就不列举数据了，从csv取
url1 = './test1.csv'
url2 = './test2.csv'
pf1 = pd.DataFrame(url1)
pf2 = pd.DataFrame(url2)

# 1. SELECT * FROM data;
pf
# 2. SELECT * FROM data LIMIT 10;
pf.head(10)

# 3. SELECT id FROM data;  //id 是 data 表的特定一列
pf['id']

# 4. SELECT COUNT(id) FROM data;

pf['id'].count()

# 5. SELECT * FROM data WHERE id<1000 AND age>30;

pf[pf['id'] < 1000 & pf['age'] > 30]

# 6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;

pf.groupby('id')['id'].agg({'order_id': pf.nunique()})


# 7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;

table1 = pd.DataFrame()
table2 = pd.DataFrame()
pf_new = pd.merge(table1, table2, on='id')

# 8. SELECT * FROM table1 UNION SELECT * FROM table2;

pd.concat(table1, table2)

# 9. DELETE FROM table1 WHERE id=10;

table1.drop(table1[table1.id= '10'].index)


# 10. ALTER TABLE table1 DROP COLUMN column_name;

del pf['column_name']


