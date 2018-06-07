from sklearn import tree

X= [[181,80,44],[177,70,43],[160,60,38],[166,65,40],[190,90,47],[175,64,39],[170,70,40],[171,75,42],[181,85,43]]
Y= ['male','female','female','female','male','male','female','male','male']

clf= tree.DecisionTreeClassifier()
clf= clf.fit(X,Y)
Prediction= clf.predict([[191,70,43]]) 
print (Prediction)
