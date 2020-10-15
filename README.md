# ImCom

<h2>Introduction</h2>
<p> This repository implements lossless image compression using Haar Transform which is categorized under Discrete Wavelet Transforms. It breaks the signal into two components namely, average and difference. The average operation produces the <i>approximation coefficients</i> and the difference operation produces <i>detail coefficients</i>.
</p>

<p> The core principle can be understood using an example :</p>
<p> Let's imagine we have an array </p> <br>
<p align="center"> <img src="https://render.githubusercontent.com/render/math?math=A = [1, 2, 3, 4, 5, 6, 7, 8]"></p>
<p> First, we group adjacent elements to form pairs.</p>
<p align="center"> <img src="https://render.githubusercontent.com/render/math?math=|1, 2|, |3, 4|, |5, 6|, |7, 8|"></p>
<p> Now, average each pair and produce a new array with the first four entries as the averages. Calculate the difference of the pairs, half them and these dour results would occupy the alst four slots in the new array.</p>
<p align="center"> <img src="https://render.githubusercontent.com/render/math?math=A = [+1.5, +3.5, +5.5, +7.5, -0.5, -0.5, -0.5, -0.5]"></p>
<p> Here, the first four elements are the approximation coefficients and the last four are detail coefficients.</p>
