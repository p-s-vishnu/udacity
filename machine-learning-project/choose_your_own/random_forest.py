
from initialize import initialize
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture
from sklearn.ensemble import RandomForestClassifier

# visualize training data
initialize()
features_train, labels_train, features_test, labels_test = makeTerrainData()

# train classifier
clf = RandomForestClassifier()
clf.fit(features_train, labels_train)
print clf.score(features_test, labels_test)
print(clf.feature_importances_)

# display decision boundary
try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
