# Jointly distributed 
(Joint) cumulative distribution function (cdf) of $X$ and $Y$ is defined as the bivariate function
$$
F(a, b)=P\{X \leq a, Y \leq b\},-\infty<a, b<\infty
$$
Marginal distributions of $X$ and $Y$ are given by
$$
\begin{aligned}
F_{X}(a) &=P\{X \leq a\}=P\{X \leq a, Y \leq \infty\} \\
&=\lim _{b \rightarrow \infty} P\{X \leq a, Y \leq b\}=F(a, \infty)
\end{aligned}
$$
Similarly, $F_{Y}(b)=F(\infty, b)$
$$\begin{aligned}
&P\{X \leq a, \text { or } Y \leq b\}=F_{X}(a)+F_{Y}(b)-F(a, b) \\
&P\left\{a_{1}<X \leq a_{2}, b_{1}<Y \leq b_{2}\right\}=F\left(a_{2}, b_{2}\right)+F\left(a_{1}, b_{1}\right)-F\left(a_{1}, b_{2}\right)-F\left(a_{2}, b_{1}\right)
\end{aligned}$$
![[Pasted image 20220319103834.png]]
$4^{\circ} F\left(x_{1}, \cdots, x_{n}\right)$ 具有下述意义上的增量非负性: 对任何 $a_{j} \leqslant b_{j}, j=1, \cdots, n$, 都有
$$
\Delta_{\left(a_{1}, \cdots, a_{n}\right)}^{\left(b_{1}, \cdots, b_{n}\right)} F=\sum \operatorname{sgn}(\boldsymbol{x}) F(\boldsymbol{x}) \geqslant 0
$$
其中共有 $2^{n}$ 个加项, $\boldsymbol{x}=\left(x_{1}, \cdots, x_{n}\right)$, 有 $x_{j}=a_{j}$ 或 $b_{j}, j=1, \cdots, n$, 并且当 $\sharp\left\{j \mid x_{j}=a_{j}\right\}$ 为偶数时, $\operatorname{sgn}(\boldsymbol{x})$ 为 $+$ 号, 当 $\sharp\left\{j \mid x_{j}=a_{j}\right\}$ 为奇数时, $\operatorname{sgn}(\boldsymbol{x})$ 为 $-$ 号, 其中 $\sharp\{\cdot\}$ 表示集合 $\{\cdot\}$ 中的元素个数.
# Joint probability mass functions
 Let $X$ and $Y$ be discrete random variables taking on values $x_{1}, x_{2}, \ldots$, and $y_{1}, y_{2}, \ldots$, respectively. The joint probability mass function of $(X, Y)$ is $p\left(x_{i}, y_{j}\right)=P\left\{X=x_{i}, Y=y_{j}\right\}$
The marginal pmf can be computed as
$$
p_{X}\left(x_{i}\right)=\sum_{j} p\left(x_{i}, y_{j}\right), p_{Y}\left(y_{j}\right)=\sum_{i} p\left(x_{i}, y_{j}\right)
$$
# Joint probability density function
random variables $X$ and $Y$ are said to be jointly continuous if there exists a function $f(x, y)$ defined for all real $x$ and $y$, having the property that for every set $C \subset R^{2} \quad(C$ is a set in the two-dimensional plane)
$$
P\{(X, Y) \in C\}=\iint_{C} f(x, y) d x d y
$$
$f(x, y)$ is called joint density function of $X$ and $Y$.
The marginal pdf for $\boldsymbol{X}$ is defined as: $f_{X}(x)=\int_{-\infty}^{\infty} f(x, y) d y$
# Independent Random Variables
Definition: $X$ and $Y$ are said to be independent if for any two sets of real number $A$ and $B$,
$$
P\{X \in A, Y \in B\}=P\{X \in A\} P\{Y \in B\}
$$
It can be shown that $\left(^{*}\right)$ will follow if and only if for all $a$ and $b \quad F(a, b)=F_{X}(a) F_{Y}(b)$
When $X$ and $Y$ are discrete, it is equivalent to (this you can prove) $p(x, y)=p_{X}(x) p_{Y}(y)$ for all $x, y$
In continuous case, it is equivalent to (this you can prove too) $\quad f(x, y)=f_{X}(x) f_{Y}(y)$ for all $x, y$
Example:(try to memorize the result) Suppose that thenumber of people that enter a post office on a given day is a Poisson random variable with parameter$\lambda$ .Show that if each person that enters the post office is a male with probability p and a female with probability 1-p, then the number of males and females entering the post office are independent Poisson random variables with respective parameters $\lambda p$ and$\lambda (1-p)$


## general
General Definition of Independence: $X_{1}, X_{2}, \ldots, X_{n}$ are
said to be independent if, for all sets $A_{1}, A_{2}, \ldots, A_{n}$,
$$
P\left\{X_{1} \in A_{1}, X_{2} \in A_{2}, \ldots, X_{n} \in A_{n}\right\}=\prod_{i=1}^{n} P\left\{X_{i} \in A_{i}\right\}
$$
# Sums of Independent Random Variables
It is often important to calculate the distribution of $X+Y$ given the distribution of $X$ and $Y$ when $X$ and $Y$ are independent.
$\text { If } \boldsymbol{X} \text { and } \boldsymbol{Y} \text { are independent, } f_{X \mid Y}(x \mid y)=f_{X}(x)$
$$
\begin{aligned}
F_{X+Y}(a) &=P\{X+Y \leq a\} \\
&=\iint_{x+y \leq a} f_{X}(x) f_{Y}(y) d x d y \\
&=\int_{-\infty}^{\infty} \int_{-\infty}^{a-y} f_{X}(x) f_{Y}(y) d x d y \\
&=\int_{-\infty}^{\infty} f_{Y}(y) \int_{-\infty}^{a-y} f_{X}(x) d x d y \\
&=\int_{-\infty}^{\infty} F_{X}(a-y) f_{Y}(y) d y
\end{aligned}
$$
Differentiating on both sides, we get
$$
\begin{aligned}
f_{X+Y}(a) &=\frac{d}{d a} \int_{-\infty}^{\infty} F_{X}(a-y) f_{Y}(y) d y \\
&=\int_{-\infty}^{\infty} \frac{d}{d a} F_{X}(a-y) f_{Y}(y) d y \\
&=\int_{-\infty}^{\infty} f_{X}(a-y) f_{Y}(y) d y
\end{aligned}
$$
# properties
If $X_{1}, X_{2}, \ldots, X_{n}$ are independent random variables that are normally distributed with parameters $\mu_{i}, \sigma_{i}^{2}, i=1,2, \ldots, n$, then $\sum_{i=1}^{n} X_{i}$ is normally distributed with parameters $\sum_{i=1}^{n} \mu_{i}$ and $\sum_{i=1}^{n} \sigma_{i}^{2}$
(Other important results) If $X$ and $Y$ are independent Poisson random variables with respective parameters $\lambda_{1}$ and $\lambda_{2}$, then $X+Y$ is a Poisson random variable with parameters $\lambda_{1}+\lambda_{2}$
If $X$ and $Y$ are independent binomial random variables with respective parameters $(n, p)$ and $(m, p)$, then $\mathbf{X}+\mathbf{Y}$ is a binomial random variable with parameters $(n+m, p)$
# conditional distribution
Definition: If $X$ and $Y$ have a joint probability density function $f(x, y)$, then the conditional pdf of $X_{\text {, given }}$ that $Y=y$ is defined for all values of $y$ such that $f_{Y}(y)>0$ by $$f_{X \mid Y}(x \mid y)=\frac{f(x, y)}{f_{Y}(y)}<p(Y=y) $$
# 转化变量
1. $y_{1}=g_{1}\left(x_{1}, x_{2}\right)$ and $y_{2}=g_{2}\left(x_{1}, x_{2}\right)$ can be uniquely solved for $x_{1}$ and $x_{2}$ to get, say, $x_{1}=h_{1}\left(y_{1}, y_{2}\right), x_{2}=h_{2}\left(y_{1}, y_{2}\right)$
2. The functions $g_{1}$ and $g_{2}$ have continuous partial derivatives and the determinant of the following determinant
$$
J\left(x_{1}, x_{2}\right)=\left|\begin{array}{ll}
\frac{\partial g_{1}}{\partial x_{1}} & \frac{\partial g_{1}}{\partial x_{2}} \\
\frac{\partial g_{2}}{\partial x_{1}} & \frac{\partial g_{2}}{\partial x_{2}}
\end{array}\right| \neq 0
$$
Then $f_{Y_{1}, Y_{2}}\left(y_{1}, y_{2}\right)=f_{X_{1}, X_{2}}\left(x_{1}, x_{2}\right)\left|J\left(x_{1}, x_{2}\right)\right|^{-1}$ where
$$
x_{1}=h_{1}\left(y_{1}, y_{2}\right), x_{2}=h_{2}\left(y_{1}, y_{2}\right)
$$
# expectation
Proposition. $\quad E[g(X, Y)]=\sum_{x} \sum_{y} g(x, y) p(x, y)$
$E[g(X, Y)]=\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} g(x, y) f(x, y) d x d y$
An important implication is
$$
\begin{aligned}
E[X+Y] &=\int_{-\infty}^{\infty} \int_{-\infty}^{\infty}(x+y) f(x, y) d x d y \\
&=\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} x f(x, y) d x d y+\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} y f(x, y) d x d y \\
&=\int_{-\infty}^{\infty} x f_{X}(x) d x+\int_{-\infty}^{\infty} y f_{Y}(y) d y \\
&=E[X]+E[Y]
\end{aligned}
$$
# Covariance
The covariance between two random variables is a measure of how they are related.
Definition: The covariance between $X$ and $Y$, denoted by $\operatorname{Cov}(X, Y)$, is defined by $\operatorname{Cov}(X, Y)=E[(X-E[X])(Y-E[Y])]$.
By expanding the right hand side of the definition of the covariance, we see that
$$
\begin{aligned}
& \operatorname{Cov}(X, Y) \\
=& E[(X-E[X])(Y-E[Y])]=E\{X Y-E[X] Y-X E[Y]+E[X] E[Y]\} \\
=& E[X Y]-E[X] E[Y]-E[X] E[Y]+E[X] E[Y]=E[X Y]-E[X] E[Y]
\end{aligned}
$$
If $X$ and $Y$ are independent, then
$$
\begin{aligned}
E[X Y] &=\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} x y f(x, y) d x d y \\
&=\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} x y f_{X}(x) f_{Y}(y) d x d y \\
&=E[X] E[Y]
\end{aligned}
$$
Definition: If $\operatorname{Cov}(X, Y)=0$, we say $X$ and $Y$ are uncorrelated. If $\operatorname{Cov}(X, Y)>0$, we say $X$ and $Y$ are positively correlated. If $\operatorname{Cov}(X, Y)<0$, we say $X$ and $Y$ are negatively correlated.

So the previous calculation tells us that independence implies uncorrelatedness.
We have
Proposition: If $X$ and $Y$ are independent, then for any functions of $g$ and $h, g(X)$ and $h(Y)$ are independent.
(i) $\operatorname{Cov}(X, Y)=\operatorname{Cov}(Y, X)$
(ii) $\operatorname{Cov}(X, X)=\operatorname{Var}(X)$
(iii) $\operatorname{Cov}(a X, b Y)=a b \operatorname{Cov}(X, Y)$
(iv) $\operatorname{Cov}\left(\sum_{i=1}^{n} X_{i}, \sum_{j=1}^{m} Y_{j}\right)=\sum_{i=1}^{n} \sum_{j=1}^{m} \operatorname{Cov}\left(X_{i}, Y_{j}\right)$
(v) $\operatorname{Var}\left(\sum_{i=1}^{n} X_{i}\right)=\sum_{i=1}^{n} \operatorname{Var}\left(X_{i}\right)+2 \sum_{i<j} \operatorname{Cov}\left(X_{i}, X_{j}\right)$
(vi) if $X_{1}, X_{2}, \ldots, X_{n}$ are pairwise independent, $\operatorname{Var}\left(\sum_{i=1}^{n} X_{i}\right)=\sum_{i=1}^{n} \operatorname{Var}\left(X_{i}\right)$
Thus two events are independent if and only if the corresponding indicator variables are uncorrelated. In other words, for indicator variables, independence and uncorrelatedness are equivalent.
## Correlation
$\rho(X, Y)=\frac{\operatorname{Cov}(X, Y)}{\sqrt{\operatorname{Var}(X) \operatorname{Var}(Y)}}$
The correlation is always between $-1$ and 1. If $X$ and $Y$ are independent, then $\rho(X, Y)=0$.but the converse is not true. Generally, the correlation (as well as covariance) is a measure of the degree of linear dependence between $X$ and $Y$.
Note that for $a>0, b>0$, $\rho(a X, b Y)=\frac{\operatorname{Cov}(a X, b Y)}{\sqrt{\operatorname{Var}(a X) \operatorname{Var}(b Y)}}=\frac{\operatorname{abCov}(X, Y)}{\sqrt{a^{2} b^{2} \operatorname{Var}(X) \operatorname{Var}(Y)}}=\rho(X, Y)$
Bivariate normal distribution
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
# random
The conditional expectation of $X$, given that $Y=y$, is
$$
E[X \mid Y=y]=\int_{-\infty}^{\infty} x f_{X \mid Y}(x \mid y) d x
$$
$\operatorname{Var}(X \mid Y=y)=E\left[(X-E[X \mid Y=y])^{2} \mid Y=y\right]$