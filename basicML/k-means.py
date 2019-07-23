# import numpy as np
# import cv2
# from matplotlib import pyplot as plt
#
# X = np.random.randint(25,50,(25,2))
# Y = np.random.randint(60,85,(25,2))
# Z = np.vstack((X,Y))
#
# # convert to np.float32
# Z = np.float32(Z)
#
# # define criteria and apply kmeans()
# criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
# ret,label,center=cv2.kmeans(Z,2,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
#
# # Now separate the data, Note the flatten()
# A = Z[label.ravel()==0]
# B = Z[label.ravel()==1]
#
# # Plot the data
# plt.scatter(A[:,0],A[:,1])
# plt.scatter(B[:,0],B[:,1],c = 'r')
# plt.scatter(center[:,0],center[:,1],s = 80,c = 'y', marker = 's')
# plt.xlabel('Height'),plt.ylabel('Weight')
# plt.show()

import numpy as np
import cv2

img = cv2.imread("D:\MyTest\opencv\opencv-data\home.jpg")
Z = img.reshape((-1,3))

# convert to np.float32
Z = np.float32(Z)

# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 16
ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

# Now convert back into uint8, and make original image
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))

cv2.imshow('res2',res2)
cv2.waitKey(0)
cv2.destroyAllWindows()