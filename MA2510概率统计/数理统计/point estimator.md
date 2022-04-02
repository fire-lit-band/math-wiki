# Method of moments estimator (MME)
General Description
Let $X_{1}, \ldots, X_{n}$ be iid sample from $f\left(x \mid \theta_{1}, \ldots, \theta_{k}\right)$.
Define
$$
\begin{array}{rlr}
m_{1}=\frac{1}{n} \sum_{i=1}^{n} X_{i}, & \mu_{1}=E X \\
m_{2}=\frac{1}{n} \sum_{i=1}^{n} X_{i}^{2}, & \mu_{2}=E X^{2} \\
m_{k}=\frac{1}{n} \sum_{i=1}^{n} X_{i}^{k}, & \mu_{k}=E X^{k}
\end{array}
$$
$\mu_{j}$ will typically be a function of $\theta_{1}, \ldots, \theta_{k}$. The method of moments estimator is obtained by solving
$$
\begin{aligned}
m_{1} &=\mu_{1}\left(\theta_{1}, \ldots, \theta_{k}\right) \\
m_{2} &=\mu_{2}\left(\theta_{1}, \ldots, \theta_{k}\right) \\
& \vdots \\
m_{k} &=\mu_{k}\left(\theta_{1}, \ldots, \theta_{k}\right)
\end{aligned}
$$
# Maximum Likelihood estimator (MLE)
Definition of the likelihood function For a sample $X=\left(X_{1}, \ldots, X_{n}\right)$ with joint pdf or pmf $f(X \mid \theta)$, the likelihood function is just the pdf or pmf, but think of it as a function of $\theta$ :
$$
L(\theta \mid X)=f(X \mid \theta)
$$
In this course, we have always that observations are i.i.d. Therefore, the resulting density for the samples is
$$
L(\theta \mid X)=\prod_{i=1}^{n} f\left(X_{i} \mid \theta\right)
$$
The maximum likelihood estimator (MLE) is just the maximizer $\hat{\theta}(X)$ of the likelihood function. Often we maximize $l(\theta \mid X)=\log L(\theta \mid X)$ instead because it is usually easier.
Invariance Property of MLE
If $\hat{\theta}$ is the MLE of $\theta$, then for any function $h(\theta)$, $h(\hat{\theta})$ is the MLE of $h(\theta) .$
$$
\begin{aligned}
L &=\prod_{i=1}^{n}\left[\left(\sqrt{2 \pi \sigma^{2}}\right)^{-1} \exp \left(-\frac{1}{2 \sigma^{2}}\left(X_{i}-\mu\right)^{2}\right)\right] \\
\log L &=-\frac{n}{2} \log (2 \pi)-\frac{n}{2} \log \left(\sigma^{2}\right)-\frac{1}{2 \sigma^{2}} \sum_{i=1}^{n}\left(X_{i}-\mu\right)^{2}
\end{aligned}
$$
求方䅡组 $\left(2.5\right.$ ) (把 $\sigma^{2}$ 作为一个整体看):
$$
\begin{gathered}
\frac{\partial \log L}{\partial \mu}=\frac{1}{\sigma^{2}} \sum_{i=1}^{n}\left(X_{i}-\mu\right)=0 \\
\frac{\partial \log L}{\partial\left(\sigma^{2}\right)}=-\frac{n}{2 \sigma^{2}}+\frac{1}{2 \sigma^{4}} \sum_{i=1}^{n}\left(X_{i}-\mu\right)^{2}=0
\end{gathered}
$$
由第一式得出 $\mu$ 的解为
$$
\mu^{*}=\sum_{i=1}^{n} X_{i} / n=\bar{X}
$$
以此代人第二式的 $\mu$, 得到 $\sigma^{2}$ 的解为
$$
\sigma^{* 2}=\sum_{i=1}^{n}\left(X_{i}-\bar{X}\right)^{2} / n=m_{2}
$$
# unbiased estimator
Definition
An estimator $\hat{\theta}$ is an unbiased estimator for $\theta$ if $E(\hat{\theta})=\theta$ (for all $\theta$ ).
$\widehat{\theta}$ is (weakly) consistent if $\hat{\theta} \rightarrow \theta$ weakly, that is $\lim _{n \rightarrow \infty} P(|\hat{\theta}-\theta|<c)=1 \forall c>0$.
我们实际上可以理解为收敛到一个最佳估计的点

Definition. The mean squared error (MSE) of an estimator $\hat{\theta}$ of $\theta$ is $E\left[(\hat{\theta}-\theta)^{2}\right]$.
One property of MSE. $\operatorname{MSE}(\widehat{\theta})=\operatorname{Var}(\hat{\theta})+$ bias $^{2}(\hat{\theta})$ where the bias of an estimator is $E[\hat{\theta}]-\theta$
我想知道总体的g(theta)（这里的g就是你现在非常想要知道的一个量，可以使平均数，也可以是方差，也可以是平均数/方差，但是这个量是由$\theta$运算出来的）是啥，但是呢我手上只有x_1,x_2,x_3....这些样本，那我怎么用估计出来呢，我们就用$\hat g$（注意的是，这边的$\hat g$和g不是同一个函数，因为他们的定义域就不一样了），然后我用这些样本x_1,x_2扔到$\hat g(x)$里面反应一下，希望他能够生成一个数来估计这个这个g(theta)(这也是前面的矩阵的 Method of moments estimator和maximum likehood的想法)但是呢，样本是可能bias的，这就导致算出来的值可能跟真实值差距比较大，这时候我们希望把所有$\hat g$的可能值都弄出来取个期望，这样的话结果会显得比较“中庸”一些
For a point estimator $\widehat{\Theta}$, the standard error of $\widehat{\Theta}$ is defined as the square root of its variance, i.e.
$$
S E_{\widehat{\Theta}}=\sqrt{\operatorname{Var}(\widehat{\Theta})}
$$