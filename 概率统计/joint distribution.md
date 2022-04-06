# definition

 $\left(X_{1}, \cdots, X_{n}\right)$ 是定义在某个概率空间 $(\Omega, \mathscr{F}, \mathbf{P})$ 上的 $n$ 维随机向量, 当且仅当
$$
\begin{aligned}
\left\{\omega \mid X_{1}(\omega) \leqslant x_{1}, \cdots, X_{n}(\omega) \leqslant x_{n}\right\}=&\left(X_{1} \leqslant x_{1}, \cdots, X_{n} \leqslant x_{n}\right) \in \mathscr{F}, \\
& \forall\left(x_{1}, \cdots, x_{n}\right) \in \mathbb{R}^{n}
\end{aligned}
$$
证明 如果 $\left(X_{1}, \cdots, X_{n}\right)$ 是一个概率空间 $(\Omega, \mathscr{F}, \mathbf{P})$ 上的 $n$ 维随机向量, 那 么 $X_{1}, \cdots, X_{n}$ 就是定义在同一个概率空间上的 $\mid n$ 个随机变量, 所以
$$
\left(X_{1} \leqslant x_{1}, \cdots, X_{n} \leqslant x_{n}\right)=\bigcap_{j=1}^{n}\left(X_{j} \leqslant x_{j}\right) \in \mathscr{F} .
$$

# 计算方法

$4^{\circ} F\left(x_{1}, \cdots, x_{n}\right)$ 具有下述意义上的增量非负性: 对任何 $a_{j} \leqslant b_{j}, j=1, \cdots, n$, 都有
$$
\Delta_{\left(a_{1}, \cdots, a_{n}\right)}^{\left(b_{1}, \cdots, b_{n}\right)} F=\sum \operatorname{sgn}(\boldsymbol{x}) F(\boldsymbol{x}) \geqslant 0
$$
其中共有 $2^{n}$ 个加项, $\boldsymbol{x}=\left(x_{1}, \cdots, x_{n}\right)$, 有 $x_{j}=a_{j}$ 或 $b_{j}, j=1, \cdots, n$, 并且当 $\sharp\left\{j \mid x_{j}=a_{j}\right\}$ 为偶数时, $\operatorname{sgn}(\boldsymbol{x})$ 为 $+$ 号, 当 $\sharp\left\{j \mid x_{j}=a_{j}\right\}$ 为奇数时, $\operatorname{sgn}(\boldsymbol{x})$ 为 $-$ 号, 其中 $\sharp\{\cdot\}$ 表示集合 $\{\cdot\}$ 中的元素个数.
为帮助读者了解式 (4.1.3), 给出 $n=2$ 和 3 时 $\Delta_{\left(a_{1}, \cdots, a_{n}\right)}^{\left(b_{1}, \cdots, b_{n}\right)} F$ 的具体形式:
$$
\begin{aligned}
\Delta_{\left(a_{1}, a_{2}\right)}^{\left(b_{1}, b_{2}\right)} F=& F\left(b_{1}, b_{2}\right)-F\left(a_{1}, b_{2}\right)-F\left(b_{1}, a_{2}\right)+F\left(a_{1}, a_{2}\right) \\
\Delta_{\left(a_{1}, a_{2}, a_{3}\right)}^{\left(b_{1}, b_{2}, b_{3}\right)} F=& F\left(b_{1}, b_{2}, b_{3}\right)-F\left(a_{1}, b_{2}, b_{3}\right)-F\left(b_{1}, a_{2}, b_{3}\right)-F\left(b_{1}, b_{2}, a_{3}\right) \\
&+F\left(a_{1}, a_{2}, b_{3}\right)+F\left(a_{1}, b_{2}, a_{3}\right)+F\left(b_{1}, a_{2}, a_{3}\right)-F\left(a_{1}, a_{2}, a_{3}\right)
\end{aligned}
$$
性质 $4^{\circ}$ 成立的原因是
$$
\Delta_{\left(a_{1}, \cdots, a_{n}\right)}^{\left(b_{1}, \cdots, b_{n}\right)} F=\mathbf{P}\left(a_{1}<X_{1} \leqslant b_{1}, \cdots, a_{n}<X_{n} \leqslant b_{n}\right) \geqslant 0 .
$$

# 边缘分布(marginal distribution)

可以由 $n$ 维随机向量 $\left(X_{1}, \cdots, X_{n}\right)$ 的联合分布 $F\left(x_{1}, \cdots, x_{n}\right)$ 方便地推出它 的任何一个 $k$ 维边缘分布. 以 $\left(X_{1}, \cdots, X_{k}\right)$ 为例:
$F_{1, \cdots, k}\left(x_{1}, \cdots, x_{k}\right)=\mathbf{P}\left(X_{1} \leqslant x_{1}, \cdots, X_{k} \leqslant x_{k}\right)=\mathbf{P}\left(\bigcap_{j=1}^{k}\left(X_{j} \leqslant x_{j}\right)\right)$
$=\mathbf{P}\left(\bigcap_{j=1}^{k}\left(X_{j} \leqslant x_{j}\right) \bigcap_{j=k+1}^{n}\left(X_{j}<\infty\right)\right)$
$=F\left(x_{1}, \cdots, x_{k}, \infty, \cdots, \infty\right)$
这一事实告诉我们: 边缘分布可以由联合分布唯一决定.

# 离散的情况
 Let $X$ and $Y$ be discrete random variables taking on values $x_{1}, x_{2}, \ldots$, and $y_{1}, y_{2}, \ldots$, respectively. The joint probability mass function of $(X, Y)$ is $p\left(x_{i}, y_{j}\right)=P\left\{X=x_{i}, Y=y_{j}\right\}$
The marginal pmf can be computed as
$$
p_{X}\left(x_{i}\right)=\sum_{j} p\left(x_{i}, y_{j}\right), p_{Y}\left(y_{j}\right)=\sum_{i} p\left(x_{i}, y_{j}\right)
$$
# 连续的情况
random variables $X$ and $Y$ are said to be jointly continuous if there exists a function $f(x, y)$ defined for all real $x$ and $y$, having the property that for every set $C \subset R^{2} \quad(C$ is a set in the two-dimensional plane)
$$
P\{(X, Y) \in C\}=\iint_{C} f(x, y) d x d y
$$
$f(x, y)$ is called joint density function of $X$ and $Y$.
The marginal pdf for $\boldsymbol{X}$ is defined as: $f_{X}(x)=\int_{-\infty}^{\infty} f(x, y) d y$

# Joint Independent Random Variables
Definition: $X$ and $Y$ are said to be independent if for any two sets of real number $A$ and $B$,
$$
P\{X \in A, Y \in B\}=P\{X \in A\} P\{Y \in B\}
$$
It can be shown that $\left(^{*}\right)$ will follow if and only if for all $a$ and $b \quad F(a, b)=F_{X}(a) F_{Y}(b)$
When $X$ and $Y$ are discrete, it is equivalent to (this you can prove) $p(x, y)=p_{X}(x) p_{Y}(y)$ for all $x, y$
In continuous case, it is equivalent to (this you can prove too) $\quad f(x, y)=f_{X}(x) f_{Y}(y)$ for all $x, y$


## general
General Definition of Independence: $X_{1}, X_{2}, \ldots, X_{n}$ are
said to be independent if, for all sets $A_{1}, A_{2}, \ldots, A_{n}$,
$$
P\left\{X_{1} \in A_{1}, X_{2} \in A_{2}, \ldots, X_{n} \in A_{n}\right\}=\prod_{i=1}^{n} P\left\{X_{i} \in A_{i}\right\}
$$

# conditional distribution
Definition: If $X$ and $Y$ have a joint probability density function $f(x, y)$, then the conditional pdf of $X_{\text {, given }}$ that $Y=y$ is defined for all values of $y$ such that $f_{Y}(y)>0$ by $$f_{X \mid Y}(x \mid y)=\frac{f(x, y)}{f_{Y}(y)}<p(Y=y) $$

# joint 二项分布



If $X_{1}, X_{2}, \ldots, X_{n}$ are independent random variables that are normally distributed with parameters $\mu_{i}, \sigma_{i}^{2}, i=1,2, \ldots, n$, then $\sum_{i=1}^{n} X_{i}$ is normally distributed with parameters $\sum_{i=1}^{n} \mu_{i}$ and $\sum_{i=1}^{n} \sigma_{i}^{2}$
(Other important results) If $X$ and $Y$ are independent Poisson random variables with respective parameters $\lambda_{1}$ and $\lambda_{2}$, then $X+Y$ is a Poisson random variable with parameters $\lambda_{1}+\lambda_{2}$
If $X$ and $Y$ are independent binomial random variables with respective parameters $(n, p)$ and $(m, p)$, then $\mathbf{X}+\mathbf{Y}$ is a binomial random variable with parameters $(n+m, p)$

# joint normal distribution

Definition: The joint density for a bivariate normal distribution is
$$
\begin{aligned}
f(x, y)=& \frac{1}{2 \pi \sigma_{x} \sigma_{y} \sqrt{1-\rho^{2}}} \exp \left\{-\frac{1}{2\left(1-\rho^{2}\right)}\left[\left(\frac{x-\mu_{x}}{\sigma_{x}}\right)^{2}\right.\right.\\
&\left.\left.+\left(\frac{y-\mu_{y}}{\sigma_{y}}\right)^{2}-2 \rho \frac{\left(x-\mu_{x}\right)\left(y-\mu_{y}\right)}{\sigma_{x} \sigma_{y}}\right]\right\}
\end{aligned}
$$
Remarks on bivariate normal random variables $(X, Y)$ :
(a) Marginally, $X \sim N\left(\mu_{x}, \sigma_{x}^{2}\right), Y \sim N\left(\mu_{y}, \sigma_{y}^{2}\right)$
(b) Conditionally, $X \mid Y=y \sim N\left(\mu_{x}+\rho \frac{\sigma_{x}}{\sigma_{y}}\left(y-\mu_{y}\right), \sigma_{x}^{2}\left(1-\rho^{2}\right)\right)$
(c) $\operatorname{Cov}(X, Y)=\rho \sigma_{x} \sigma_{y}$
(d) Linear combinations of $X$ and $Y$ are normal random variables, even though $X$ and $Y$ are not independent when $\rho \neq 0$
(e) Two normal random variables are independent iff they are uncorrelated.