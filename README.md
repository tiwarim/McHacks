# McHacks

McHacks repo

## ml.anomaly_detection()

Arguments:

* corpus (list[str]): training corpus of previous tweets, as a list of strings (text body)
* new_data (list[str]): new tweet text (list of one string)
* vis (boolean): boolean to visualize 2D PCA projected scatterplot, defaults to False
* c_num (list[int]): list of cluster numbers to try, defaults to just [2], best is to use [2, 3, 4]
* features (int): maximum number of features to include, defaults to 100
* log (boolean): boolean to print out a bunch of data, defaults to False
  
Usage:

```python
ml.anomaly_detection(corpus, new_data, False, [2, 3, 4], 1000, False)
```
