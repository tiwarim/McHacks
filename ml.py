#!python3
'''
Created on Sat Feb 01 11:44 2020

K-means anomaly detection for twitter flow.

@author Michael
'''
import sklearn
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import PCA, TruncatedSVD
from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans
import random
import seaborn as sns
import matplotlib.pyplot as plt


def Matrix_Normalize(X, tol=0.0001):
    '''

    Takes matrix of X of text representations and normalizes so each feature has mean 0 and std 1.

    Args:
        X (np.array): D x N matrix (D features/rows by N instances/columns)
        tol (float): numerical error tolerance, don't touch this
    Returns:
        X_norm (np.array): D x K (K < N) matrix with std=0 rows removed

    '''

    X_norm = X - X.mean(axis=1, keepdims=True)
    X_norm = X_norm[~np.all(X_norm == 0, axis=1)]
    X_norm /= np.std(X_norm, axis=1)[:, None]

    # Returns Normalization Error if every row isn't mean 0 or std 1
    assert (abs(np.mean(np.mean(X_norm, axis=1))) <= tol and abs(np.mean(np.std(X_norm, axis=1)) - 1) <= tol), 'Normalization Error'

    return X_norm

def Feature_Extraction(corpus, min_df=1, max_features=None, stop_words='english'):
    '''
    Converts tweet corpus into a CountVectorizer object.

    Args:
        corpus (list[str]): corpus of text bodies
        min_df (int): minimum frequency (count) of a word in documents, default to 1
        max_features (int): maximum number of features, defaults to unlimited
        stop_words (str): stop words used, defaults to 'english'

    Returns:
        cv (CountVectorizer object): fitted CountVectorizer
        arr (np.array): 
            matrix with words encoded D x N (features/rows x instances/columns) 
    '''

    # init CountVectorizer object
    cv = CountVectorizer(min_df=min_df, max_features=max_features, stop_words=stop_words)
    arr = cv.fit_transform(corpus)
    arr = arr.toarray().transpose()

    return cv, arr

def plot_pca(x, y, centers=np.array([]), new_data=np.array([])):
    '''
    Plots Hex JointPlot of the input vector X (which has D rows/features and N columns/instances), projects down via PCA to 2D for visualization.

    Args:
        x (np.array): projected x values
        y (np.array): projected y values
        centers (np.array): clustered centers (optional)
    Returns:
        None

    '''

    with sns.axes_style('white'):
        g = sns.jointplot(x, y, kind='scatter')

        # overlay the projected clustered centers
        if centers.any():
            # plot cluster centers
            g.ax_joint.plot(centers[0], centers[1], '+', color='r')
            # new datapoint
            g.ax_joint.plot(new_data[0], new_data[1], '+', color='#eb9b05')

        plt.show()



def project_pca(X):
    '''
    Performs PCA projection into 2D.

    Args:
        X (np.array): input vector X
    Returns:
        x (np.array): PCA projected x values
        y (np.array): PCA projected y values
        pca (PCA object): fitted PCA object
    '''

    # fits PCA Projection
    pca = PCA(n_components=2)
    X2 = pca.fit_transform(X)

    X2 = X2.transpose()

    x = X2[0]
    y = X2[1]

    return x, y, pca

def cluster(X, n_clusters=3):
    '''
    Performs K-Means Clustering on the input matrix X. Default number of clusters set to 3.

    Args:
        X (np.array): input matrix
        n_clusters (int): number of clusters, defaults to 3
        
    Returns:
        centers (np.array): 
            n_clusters x D, each row represents a cluster center, each column represents a feature
        labels (np.array):
            N x 1, each entry represents the clustering classification for the instance number
        kmeans (KMeans Object): Fitted Classifier

    '''

    X = X.transpose()

    # fit KMeans classifier
    kmeans = KMeans(n_clusters=n_clusters, random_state=0)
    kmeans.fit(X)

    centers = kmeans.cluster_centers_
    labels = kmeans.labels_

    return centers, labels, kmeans


def anomaly_detection(corpus, new_data, vis=False, c_num=[2], features=100, log=False):
    '''
    Checks to see if the new_data is anomalous for the user based on kmeans clustering distances.

    Args:
        corpus (list[str]): list of tweet text
        new_data (list[str]): new input text
        vis (boolean): visualize in 2D PCA projected plane, defaults to False
        c_num (list[int]): number of clusters to try, defaults to [2]
        features (int): maximum number of features, defaults to 100
        log (boolean): if True, prints a bunch of data

    Returns:
        (boolean): 
            True if anomalous, False if within a standard deviation of normal twitter behavior
    '''

    cv, X = Feature_Extraction(corpus, 1, features)

    # vectorize new data
    x2 = cv.transform(new_data).toarray()


    best = 2 #by default
    best_centers = None
    best_labels = None
    best_km = None

    # compute max silhouette score for the given c_num list, and keep the best centers/labels/kmeans_classifier
    max_score = -float('inf')
    for i in c_num:
        centers, labels, km = cluster(X, i)
        
        t = silhouette_score(X.transpose(), labels)
        if t > max_score:
            best = i 
            max_score = t
            best_centers = np.copy(centers)
            best_labels = np.copy(labels)
            best_km = km



    # pca for visualization
    if vis:
        x, y, pca = project_pca(X.transpose())
        centers_projected = pca.transform(best_centers)
        centers_projected = centers_projected.transpose()

        new_data = pca.transform(x2)
        new_data = new_data.transpose()
        plot_pca(x, y, centers_projected, new_data)


    predicted_cluster = best_km.predict(x2)



    # coordinates for the predicted center
    c = centers[predicted_cluster]

    distances = []
    # get all distances for the predicted cluster
    for i, l in enumerate(best_labels):
        if l == predicted_cluster:
            distances.append((np.linalg.norm(c - X.transpose()[i])))


    # compute statistics
    input_dist = np.linalg.norm(c - x2)
    mean_dist = np.mean(distances)
    std_dist = np.std(distances)


    # if the input_dist is within one standard deviation of the mean it is not anomalous
    if abs(mean_dist - input_dist) > std_dist:
        result = True
    else:
        result = False

    # if log is True print out a bunch of data
    if log:
        print('Best Silhouette Score:              {}\nBest Cluster Number:                {}'.format(max_score, best))
        print('Mean Distance for Cluster:          {}\nStandard Deviation for Cluster:     {}\nInput Distance from Cluster Center: {}\nAnomalous:                          {}'.format(mean_dist, std_dist, input_dist, result))


    return result
    


    


# if __name__ == '__main__':
#     strings = []

#     with open('temp.txt', 'r') as f:
#         for line in f.readlines():
#             strings.append(line.rstrip())
            
#     random.seed(420)
#     l = random.sample(strings, 1000)

#     # t = ['barely character, comedy, director film yeet']
#     t = ['the movie is pretty boring not all that great kind of flat bland']
#     anomaly_detection(l, t, True, [2, 3, 4], 10, True)




