我们这里实际上讨论的参数是$\mu$其他的太复杂了，我懒得写（但是后续肯定会补的）

另外这边还要分两个情况，样本比较小的情况下，我们对总体的分布是有要求的（但为了简单起见，我们认为总体是正态的，当然其他分布也可以，但注意的是二项分布在总体较大的时候也算作正态分布）

但是对于大样本，central limit theorem会帮助你

引入区间估计的原因实际上就在上一章的末尾，对于我们估计的参数是存在standard error，我们想要刻画这种error，下面引入confidence level

# confidence level

定义 4.1 如果不论参数 $\theta$ 在参数空间 $\Theta$ 中取什么值, “区间 $\left[\theta_{1}(X)\right.$, $\left.\theta_{2}(X)\right]$ 包含 $\theta$ '这个事件的概率总不小于指定的常数 $1-\alpha(0 \leqslant \alpha \leqslant 1, \alpha$ 通常 很小), 即
$$
P_{\theta}\left(\theta_{1}(X) \leqslant \theta \leqslant \theta_{2}(X)\right) \geqslant 1-\alpha \quad(\text { 切 } \theta \in \Theta),
$$
则称 $\left[\theta_{1}(X), \theta_{2}(X)\right]$ 有置信水平 $1-\alpha$. 也常称 $\left[\theta_{1}(X), \theta_{2}(X)\right]$ 是 $\theta$ 的置信水 平 $1-\alpha$ 的区间估计或置信区间.

但同时我们也要注意到，这个区间不能太大（涉及到精度问题），这是一个经典的矛盾问题（在后续的很多章节中，我们都可以看到统计学里面的矛盾和他的处理办法）

通常我们都是在保证可信度的情况下进行尽可能的缩小精度

精度我们用marginal error来衡量

$E=z_{\alpha / 2} \frac{\sigma}{\sqrt{n}}$

（至于为什么定义为1-alpha我不太清楚，后面再说）

# 正态分布的估计

## 已知$\sigma$

先找一个 $\mu$ 的良好的点估计. 在此可选择样本均值 $\bar{X}$. 由总 体为正态易知
$$
\sqrt{n}(\bar{X}-\mu) / \sigma-N(0,1)
$$
以 $\Phi$ 记 $N(0,1)$ 的分布函数. 对 $0<\beta<1$ (一般是 $\beta$ 很小), 用方程
$$
\Phi\left(u_{\beta}\right)=1-\beta
$$
定义记号 $u_{\beta} \cdot u_{\beta}$ 称为分布 $N(0,1)$ 的 “上 $\beta$ 分位点”. 其意义是:

$N(0,1)$ 分布中大于 $u_{\beta}$ 的那部分的概率, 就是 $\beta$. 图 $4.2$ 中画出的 是 $N(0,1)$ 的密度函数 $\varphi(x)=(\sqrt{2 \pi})^{-1} \mathrm{e}^{-x^{2} / 2}$ 的图形, 涂黑部分 标出的面积为 $\beta$.

![image-20220406115804002](C:\Users\PRAGM\Documents\GitHub\math-wiki\概率统计\image-20220406115804002.png)

$\begin{aligned}
P(&\left.-u_{\alpha / 2} \leqslant \sqrt{n}(\bar{X}-\mu) / \sigma \leqslant u_{\alpha / 2}\right)=\Phi\left(u_{\alpha / 2}\right)-\Phi\left(-u_{\alpha / 2}\right) \\
&=(1-\alpha / 2)-\alpha / 2=1-\alpha
\end{aligned}$

实际上是通过求反函数来实现的
$$
\left(u_{\beta}\right)=\Phi^{-1}(1-\beta)
$$
但是我们查表的时候不需要经过反函数这一步，就可以直接得出数据（记住这里的u是一个区间的边界值）

# 未知$\sigma$

在这种情况下, $\mu$ 的良好的点估计仍为 $\bar{X}$, 由于 $\sigma^{2}$ 末知, 例 $4.2 .1$ 中的随机变 量 $U=\sqrt{n}(\bar{X}-\mu) / \sigma$ 在此不能作为枢轴变量, 将其中的 $\sigma$ 用 $S$ ( $S^{2}$ 是样本方差)

$$
T=\frac{\sqrt{n}(\bar{X}-\mu)}{S} .
$$
由推论 $2.4 .2$ （未来补上双链）可知 $T \sim t_{n-1}$. 可见 $T$ 的表达式与 $\mu$ 有关, 而其分布与 $\mu$ 无关, 故取 $T$ 为枢轴变量. 由于 $t$ 分布关于原点对称, 令
$$
P(|T| \leqslant c)=P\left(-c \leqslant \frac{\sqrt{n}(\bar{X}-\mu)}{S} \leqslant c\right)=1-\alpha,
$$
则 $c=t_{n-1}(\alpha / 2)$. 将括号中的不等式经过等价变形得 $\mu$ 的置信系数为 $1-\alpha$ 的置 信区间为
$$
\left[\bar{X}-\frac{S}{\sqrt{n}} t_{n-1}(\alpha / 2), \bar{X}+\frac{S}{\sqrt{n}} t_{n-1}(\alpha / 2)\right]
$$
remark：这边我也标记一下，对于t分布的denisty function 有一个$t_n(x)$但是这边还有一个$t_n(\alpha /2)$这个是$\alpha$分数。但离谱的数，前者在函数上，后者在坐标系上，怎么定义的方式一样呢