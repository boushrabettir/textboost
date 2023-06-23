# Possibility of getting a folder on their downloads, 
# and look in that folder and there can be subsections like Downloads/food or 
# Downloads/makeup or Downloads/clothing etc. And dependent on the context of the 
# outputted pdf, the machine learning algorithm will place the pdf in their respected folder

import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans


X = ["Games","I enjoy history", "History is a nice topic", "Historyyy", "Makeup is so overrated.", "I love animals like cats", "Dogs are my favorite.", "Chicken is good"]
y = [4,0, 0, 0, 1, 2,2, 3]


vectorizer = TfidfVectorizer()
X_transformed = vectorizer.fit_transform(X)
print(X_transformed)

list_of_inertia = []
for i in range(1, 8):
    kmeans = KMeans(n_clusters=i)
    kmeans.fit(X_transformed)
    list_of_inertia.append(kmeans.inertia_)

# Plot the elbow curve
plt.plot(range(1, 8), list_of_inertia, marker="o")
plt.xlabel("Number of Clusters (k)")
plt.ylabel("Inertia")
plt.title("Elbow Method")
plt.show()
