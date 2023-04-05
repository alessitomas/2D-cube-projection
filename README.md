# 2D-cube-projection

# Passo a passo para rodar o projeto


# Descrição do modelo matemático do projeto
    
Matriz inicial do Cubo 3D

$$
cubo_3d = \begin{bmatrix}
X1 & X2 & X3 & X4 & X5 & X6 & X7 & X8\\
Y1 & Y2 & Y3 & Y4 & Y5 & Y6 & Y7 & Y8\\
Z1 & Z2 & Z3 & Z4 & Z5 & Z6 & Z7 & Z8\\
\end{bmatrix}
\hspace{0.5in}
$$
    
Matriz Final Desejada representação do Cubo 2D

$$
projecoes_2d = \begin{bmatrix}
X1p & X2p & X3p & X4p & X5p & X6p & X7p & X8p\\
Y1p & Y2p & Y3p & Y4p & Y5p & Y6p & Y7p & Y8p
\end{bmatrix}
\hspace{0.5in}
$$

## Representação 2D do Cubo em 3D 
    
Objetivo: Para representar o cubo em 2D, é necessário encontrar as projeções Xp e YP das coordenadas de cada ponto do cubo 3D.

Passo 1: Encontrar as projeções Xp dos pontos do Cubo.

- Para isso vamos assumir um ponto genérico (Xo,Yo,Zo) do cubo.
- Como queremos encontrar apenas a projeção de X nesse momento, iremos imaginar que esse ponto não pode se movimentar no eixo y.
- Neste momento, vamos usar conhecimentos de geometria para simular uma câmera no espaço 2D - mais especificamente, o plano cartesiano $x,z$

* O *pinhole*, que é o buraco por onde a luz entra, ficará exatamente na origem do plano cartesiano, isto é, no ponto $[0,0]$.
* O anteparo está a uma distância $d$ do *pinhole*
* O anteparo ficará sobre a reta $z=-d$, que é a reta horizontal que passa pelo ponto $[0,-d]$.

Um ponto que está no ponto $[x_o,z_o]$ deverá ser projetado no anteparo no ponto $[x_p, z_p]$:

Onde, x_p será a nossa projeção de x desejada e z_p será constante e igual a -d.
    
 
### Encontrando um sistema linear, envolvendo o Xp.

<img src="equa.jpg">

### Sitema de equação considerando a projecao em X
* Como demonstrado na imagem chegamos no Sitema de equação considerando a projecao em X.

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
* Para encontrar a projeção em Y podemos repetir o mesmo processo, encontraremos o Sitema de equação considerando a projecao em Y

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
* Com os dois sistemas, podemos selecionar apenas as equações que contenham a projeção Xp e yp, e o valor da incógnita W, que será necessária para encontrar os valores de Xp e Yp. Com isso montamos o Sitema de equação considerando as projecoes em X e Y (2D)

$$ 
\begin{cases}
    \begin{aligned}
    W * Xp & = Xo \\
    W * Yp & = Yo \\
    W & = Zo / -d \\
    \end{aligned}
\end{cases}
$$

### Representação matricial do sistema linear encontrado.

$$
Matriz Projecao = 
\begin{bmatrix}
    1 & 0 & 0 \\
    0 & 1 & 0 \\
    0 & 0 & -1/d
\end{bmatrix}
$$

$$
original = 
\begin{bmatrix}
    Xo \\
    Yo\\
    Zo
\end{bmatrix}
$$

$$
projecao = 
\begin{bmatrix}
    Xp * W \\
    Yp * W \\
       W
\end{bmatrix}
$$

PROJECAO = ORIGINAL @ MATRIZ PROJECAO

Onde @ representa multiplicação matricial.

### Aplicando a representação matricial, para o exemplo dos vértices de um Cubo 3D.

$$
cubo_3d = \begin{bmatrix}
X1 & X2 & X3 & X4 & X5 & X6 & X7 & X8\\
Y1 & Y2 & Y3 & Y4 & Y5 & Y6 & Y7 & Y8\\
Z1 & Z2 & Z3 & Z4 & Z5 & Z6 & Z7 & Z8\\
\end{bmatrix}
\hspace{0.5in}
$$

$$
Matriz Projecao = 
\begin{bmatrix}
    1 & 0 & 0 \\
    0 & 1 & 0 \\
    0 & 0 & -1/d
\end{bmatrix}
$$

cubo_2d = cubo_3d @ MATRIZ PROJECAO

$$
cubo_2d = \begin{bmatrix}
W * Xp1 & W * Xp2 & W * Xp3 & W * Xp4 & W * Xp5 & W * Xp6 & W * Xp7 & W * Xp8\\
W * Yp1 & W * Yp2 & W * Yp3 & W * Yp4 & W * Yp5 & W * Yp6 & W * Yp7 & W * Yp8\\
W & W & W & W & W & W & W & W\\
\end{bmatrix}
\hspace{0.5in}
$$

### Projeções em 2D encontradas


$$
projecoes_2d = \begin{bmatrix}
X1p & X2p & X3p & X4p & X5p & X6p & X7p & X8p\\
Y1p & Y2p & Y3p & Y4p & Y5p & Y6p & Y7p & Y8p
\end{bmatrix}
\hspace{0.5in}
$$




    
