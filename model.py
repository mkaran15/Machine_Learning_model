import pandas as pd
from keras.models import Sequential
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from keras.layers import Dense
from keras.optimizers import Adam

data = pd.read_csv('wines.csv')

Y = data['Class']
y = pd.get_dummies(Y)

X = data.drop('Class' , axis=1)

X_train,X_test,y_train,y_test=train_test_split(X, y, test_size=0.2, random_state=42)

sc=StandardScaler()
X_train=sc.fit_transform(X_train)

model  =  Sequential()
model.add(Dense(units=5, input_shape=(13,), activation='relu' ))
model.add(Dense(units=8, activation='relu',))
model.add(Dense(units=2, activation='relu'))
model.add(Dense(units=3, activation='softmax'))
model.compile(optimizer=Adam(lr=0.01),loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(X_train,y_train,epochs=10)

X_test=sc.transform(X_test)
y_pred=model.predict(X_test)

model.save('modelsave.h5')

history = model.history.history
accuracy = history["acc"][-1] * 100
print("\nAccuracy of this model is {}% .\n".format(accuracy))
