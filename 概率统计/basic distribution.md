这些基础的分布在后续的章节中会被用到，现在我们只是进行一个理论的奠基，以方便后续的讲解

# chi_squared distribution

The $\chi^{2}(n)$, or $\chi_{n}^{2}$ distribution is just the gamma distribution, with $\alpha=n / 2$ and $\beta=1 / 2$. The integer $n$ is the parameter of the distribution and sometimes called the degree of freedom. If $X \sim \chi^{2}(n)$, then $E[X]=\overline{n, \operatorname{Var}(X)=2 n .}$
Characterization/Definition: if $Z_{i} \stackrel{i . i . d}{\sim} N(0,1)$, then $\sum_{i=1}^{n} Z_{i}^{2} \sim \chi^{2}(n)$.

Property: if $X$ and $Y$ are independent with $\chi_{n}^{2}$ and $\chi_{m}^{2}$ distributions, then $X+Y \sim \chi_{n+m}^{2}$ (this can be proved easily with the above characterization)

# t distribution

Characterization:
If $Z \sim N(0,1), X \sim \chi_{n}^{2}$, and $X$ and $Z$ are independent, then $\sqrt{n} Z / \sqrt{X} \sim \operatorname{t_n}($ or $t(n))$. $n$ is the parameter of the $t$ distribution and called the degrees of freedom like for $\chi^{2}$ distribution.

# density function

Density:
$$
f(x)=\frac{\Gamma\left(\frac{n+1}{2}\right)}{\Gamma\left(\frac{n}{2}\right) \sqrt{n \pi}}\left(1+x^{2} / n\right)^{-(n+1) / 2}
$$
$E[X]=0, \operatorname{Var}(X)=\frac{n}{n-2} \text { if } n>2$