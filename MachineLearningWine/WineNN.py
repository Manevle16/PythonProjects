from sklearn import datasets
from sklearn import tree
from sklearn.model_selection import train_test_split as tts
from sklearn.ensemble import RandomForestClassifier

wineDS = datasets.load_wine()
features = wineDS.data
labels = wineDS.target


train_feats, test_feats, train_labels, test_labels = tts(features, labels, test_size=0.2)

print("Number of entries: " + str(len(test_feats)))
for name in wineDS.feature_names:
    print(name[:10], end="    \t")
print("Class")
for feature, label in zip(test_feats, test_labels):
    for f in feature:
        print(f, end="\t\t")
    print(label)

wineGuesser = RandomForestClassifier()

# train
wineGuesser.fit(train_feats, train_labels)

predictions = wineGuesser.predict(test_feats)
print(predictions)

accuracy = 0
for i in range(len(predictions)):
    if predictions[i] == test_labels[i]:
        accuracy += 1

print(accuracy/len(predictions))
