import numpy as np
if __name__ == "__main__":
    alist = [1, 2, 3, -8, 2, 3, 4, -1, 2, 3, -9, 2]
    sum_num = 0
    max_num = float('-inf')
    left = 0
    right = 0

    for index, value in enumerate(alist):
        sum_num += value
        if sum_num < 0:
            sum_num = 0
            left = index + 1
        if max_num < sum_num:
            max_sum = sum_num
            right = index+1
    print(alist[left:right])


"""
CREATE DATABASE student;
DROP DATABASE test;
USE test;
SHOW TABLES;
CREATE TABLE students (id BIINT NOT NULL AUTO_INCREMENT, class_id BIGINT NOT NULL, PRIMARY KEY (id));
INSERT INTO student (class_id, average) SELECT class_id AVG(score) FROM students GROUP BY class_id;
ALTER TABLE x ADD COLUMN birth VARCHAR(10) NOT NULL;
REPLACE INTO x (id,class_id) VALUES (1,1);
SELECT id,gender FROM x ORDER BY score;
ORDER BY score DESC/ASC
LIMIT M OFFSET N
UPDATE x SET name= score= WHERE id>=5 AND id<=7;

BEGIN;
UPDATE x SET balance = balance-100 WHERE id=1;

COMMIT;
ROLLBACK;

"""

