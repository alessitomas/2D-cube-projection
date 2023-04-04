# 2D-cube-projection

# Passo a passo para rodar o projeto


# Descrição do modelo matemático do projeto

## Representação 2D de Cubo em 3D 

MatriW do cubo 3D:
    
    -  8 Vértices do cubo, e cada vértice possui 3 coordenadas (X, Y, z)
    
    -  Cada linha representa uma coordenada do vértice
    
    -  Cada coluna representa um vértice do cubo


$$
cubo = \begin{bmatriX}
X1 & X2 & X3 & X4 & X5 & X6 & X7 & X8\\
Y1 & Y2 & Y3 & Y4 & Y5 & Y6 & Y7 & Y8\\
z1 & z2 & z3 & z4 & z5 & z6 & z7 & z8\\
\end{bmatriX}
\hspace{0.5in}
$$

### Chegando na Matriz projeção

<img src="equa.jpg">

### Sitema de equação considerando a projecao em X

$$ 
\begin{cases}
    \begin{aligned}
    Zp & = -d \\
    W * Xp & = Xo \\
    W & = Zo / -d \\
    \end{aligned}
\end{cases}
$$

### Sitema de equação considerando a projecao em Y

$$ 
\begin{cases}
    \begin{aligned}
    Zp & = -d \\
    W * Yp & = Yo \\
    W & = Zo / -d \\
    \end{aligned}
\end{cases}
$$

### Sitema de equação considerando as projecoes em X e Y (2D)

$$ 
\begin{cases}
    \begin{aligned}
    W * Xp & = Xo \\
    W * Yp & = Yo \\
    W & = Zo / -d \\
    \end{aligned}
\end{cases}
$$

### Matriz de projeção


$$
\begin{bmatrix}
Xo\\
Yo\\
Zo\\
\end{bmatrix}
\begin{bmatrix}
1 & 0 & 0\\
0 & 1 & 0\\
0 & 0 & -1/d\\
\end{bmatrix}
=
\begin{bmatrix}
W * Xp\\
W * Yp\\
W\\
\end{bmatrix}
$$



$$
cubo_2d = \begin{bmatrix}
W * Xp1 & W * Xp2 & W * Xp3 & W * Xp4 & W * Xp5 & W * Xp6 & W * Xp7 & W * Xp8\\
W * Yp1 & W * Yp2 & W * Yp3 & W * Yp4 & W * Yp5 & W * Yp6 & W * Yp7 & W * Yp8\\
W & W & W & W & W & W & W & W\\
\end{bmatrix}
\hspace{0.5in}
$$
    
