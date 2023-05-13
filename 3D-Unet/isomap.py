import numpy as np
from sklearn.manifold import Isomap
 
data = np.load("/Users/lijingyi/Desktop/npy_test/npy/c0008.npy")
isomap = Isomap(n_components=2,n_neighbors=5,path_method="auto")
data_2d = isomap.fit_transform(X=data)
geo_distance_metrix = isomap.dist_matrix_ # 测地距离矩阵，shape=[n_sample,n_sample]

