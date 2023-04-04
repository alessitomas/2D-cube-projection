# 2D-cube-projection

# Passo a passo para rodar o projeto


# Descrição do modelo matemático do projeto

## Representação 2D de Cubo em 3D 

Matriw do cubo 3D:
    
    -  8 Vértices do cubo, e cada vértice possui 3 coordenadas (x, y, z)
    
    -  Cada linha representa uma coordenada do vértice
    
    -  Cada coluna representa um vértice do cubo


$$
cubo = \begin{bmatrix}
x1 & x2 & x3 & x4 & x5 & x6 & x7 & x8\\
y1 & y2 & y3 & y4 & y5 & y6 & y7 & y8\\
z1 & z2 & z3 & z4 & z5 & z6 & z7 & z8\\
\end{bmatrix}
\hspace{0.5in}
$$

<img src="equacao.png">


$$
M_projecao = \begin{bmatrix}
1 & 0 & 0\\
0 & 1 & 0\\
0 & 0 & -1/d\\
\end{bmatrix}
\hspace{0.5in}
$$



$$
cubo_2d = \begin{bmatrix}
w * xp1 & w * xp2 & w * xp3 & w * xp4 & w * xp5 & w * xp6 & w * xp7 & w * xp8\\
w * yp1 & w * yp2 & w * yp3 & w * yp4 & w * yp5 & w * yp6 & w * yp7 & w * yp8\\
w & w & w & w & w & w & w & w\\
\end{bmatrix}
\hspace{0.5in}
$$
    
