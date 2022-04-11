这一章挺绕的，麻掉了

上个章节，我们讲了那个用样本估计总体，涉及到了两个——一个是点估计，一个是区间估计。这两个inference，实际上意味上可以理解为是一种对总体的阐释,但是呢我们想利用这些数据来帮助我们做决策，是比较困难的，例如你有99%的confidence level认为总体期望是[9,11]，对于一个要求大约平均数在9.5的买家而言，他是否会选择购买你这个货物呢，所以我们引入了hypothesis test

要注意的是，这边我可能会引入很多的英文单词，这一点可能我也会在开头部分进行。统计学严格来说还是一门比较新的知识，包括他的奠基，他的引用，甚至理论都是比较新的，在野蛮生长的时代，有许多词说实话都定义的比较随便，所以导致很多概念非常像，然后内地的很多教材，为了显示这些名词有多么的高大上，会用一些奇奇怪怪的词来进行定义，反而让读者很难理解主要的核心内容。

# 引入

你作为一个企业，你要买一批可以写40000字左右的笔用于公司使用，然后你就去买的商铺里面跳了n款笔拿出来测试，发现样本的平均字数是39000，那么请问你是否决定购买（假设笔的长度是正态分布）

在这里，你希望总体的平均数是大于等于40000，或者大于40000，他被称为" null hypothess",在中文里面被称为零假设，或者原假设，但是假设的正确与否是需要通过样本去判断的，实际上可以理解为你预期的希望达到的量。

与null hypothess 相对的是alternative hypothess，我个人的理解是，如果说你的null hypothess是错（准确来说叫拒绝）的，那么你可以去验证alternative是否是对的

为了检验hypothsis是否正确，我们需要一个 test statistics，也就是一个由样本算出来的测量量，看测量量是否满足一定的要求，如果满足我们就accpet，不满足我们就reject。要注意的是样本测出来的是估计值，所以会出现两个error，下面是一张很经典的图

![image-20220407152345165](C:\Users\PRAGM\Documents\GitHub\math-wiki\概率统计\image-20220407152345165.png)

我们先看左边，accept H的意思，并不是说H是对的，而是说我们根据估计的量进行的决定。就像上面的例子提到的，或许实际上总体平均能写的字数是41000，但是你手气不好，没抽到质量比较好的那一批，因此你谨慎起见，拒绝(reject)这批水笔。

也就是我们可以看到accept与否和null hypothesis正确与否无关

这时候就出现两个错误

错误一：总体符合你的预期，但是你reject了（股票上涨了，但是你没买）

错误二：总体不符合你的语气，但是你accept（股票跌了，但是你买了）

二者是矛盾的（又提到了矛盾关系），但通常来说我们会在保证$\alpha$不太大的情况下（也就是手上有一定量的好股票）的同时尽可能的降低$\beta$（也就是尽可能不买垃圾股票）

# decision rule

在decision rule中，我们并未开始进行样本采集，我们先把否定域（如果样本在这个区间内，就reject）定出来，这样的话一得到采集的样本就可以立刻根据这个域来进行decision

我们要让$\alpha$不太大，这时候我们自己设定一个数即可，这时候需要

P(we reject H|H is true)=$\alpha$ 

如果你想要一批书写长度大概在$\mu$的笔，那么你就会希望H：$\mu=\mu_0$($\mu 0$是你想要hypothesis中的数,$\mu$是总体期望)

这时候我们先定义否定域D={($X_1,X_2,X_3\dots X_n$),$|\bar{X}-\mu_0|>c\}$，当样本测量值距离$\mu_0$太远了（这里的远就是用c来定义，但是目前他未知），我们就否定他

P(we reject H|H is true)=$P(D|H$ is true)，也就是当H=$\mu=\mu_0$成立时的P的大小（不过通常来说，否定域应该是直接对应标准正态函数上面的一个范围，然后x进行标准化处理）

如果$H=\mu=\mu_0$是对的，此时D={($X_1,X_2,X_3\dots X_n$),$|\bar{X}-\mu_0|>c\}$

如果$\sigma$已知（未知自己去推吧，我写的人快没了，累死了）

$P(D|H$ is true)=$P(|\bar{X}-\mu_0|>c\}|\mu=\mu_0)$我们知道$\bar{X}$满足N($\mu,\frac{\sigma^2}{n}$)，所以

$P(|\frac{\sqrt{n}(\bar{X}-\mu_0)}{\sigma}|>\frac{c\sqrt{n}}{\sigma})=\alpha$

那么$\frac{c\sqrt{n}}{\sigma}=u_{\alpha/2}$（这里用双链，以后做）

从而我们可以算出c来，进而建立否定域，在否定域内的，我们就reject

但有的时候我们能够接受$\mu \geq \mu_0$的情况（比如我们希望笔写的字越长越好）

这时的否定域是D={($X_1,X_2,X_3\dots X_n$),$\bar{X}-\mu_0<-c\}$（之所以不是$\bar{X}-\mu_0<0$，是因为我们的$\bar{X}$是一个估计值，不能完完全全代表数据，需要有一点误差空间)

$P(\bar{X}-\mu_0<-c|\mu \leq\mu_0)=$$P(\frac{\sqrt{n}(\bar{X}-\mu)}{\sigma}<-\frac{(c+\mu_0-\mu)\sqrt{n}}{\sigma})=P(Z<-\frac{(c+\mu_0-\mu)\sqrt{n}}{\sigma})\leq P(Z<-\frac{c\sqrt{n}}{\sigma})= \alpha$

# p-value

p-value实际上不难，就是在知道测量值后，算$P(X>\bar{X}|\mu=\mu_0)$的值，如果大于$\alpha$，我们reject，反之我们accept

实际上decision rule就是解方程，看哪个值是边界，而p-value就是直接一步到位计算

## type 2 error

在$\alpha$不大之后，我们就应该让$\beta$尽可能小

$H_{0}: \theta=\theta_{0}, H_{a}: \theta \in \Omega_{a},H_a$表示alternative hypothesis

type II error (is a function):
$\beta\left(\theta_{a}\right)=P\left(\right.$ accepting $H_{0}$ when $\left.\theta=\theta_{a} \in \Omega_{a}\right)$
Power (Power Function):
power $\left(\theta_{a}\right)=P\left(\right.$ rejecting $H_{0}$ when $\left.\theta=\theta_{a} \in \Omega_{a}\right)=$ $1-\beta\left(\theta_{a}\right)$,$\theta_{a}$在这里是自变量，有的时候其他题里面用的是$\mu$

在type 1 error中，$\alpha$是一个边界的值，而在

![image-20220409170629669](C:\Users\PRAGM\Documents\GitHub\math-wiki\概率统计\image-20220409170629669.png)