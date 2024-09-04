import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
df = pd.read_csv('customer_data.csv')
print("Sample of the Data:")
print(df.head())
features = df[['total_amount', 'purchase_count', 'avg_value']]
scaler = StandardScaler()
scaled_data = scaler.fit_transform(features)
n_clusters = 4
kmeans = KMeans(n_clusters=n_clusters, random_state=123)
df['group'] = kmeans.fit_predict(scaled_data)
tsne = TSNE(n_components=2, perplexity=2, random_state=123)
tsne_results = tsne.fit_transform(scaled_data)
tsne_df = pd.DataFrame(data=tsne_results, columns=['Component1', 'Component2'])
tsne_df['group'] = df['group']
colors = ['purple', 'orange', 'teal', 'pink']
plt.figure(figsize=(12, 8))
scatter = plt.scatter(tsne_df['Component1'], tsne_df['Component2'], c=tsne_df['group'], cmap=mcolors.ListedColormap(colors), edgecolor='k', s=100)
plt.title('Customer Segmentation with K-Means and t-SNE')
plt.xlabel('t-SNE Feature 1')
plt.ylabel('t-SNE Feature 2')
legend_labels = [f'Group {i}' for i in range(n_clusters)]
handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=colors[i], markersize=10, linestyle='') for i in range(n_clusters)]
plt.legend(handles, legend_labels, title='Group')
plt.colorbar(scatter, label='Group')
plt.show()
print("\nData with Group Labels:")
print(df.head())