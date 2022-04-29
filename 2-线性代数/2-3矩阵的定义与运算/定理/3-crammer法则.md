一个线性方程组可以用矩阵与向量的方程来表示:
$$
A x=c
$$
其中的 $A$ 是一个 $n \times n$ 的方块矩阵，而向量 $x=\left(x_{1}, x_{2}, \cdots x_{n}\right)^{T}$ 是一个长度为 $\mathbf{n}$ 的行向量(大陆为列向量)。 $c=\left(c_{1}, c_{2}, \cdots c_{n}\right)^{T}$ 也一样。 克莱姆法则说明: 
如果 $A$ 是一个可逆矩阵（ $\operatorname{det} A \neq 0)$ ，那么方程有唯一解 $x=\left(x_{1}, x_{2}, \cdots x_{n}\right)^{T}$ ，其中 $x_{i}=\frac{\operatorname{det}\left(A_{i}\right)}{\operatorname{det}(A)}(1)$
当中 $x_{i}$ 是列向量 $x$ 的第 $i$ 行 (行向量与列向量不一样，解释默认列向量)
