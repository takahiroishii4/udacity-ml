def doPCA():
    from sklearn.decomposition import PCA
    pca = PCA(n_component=2)
    pca.fit(data)
    return pca

pca = doPCA()
print(pca.explained_variance_ratio_) #tells how much the first PC explains the dataset
first_pc = pca.components_[0]
second_pc = pca.components_[1]

transformed_data = pca.transform(data)
for ii, jj in zip(transformed_data, data):
    plt.scatter( first_pc[0])
