# R-squares algorithms
# Ordinary least squares (OLS) - sklearn LinearRegression
# Gradient descent



from sklearn import linear_model
reg = linear_model.LinearRegression()
reg.fit(input, output)

slope = reg.coef_
intercept = reg.intercept_

predict = reg.predict(list_of_values)

r-squared_score = reg.score(input_test, output_test)

# visulization
import matplotlib.pyplot as plt
plt.scatter(features, output)
ply.plot(features, reg.predict(features), color="blue", linewidth=3)
plt.xlabel("features")
plt.ylabel("output")
plt.show()
