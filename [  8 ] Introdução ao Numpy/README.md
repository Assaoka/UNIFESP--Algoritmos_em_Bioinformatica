<h1 align="center">Numpy 1 <br>
  <a href="../[  7 ] Seminário - Banco de Dados de Sequências de Proteínas/"><img src="https://img.shields.io/badge/Anterior-Seminário-215a36" alt="Anterior"></a>
</h1>

# Exercícios:
## 1. Crie um array unidimensional com valores aleatórios e imprima o valor médio e a mediana.
~~~python
import numpy as np
a = np.random.rand(10)

print(f'Média: {np.mean(a)}')
print(f'Mediana: {np.median(a)}')
~~~ 

## 2. Crie um array unidimensional com valores aleatórios e inverta a ordem dos elementos.
~~~python
import numpy as np
a = np.random.rand(10)

print(f'Array original: {a}')
print(f'Array invertido: {a[::-1]}')
~~~

## 3. Crie um array unidimensional com valores aleatórios e calcule a diferença entre cada elemento e o próximo elemento.
~~~python
import numpy as np
a = np.random.rand(10)

print(f'Array original: {a}')
print(f'Diferença entre elementos: {np.diff(a)}')
~~~

## 4. Crie uma matriz de zeros de tamanho 10x10 e adicione uma borda de valor 1.
~~~python
import numpy as np
a = np.zeros((10,10))
a[0:10, 0:10:9] = 1 # Bordas horizontais
a[0:10:9, 1:10] = 1 # Bordas verticais

print(a)
~~~

## 5. Crie um array unidimensional com valores aleatórios e encontre o índice do valor mais próximo de um valor fornecido.
~~~python
import numpy as np

dados = np.random.rand(3)
x = 0.5
indice_proximo = np.abs(dados - x).argmin()

print(f"Array: {dados}")
print(f"Valor mais próximo de x: {dados[indice_proximo]}")
print(f"Índice do valor mais próximo: {indice_proximo}")
~~~

## 6. Crie um array unidimensional com valores aleatórios e encontre os valores únicos e suas contagens.
~~~python
import numpy as np

dados = np.random.randint(0, 10, 10)
valores, contagens = np.unique(dados, return_counts=True)

print(f"Array: {dados}")
print(f"Valores únicos: {valores}")
print(f"Contagens: {contagens}")
~~~

---