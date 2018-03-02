import csv
import math
import matplotlib.pyplot as plt
import numpy as np
from numpy import array
from sklearn.cluster import KMeans

def plot_graph(clusters, plot_flag):
    if plot_flag:
        fig = plt.figure()
        ax = fig.add_subplot(111)
        markers = ['o', 'd', 'x', 'h', 'H', 7, 4, 5, 6, '8', 'p', ',', '+', '.', 's', '*', 3, 0, 1, 2]
        colors = ['r', 'k', 'b', [0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0],
                  [1, 1, 1]]
        ## third arg : c = colors[cnt]
        cnt = 4
        for cluster in clusters.values():
            #print (cluster, " jianjsdnfckjsdbf")
            feat1 = []
            feat2 = []
            for point in cluster:
                #print (point, "point")
                feat1.append(point[0]) ### feat 1  = cosine_sim
                feat2.append(point[1]) ### feat 2  = len of comment

                #feat2.append(point[2]) ### feat 3  = readability of comment
                #feat2.append(point[2]) ### feat 4  = similarity between comment and Method name
            ax.scatter(feat2, feat1, s=60 ,c = colors[cnt])
            cnt += 1
        plt.show()

def assign_points(data_points, means):
    clusters = dict()
    for point in data_points:
        dist = []
        # find the best cluster for this node
        for mean in means:
            dist.append(math.sqrt(math.pow(float(point[0]) - float(mean[0]), 2.0) + math.pow(float(point[1]) - float(mean[1]), 2.0)))
        # let's find the smallest mean
        cnt_ = 0
        index = 0
        min_ = dist[0]
        for d in dist:
            if d < min_:
                min_ = d
                index = cnt_
            cnt_ += 1

        clusters.setdefault(index, []).append(point)
    return clusters

def compute_mean(clusters):
    means = []
    for cluster in clusters.values():
        mean_point = [0.0, 0.0, 0.0, 0.0]
        cnt = 0.0
        for point in cluster:
            mean_point[0] += float(point[0])
            mean_point[1] += float(point[1])
            
            cnt += 1.0

        mean_point[0] = mean_point[0] / cnt
        mean_point[1] = mean_point[1] / cnt
        means.append(mean_point)
    return means

def update_means(old_means ,new_means, threshold):
    # check the current mean with the previous one to see if we should stop
    for i in range(len(old_means)):
        mean_1 = old_means[i]
        mean_2 = new_means[i]
        diff = math.sqrt(math.pow(mean_1[0] - mean_2[0], 2.0) + math.pow(mean_1[1] - mean_2[1], 2.0))
        print("diff between prev and curr mean :" ,diff)
        if diff > threshold:
            return False

    return True

def print_means(means):
    print("Printing both means for this iteration :")
    for point in means:
        print("%f %f %f %f" % (point[0], point[1], point[2], point[3]))

def k_means(data_points,k,means,plot_flag,threshold):

        cluster = dict()

        for i in range(k):
            cluster[i] = []
    
        # tmp = np.asarray(data_points)
        # data_points = tmp.reshape((48, 4))
        # print(tmp.shape , " kasndksa")
        tmp  = []
        for i in range(len(data_points)):
            tmp.append(data_points[i])
        data_points = np.array(tmp)

        #print(data_points, "jnhkjhkhk454545454datapoint")

        kmeans = KMeans(n_clusters=k, random_state=0).fit(data_points)
        for i in range(len(data_points)):
            print(data_points[i], "Before")
            prediction = kmeans.predict(data_points[i].reshape(1,-1))
            print(data_points[i], "After")
            predictioni = prediction[0]
            cluster[predictioni].append(data_points[i].tolist())
           
        


        # clusters = dict()
        # if len(data_points) < k:
        #     return -1  # error
        # #### means is initial mean set #####
        # stop = False
        # iter = 1
        # old_means = means
        # print("Starting k means iterations.")
        # while not stop:
        #     # assignment step: assign each node to the cluster with the closest mean
        #     print("######iteration :" , iter, "completed###############################")
        #     clusters = assign_points(data_points,old_means)
        #     new_means = compute_mean(clusters)
        #     print_means(new_means)
        #     stop = update_means(old_means,new_means, threshold)
        #     if not stop:
        #         old_means = new_means

        #     iter +=1

        # clusters = clusters
        # print("Convergence !!! Stoping k means algorithm.")
        plot_graph(cluster, plot_flag)
        return cluster

def pca(X = np.array([]), initial_dims = 50):
    """
    Runs PCA on the N x D array X in order to reduce its dimensionality to no_dims dimensions.
    Inputs:
    - X: An array with shape N x D where N is the number of examples and D is the
         dimensionality of original data.
    - initial_dims: A scalar indicates the output dimension of examples after performing PCA.
    Returns:
    - Y: An array with shape N x initial_dims where N is the number of examples and initial_dims is the
         dimensionality of output examples. intial_dims should be smaller than D, which is the
         dimensionality of original examples.
    """

    print ("Preprocessing the data using PCA...")
    
    Y = np.zeros((X.shape[0],initial_dims))
    
    # start your code here

    X =  np.subtract(X, np.mean(X,axis=0))

    # Xt = np.transpose(X)
    # S = np.divide( Xt.dot(X), len(X))

    # print(X.shape, " X shape")

    S = np.cov(np.transpose(X))

    # print(S.shape, "S shape")

    w,v = np.linalg.eig(S)

    # print w[0], "Value"

    # print v[:,0], "Vector"

    # print(w.shape, "w shape")

    # print(v.shape, "v shape")
    #print w, "W"
    #print v, "V"

    v = np.transpose(v)

    zipped = sorted(zip(w,v), key=lambda x: x[0])[::-1]
    lambdas, vectors = zip(*zipped)

    # print(len(vectors), " Vectors")
    # print(len(vectors[0]), " Vectors")

    #print(vectors[0:2])

    u = np.array(vectors)[:50,:]
    # print u.shape, "Shape of u"

    Y = np.dot(X,np.transpose(u))

    # print Y.shape, "Shape of Y"
    # print Y

    return Y



if __name__=="__main__":

    data_points = []

    clusters = dict()  # clusters of nodes

    ########################################################
    # data point format : data_points = [feat1,feat2,feat3,feat4]
    # feat1  = cosine_similarity
    # feat2  = len of comment
    # feat3  = readability of comment
    # feat4  = similarity between comment and Method name
    ########################################################


    ######### 0th point (For making same index as data set)#############################
    #data_points.append([0.1199,65,13.31,0.5023])
    ####################################################################################


    ########################Update data points#####################################
    f = open('/Users/pratnaik/PycharmProjects/code_comments-master/Points.csv', 'r')
    reader = csv.reader(f, delimiter=",")
    for line in reader:
        if(len(line)==0):
            continue
        point = []  # tuples for point
        #print(line, "LINE")
        point.append(float(line[2])) # feat1  = cosine_similarity
        point.append(float(line[3])) # feat2  = len of comment
        point.append(float(line[4])) # feat3  = readability of comment
        point.append(float(line[5])) # feat4  = similarity between comment and Method name
        point.append(float(line[0]))
        data_points.append(point)

    data_points = pca(np.asarray(data_points))
    ###############################################################################


    ###################### Parameters for kmeans function ########################
    threshold = 0.01
    plot_flag = True
    k = 2
    ##############################################################################

    print("Printing data points :" ,data_points)
    print("Printing threshold : ", threshold)
    print("Printing number of clusters (K) :" , k)

    ######### Initialize means #####################################################################
    means = []  # means of clusters
    means.append(data_points[0]) # non coherent
    means.append(data_points[1]) # coherent

    ################################################################################################
    clusters = k_means(data_points,k,means,plot_flag ,threshold)
    ################################################################################################
    print("Length of (CLUSTER 0):", len(clusters[0]))
    print("Length of (CLUSTER 1):", len(clusters[1]))

    print("(CLUSTER 0):" , clusters[0])
    print("(CLUSTER 1):" , clusters[1])