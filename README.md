# k-clustering

Objetivos
---------

Nesse trabalho serão abordados os aspectos práticos relacionados à implementação
de algoritmos aproximativos. Especificamente, abordaremos o problema dos k-centros,
útil na tarefa de agrupamento em aprendizado de máquinas.

Abordaremos também questões de comparação empírica de algoritmos/programas. Nesse
sentido, vamos comparar a implementação do algoritmo 2-aproximado para o problema
do k-centro com o algoritmo clássico para o problema de agrupamento (K-Means). As
comparações deverão avaliar tanto aspectos de demanda computacional quanto de qualidade
de solução.

Tarefas
-------

Os alunos deverão implementar o algoritmo 2-aproximado visto em aula usando a
linguagem Python 3. Deverão ser implementadas também todas as funções auxiliares
envolvidas no algoritmo. Isto é, deverão ser implementadas funções para o cálculo
de distâncias.

Os alunos deverão implementar a função de distância de Minkowski, a qual deverá ser avaliada
nos experimentos com diferentes valores de p≥1 (obrigatoriamente deverão ser testados p=1 e 2,
as quais equivalem, respectivamente, a distância Manhattan e Euclidiana). A implementação
deverá ser feita usando funções vetoriais com a biblioteca NumPy.

Tendo implementado o algoritmo para agrupamento e a métrica de distância, o próximo passo
é a avaliação empírica do método. O método deverá ser avaliado com conjunto de dados
obtidos na UCI Machine Learning Repository (referência abaixo). Devem ser escolhidos
10 conjuntos de dados com, no mínimo, 700 exemplos (instâncias). Os conjuntos de dados
devem ser exclusivamente numéricos para a tarefa de classificação (o atributo classe/label)
deve ser ignorado durante o agrupamento cálculo de distância; o número de valores distintos
para essa variável determina o número de grupos/clusters a buscar. Embora o algoritmo seja
2-aproximado, a escolha dos centros é arbitrária e pode influenciar na qualidade da solução.
Dessa forma, para cada conjunto de dados, deverão ser realizados 30 testes/execuções do
algoritmo (note que a matriz de distância deve ser computada uma única vez, pois essa
nunca se altera). A cada execução deve-se armazenar o raio da solução e também computar
duas medidas clássicas em avaliação de agrupamentos: silhueta e índice de Rand ajustado.
Essas duas últimas métricas não precisam ser implementadas, devendo ser usadas as implementações
da biblioteca Scikit Learn (https://scikit-learn.org/stable/index.html). Além das métricas
de qualidade, deverão ser armazenados também o tempo de processamento de cada execução.

A título de comparação da qualidade da solução, os experimentos acima deverão ser repetidos
com a implementação do algoritmo K-Means também disponível no Scikit Learn 
(https://scikit-learn.org/stable/modules/clustering.html#k-means). Observe que todas
as medidas de desempenho também deverão ser computadas para essa implementação.
