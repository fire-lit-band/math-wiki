
# confidence interval estimation
use a range (or an interval) of numbers to
estimate unknown population parameter
The level of confidence is $100(1-\alpha) \%$. Most common confidence levels are: $90 \% \quad(\alpha=0.10), 95 \% \quad(\alpha=0.05)$, and $99 \% \quad(\alpha=0.01)$. Note that it can never be $100 \%$ confident
![[Pasted image 20220306181754.png]]
- Assumptions
- Population standard deviation is unknown
- Population is normal
- If population is not normal, use large $n$
- The variable $\mathrm{T}=\frac{\bar{x}-\mu}{s / \sqrt{n}}$ follows a distribution called Student's $t$-distribution (or simply called $t$-distribution)
- Developed by Gosset who used "Student" as the pen name in pi the paper
- The probability density function of $t$-distribution is
$$
f(t)=\frac{\Gamma\left(\frac{v+1}{2}\right)}{\sqrt{v \pi} \Gamma\left(\frac{v}{2}\right)}\left(1+\frac{t^{2}}{v}\right)^{-\frac{v+1}{2}}, v>0
$$
where $\Gamma$ is the gamma function and $v$ is the parameter of the function which is often called the degrees of freedom
## degree of freedom
Df is the number of observations that are free to vary in the final
calculation of a statistic
Df equals the total number of observations used in the analysis
minus the number of parameters estimated as intermediate steps
in the estimation of the parameter itself
![[Pasted image 20220306182433.png]]
![[Pasted image 20220306182852.png]]
If the population standard deviation is unknown,
 Use prior information such as the sample standard deviation in earlier similar
studies to guess $\sigma$ value
 If no prior information is available, estimate the range of the data and then
estimate the standard deviation as range/4 (or range/6 )这里是假装的
	If population is normal or near.normal, 95.4% of the observations are within 2$\sigma$ of the mean (99.7% of the observations are within 3$\sigma$ of the mean)
Conduct a small.scale study and estimate the standard deviation from the
resulting data
![[Pasted image 20220306183002.png]]