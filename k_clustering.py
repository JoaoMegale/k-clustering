import numpy as np
import pandas as pd
import sys

def distance_minkowski (X, Y, p):
    '''
    Parameters
    ----------
    X : ponto 1
    Y : potno 2
    p : fator p
    
    Returns
    -------
    distancia de Minkowski entre os pontos X e Y
    
    '''
    return (np.sum((abs(X - Y)**p))) ** (1/p)


def get_distance_matrix (data, p):
    '''
    Parameters
    ----------
    data : dados em forma de vetor
    p : fator p da distancia de minkowski

    Returns
    -------
    matrix : matriz de distancias
    
    '''
    num_pontos = data.shape[0]
    matrix = np.zeros((num_pontos, num_pontos), dtype=float)
    for i in range (num_pontos):
        for j in range(num_pontos):
            matrix[i][j] = distance_minkowski(data[i], data[j], p)
    return matrix


def get_radius_and_labels (m, centers):
    '''
    Parameters
    ----------
    m : matriz de distancias
    centers : centros gerados pelo algoritmo 2-aproximativo

    Returns
    -------
    max_r : raio máximo da solução
    labels: labels da solução

    '''
    n = m.shape[0]
    points = [i for i in range(0, n)]
    
    distances = []
    labels = []
    # passa por cada ponto e armazena a distancia de seu centro mais proximo
    for point in points:
        min_dist = min(m[point][centers])
        closest_center = centers[np.argmin(m[point][centers])]
        distances.append(min_dist)
        labels.append(closest_center)
        
    max_r = max(distances)
    return max_r, labels


def get_kmeans_radius (centers, data, p):
    '''
    Parameters
    ----------
    centers : centros do kmeans
    data : dados em forma de vetor
    p : fator p da distancia de Minkowski

    Returns
    -------
    max_r : raio maximo
    '''
    
    distances = []
    for point in data:
        min_dist = sys.maxsize
        for center in centers:
            dist_cluster = distance_minkowski(center, point, p)
            if dist_cluster < min_dist:
                min_dist = dist_cluster
        distances.append(min_dist)
        
    max_r = max(distances)
    return max_r
        

def k_centers (m, k):
    '''
    Parameters
    ----------
    m : matriz de distancias
    k : numero de centros
    
    Returns
    -------
    centers_index : indice dos centros obtidos pelo algoritmo 2-aproximativo

    '''
    n = m.shape[0]
    points = [i for i in range(0, n)]
    
    random_point = np.random.randint(0, n)
    centers_index = [random_point]
    points.remove(random_point)
    
    while len(centers_index) < k:
        max_distance = 0
        for point in points:
            # pega a distancia de um ponto ao centro mais proximo
            min_dist_point = min(m[point][centers_index])
            # atualiza o ponto que está mais longe de qualquer centro
            if min_dist_point > max_distance:
                furthest_point = point
                max_distance = min_dist_point
                
        centers_index.append(furthest_point)
        points.remove(furthest_point)
        
    return centers_index
