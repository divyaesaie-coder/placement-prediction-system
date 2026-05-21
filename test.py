import pandas as pd

df = pd.read_csv(r"C:\Users\Admin\Downloads\archive\Student Placement Dataset\train.csv")

# remove ID
df = df.drop("Student_ID",axis=1)

# convert target column
df["Placement_Status"] = df["Placement_Status"].map({
    "Placed":1,
    "Not Placed":0
})

# convert text columns
df = pd.get_dummies(
    df,
    columns=["Gender","Degree","Branch"],
    drop_first=True
)

print(df.head())

print("\nShape:")
print(df.shape)
X = df.drop("Placement_Status", axis=1)
y = df["Placement_Status"]

print("X shape:", X.shape)
print("y shape:", y.shape)
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("X_train:", X_train.shape)
print("X_test:", X_test.shape)
print("y_train:", y_train.shape)
print("y_test:", y_test.shape)
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)

print(X_train[:5])
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

model = LogisticRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier()

knn.fit(X_train, y_train)

knn_pred = knn.predict(X_test)

print("KNN Accuracy:",
      accuracy_score(y_test, knn_pred))
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier()

rf.fit(X_train, y_train)

rf_pred = rf.predict(X_test)

print(
    "Random Forest Accuracy:",
    accuracy_score(y_test, rf_pred)
)
from sklearn.model_selection import cross_val_score

scores = cross_val_score(
    rf,
    X,
    y,
    cv=5
)

print(scores)
print("Average:", scores.mean())
feature_names = X.columns

importance = rf.feature_importances_

for name, score in zip(feature_names, importance):
    print(name, ":", score)
    import pickle

pickle.dump(rf,
            open("placement_model.pkl","wb"))

print("Model saved successfully")
new_student = [[
    21,
    5.2,   # low CGPA
    0,     # no internships
    0,     # no projects
    40,    # low coding
    35,    # low communication
    45,
    2,
    0,
    5,     # many backlogs
    1,
    1,
    0,
    0,
    0,
    0,
    1,
    0
]]

prediction = rf.predict(new_student)

if prediction[0] == 1:
    print("Placed")
else:
    print("Not Placed")
