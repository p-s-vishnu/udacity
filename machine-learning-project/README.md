ud120-projects
==============

Starter project code for students taking Udacity ud120


Since my system was showing memory error for given test size = 0.1, so I used test size from a range of values from 0.1 to 0.5. But when I sliced the data I was able to run using given test_size=0.1*

In order to change test _size go to *'/machine-learning-project/tools/email_preprocess.py'*

Given test_size = 0.1, Current test_size = 0.2. Most of the time I will be using test_size *0.2*. In below screenshots, no. of Chris & Sara's training emails are prior to slicing.

### Supervised Classification Algorithms
### Algorithm 1 : Naive Bayes

![Output](https://github.com/qwertypsv/udacity/blob/master/machine-learning-project/images/NaiveBayes.PNG)

**Disadvantage** : It makes a very strong assumption on the shape of your data distribution, i.e. any two features are independent given the output class. E.g In a sentence, the algorithm doesn't consider the sequence of words, instead it focuses only on the number of words that appear in the sentence.

---

### Algorithm 2 : SVM (Support Vector Machine)
##### Speed - Accuracy tradeoff 
* SVM is MUCH slower to train and use for predicting

	![Output](https://github.com/qwertypsv/udacity/blob/master/machine-learning-project/images/SVM.PNG)

* Trained using a smaller training set (1% of test_size)

	![Output](https://github.com/qwertypsv/udacity/blob/master/machine-learning-project/images/SVM_small.PNG)

* Using the above sliced training set, I trained using *kernel as 'rbf'*

	![Output](https://github.com/qwertypsv/udacity/blob/master/machine-learning-project/images/SVM_small_rbf.PNG)

* In the above case, varied the C values to 10, 100, 1000, 10000 (with test_size = 0.1). *As the value of C increased Accuracy also increased* 

	![10](https://github.com/qwertypsv/udacity/blob/master/machine-learning-project/images/SVM_10.PNG)

	![100](https://github.com/qwertypsv/udacity/blob/master/machine-learning-project/images/SVM_100.PNG)

	![1000](https://github.com/qwertypsv/udacity/blob/master/machine-learning-project/images/SVM_1000.PNG)

	![10000](https://github.com/qwertypsv/udacity/blob/master/machine-learning-project/images/SVM_10000.PNG)

* Removing the slicing and re-training with the C = 10000 and test_size = 0.11 (since 0.1 shows memory errors)

	![Output](https://github.com/qwertypsv/udacity/blob/master/machine-learning-project/images/SVM_rbf.PNG)

* The author of 10th, 26th and 50th mail

	![Output](https://github.com/qwertypsv/udacity/blob/master/machine-learning-project/images/SVM_prediction.PNG)

* The total number of mails which belonged to Chris(1) were *877* (with test_size = 0.1, no slicing, accuracy of 99%) 

**Advantage** :
+ It performs well where there is a clear separation 

**Disadvantage**:
- Low performance in large data set
- If the data is having more noise, Naive Bayes has the upper hand

---

### Algorithm 3 : Decision Trees

* min_samples_split = 40

    ![Output](https://github.com/qwertypsv/udacity/blob/master/machine-learning-project/images/DT_min_40.PNG)
    
* Number of features = 3785
* In order to reduce the complexity of Tree, the number of features can be modified(feature selection).
Here sklearn.feature_selection.SelectPercentile's parameter(percentile) can be modified to reduce features.
* Accuracy of decision tree while using only 1% of available features = 96%

### Algorithm 4 : KNN

### Algorithm 5 : Adaboost

### Algorithm 6 : Random forest   