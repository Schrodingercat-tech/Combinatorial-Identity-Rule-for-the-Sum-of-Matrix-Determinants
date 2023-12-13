# Combinatorial Identity Rule for the Sum of Matrix Determinants

**Author:**

- Sai Ganesh Reddy

**Contact Information:**

- Email: <ganesh.sai432@gmail.com>
- GitHub: [Schrodingercat-tech](https://github.com/Schrodingercat-tech)
- YouTube: [**sAi**](YouTube_Profile_Link)
- Instagram: [self.sai](Instagram_Profile_Link)

---

We know that adding the determinants of matrices $\det(A)$ and $\det(B)$ doesn't equal the determinant of their sum $\det(A+B)$.

$$
\det(A+B) \neq \det(A) + \det(B)
$$

However, there's a captivating pattern: the determinant of the sum $\det(A+B)$ seems to have a connection with the sum of the determinants of $\det(A)$ and $\det(B)$. This intriguing relationship introduces an additional factor denoted as $c(A, B)$ into the equation.

$$
\det(A+B) \equiv \det(A) + \det(B) + c(A,B)
$$

Interestingly, $c(A+B)$ is nothing but combinational arrangements of these two matrices either by column or by row. Let's see what we mean by that with an example.

$$
A = \begin{bmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{bmatrix} \quad ; \quad B = \begin{bmatrix} b_{11} & b_{12} \\ b_{21} & b_{22} \end{bmatrix}
$$

$$
\det(A+B) = \det\begin{bmatrix} a_{11}+b_{11} & a_{12}+b_{12} \\ a_{21}+b_{21} & a_{22}+b_{22} \end{bmatrix}
$$

**Column Combinations**

$$
\begin{align*}
\det\begin{bmatrix} a_{11}+b_{11} & a_{12}+b_{12} \\ a_{21}+b_{21} & a_{22}+b_{22} \end{bmatrix} &\equiv \det\begin{bmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{bmatrix} \\
&+ \det\begin{bmatrix} b_{11} & b_{12} \\ b_{21} & b_{22} \end{bmatrix} \\
&+ \det\begin{bmatrix} a_{11} & b_{12} \\ a_{21} & b_{22} \end{bmatrix} \\
&+ \det\begin{bmatrix} b_{11} & a_{12} \\ b_{21} & a_{22} \end{bmatrix}
\end{align*}
$$

**Row Combinations**

$$
\begin{align*}
\det\begin{bmatrix} a_{11}+b_{11} & a_{12}+b_{12} \\ a_{21}+b_{21} & a_{22}+b_{22} \end{bmatrix} &\equiv \det\begin{bmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{bmatrix} \\
&+ \det\begin{bmatrix} b_{11} & b_{12} \\ b_{21} & b_{22} \end{bmatrix} \\
&+ \det\begin{bmatrix} a_{11} & a_{12} \\ b_{21} & b_{22} \end{bmatrix} \\
&+ \det\begin{bmatrix} b_{11} & b_{12} \\ a_{21} & a_{22} \end{bmatrix}
\end{align*}
$$

$$
\text{LHS} = (a_{11}+b_{11})(a_{22}+b_{22}) - (a_{12}+b_{12})(a_{21}+b_{21})
$$

$$
\text{RHS}_{\text{row comb}} = (a_{11}a_{22} - a_{12}a_{21}) + (b_{11}b_{22} - b_{12}b_{21}) + (a_{11}b_{22} - a_{12}b_{21}) + (b_{11}a_{22} - b_{12}a_{21})
$$

**Re-arranging terms**

$$
\begin{align*}
&= (a_{11}a_{22} + a_{11}b_{22} + b_{11}a_{22} + b_{11}b_{22}) \\
&- (a_{12}a_{21} + a_{12}b_{21} + b_{12}a_{21} + b_{12}b_{21}) \\
&= (a_{11}(a_{22}+b_{22}) + b_{11}(a_{22}+b_{22})) \\
&- (a_{12}(a_{21}+b_{21}) + b_{12}(a_{21}+b_{21})) \\
&= (a_{11}+b_{11})(a_{22}+b_{22}) - (a_{12}+b_{12})(a_{21}+b_{21}) \\
&\text{LHS} \equiv \text{RHS}_{\text{row comb}} \equiv \text{RHS}_{\text{column comb}}
\end{align*}
$$

where $(\lambda_1, \lambda_2, \ldots, \lambda_n)_{1 \times n} \subset \text{all combinations of terms}_{(t^n, n)}$.

From the above, we can see that both LHS and RHS are equal. We can extend this method to an $n \times n$ grid. Note that the index positions of the elements remain the same, but the elements themselves are altered based on their positions in either the column or row arrangements. This extension allows for the computation of determinants for square matrices of any size.

With an increase in the dimension of matrices, the number of elements will also increase. The total number of terms will be equal to:

$$
\text{no of terms} (T) = \sum_{r=n}^{r=0} \binom{n}{r} \quad \text{where} \quad \binom{n}{r} = \frac{n!}{(n-r)!r!}
$$

If we look closely, this is similar to the Binomial Function:

$$
(a + b)^n = \sum_{r=n}^{r=0} \binom{n}{r} a^{n-r} b^r \quad \text{where} \quad a, b = 1
$$

$$
2^n = \sum_{r=n}^{r=0} \binom{n}{r}
$$

Also, if we notice, for a 2-term determinant, we have $2^n$ terms. Similarly, we can have $t$ terms, and their corresponding terms will be $t^n$:

$$
(1 + a)^n = \sum_{r=n}^{r=0} \binom{n}{r} a^r
$$

Setting $a := a + 1$:

$$
(1 + (a + 1))^n = \sum_{r_1=n}^{r_1=0} \sum_{r_2=r_1}^{r_2=0} \binom{n}{r_1} \binom{r_1}{r_2} a^{r_2} \quad \text{where} \quad \binom{n}{r_1} = \binom{r_1}{r_2} = \frac{n!}{(n-r_1)!r_1!}
$$

$$
3^n = \sum_{r_1=n}^{r_1=0} \sum_{r_2=r_1}^{r_2=0} \binom{n}{r_1} \binom{r_1}{r_2} \quad \text{at} \ a = 1
$$

$$
t^n = \sum_{r_1=n}^{r_1=0} \sum_{r_2=r_1}^{r_2=0} \ldots \sum_{r_{t-2}=r_{t-1}}^{r_{t-2}=0} \binom{n}{r_1} \binom{r_1}{r_2} \ldots \binom{r_{t-2}}{r_{t-1}}
$$

In general, for a given set of square matrices, we transform them into a rank-3 tensor $a^{(\lambda)}_{ij}$ where $\lambda$ controls the terms of the matrices. To account for the interchangeability of rows or columns, we create a subset of $\lambda$ values, considering all possible combinations. The determinant is then calculated for each arrangement, and the sum of these determinants yields the same result as the determinant of the sum of matrices:

$$
A^{(\lambda)} = \begin{bmatrix} a^{(\lambda)}_{11} & \ldots & a^{(\lambda)}_{1n} \\ \ldots & \ldots & \ldots \\ a^{(\lambda)}_{n1} & \ldots & a^{(\lambda)}_{nn} \end{bmatrix}
$$

$$
\det(A^{(0)} + A^{(1)} + \ldots + A^{(t-1)}) \equiv \sum_{\text{terms} = t^n}^{(\lambda_1, \lambda_2, \ldots, \lambda_n) \subset \text{all comb}} \det\begin{bmatrix} a^{(\lambda_1)}_{11} & \ldots & a^{(\lambda_1)}_{1n} \\ \ldots & \ldots & \ldots \\ a^{(\lambda_n)}_{n1} & \ldots & a^{(\lambda_n)}_{nn} \end{bmatrix}
$$
