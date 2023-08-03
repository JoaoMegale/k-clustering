import pandas as pd
import numpy as np
from sklearn.cluster import k_means
from sklearn.metrics import silhouette_score, adjusted_rand_score

from k_clustering import *

files = ["databases/1.data",
         "databases/2.txt",
         "databases/3.data",
         "databases/4.arff",
         "databases/5.data",
         "databases/6.txt",
         "databases/7.csv",
         "databases/8.csv",
         "databases/9.txt",
         "databases/10.csv"]

for file in files:
    # define o separador e header para ler o arquivo
    separador = input("Escreva o separador: ")
    header = input("Possui header? (Y/N): ")
    if header == 'N':
        df = pd.read_csv(file ,header=None, sep=separador)
    if header == 'Y':
        df = pd.read_csv(file, sep=separador)
        
    df = df.dropna()
    
    # lê colunas numericas
    numericas = input("Indice das colunas numericas: ").split(",")
    num = list(map(int,numericas))
    data = df.iloc[:, num].values
    
    # lê coluna categorica e define K
    categorica = int(input("Indice da coluna categorica: "))
    k = df.iloc[:, categorica].nunique()
    
    for p_distance in [1, 2]:
        
        if p_distance == 2:
            metrica = 'euclidean'
        else:
            metrica = 'manhattan'
    
        # calculo da matriz de distancias
        distance_matrix = get_distance_matrix(data, p_distance)
        
        
        # ALGORITMO 2-APROXIMATIVO
        
        # vetores para armazenar as informações
        raios_kcenters = []
        silhouette_scores_kcenters = []
        rand_scores_kcenters = []
        for i in range(30):
            centros_index = k_centers(distance_matrix, k, data)
            raio = get_radius_and_labels(distance_matrix, centros_index)[0]
            labels = get_radius_and_labels(distance_matrix, centros_index)[1]
            
            silhouette = silhouette_score(data, labels, metric=metrica)
            rand = adjusted_rand_score(labels, df.iloc[:, -1].values)
            
            raios_kcenters.append(raio)
            silhouette_scores_kcenters.append(silhouette)
            rand_scores_kcenters.append(rand)
            
        kcenters_results = pd.DataFrame(columns=['Radius', 'Silhouette', 'Adjusted Rand'])
        kcenters_results['Radius'] = raios_kcenters
        kcenters_results['Silhouette'] = silhouette_scores_kcenters
        kcenters_results['Adjusted Rand'] = rand_scores_kcenters
          
        
        # K-MEANS DO SKLEARN
        
        centers_kmeans, labels_kmeans, _ = k_means(X=data, n_clusters=k)
        
        kmeans_radius = get_kmeans_radius(centers_kmeans, data, p_distance)
        kmeans_silhouette = silhouette_score(data, labels_kmeans, metric=metrica)
        kmeans_rand = adjusted_rand_score(labels_kmeans, df.iloc[:, -1].values)
        
        kmeans_results = pd.DataFrame(columns=['Radius', 'Silhouette', 'Adjusted Rand'])
        kmeans_results['Radius'] = [kmeans_radius]
        kmeans_results['Silhouette'] = [kmeans_silhouette]
        kmeans_results['Adjusted Rand'] = [kmeans_rand]
        
        
        # RELATÓRIO
        
        print("\n\nSUMÁRIO PARA " + file + ":")
        
        print("Distancia: " + metrica + "\n")
        
        print("\nResultados médios:")
        print(kcenters_results.mean())
        
        print("\nResultados sklearn para comparação:")
        print(kmeans_results.mean())
        
        print("\n\n =============")
