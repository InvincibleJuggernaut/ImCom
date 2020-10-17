# ImCom

<h2>Introduction</h2>
<p> This repository implements lossless image compression using Haar Transform which is categorized under Discrete Wavelet Transforms. It breaks the signal into two components namely, average and difference. The average operation produces the <i>approximation coefficients</i> and the difference operation produces <i>detail coefficients</i>.
<p> The program takes a RGB image as an input and produces a compressed image which looks visually the same.</p>

<h2>Working</h2>

<p> The core principle can be understood using an example :</p>
<p> Let's imagine we have an array </p> <br>
<p align="center"> <img src="https://render.githubusercontent.com/render/math?math=A = [1, 2, 3, 4, 5, 6, 7, 8]"></p>
<p> First, we group adjacent elements to form pairs.</p>
<p align="center"> <img src="https://render.githubusercontent.com/render/math?math=|1, 2|, |3, 4|, |5, 6|, |7, 8|"></p>
<p> Now, average each pair and produce a new array with the first four entries as the averages. Calculate half the difference of the pairs and these four results would occupy the last four slots in the new array.</p>
<p align="center"> <img src="https://render.githubusercontent.com/render/math?math=A' = [+1.5, +3.5, +5.5, +7.5, -0.5, -0.5, -0.5, -0.5]"></p>
<p> Here, the first four elements are the approximation coefficients and the last four are detail coefficients.</p>
<p> In the next step, we form pairs from half the length i.e we form two pairs from the first four elements.</p>
<p align="center"> <img src="https://render.githubusercontent.com/render/math?math=|1.5, 3.5|, |5.5, 7.5|"></p>
<p> We again average the pairs and find out half the differences and replace the first four entries.</p>
<p align="center"> <img src="https://render.githubusercontent.com/render/math?math=A'' = [2.5, 6.5, -1.0, -1.0, -0.5, -0.5, -0.5, -0.5, -0.5]"></p>
<p> This time, we form one pair from the first two elements and carry out the same oeprations as we did before.</p>
<p align="center"> <img src="https://render.githubusercontent.com/render/math?math=A''' = [4.5, -2.0, -1.0, -1.0, -0.5, -0.5, -0.5, -0.5, -0.5]"></p>

<p> We observe that our latest array has reduced greatly with almost all elements close to 0 except the first one. We can reverse this process to obtain the original array.</p>
<p> We originally had an array with 8 elements. We carried out the operations 3 times. So, how did we arrive at this number? Is it just hit and trial? No, we can find out the number of the iterations by using the formula:</p>
<p align="center"> <img src="https://render.githubusercontent.com/render/math?math=n= log(array~length)/log(2)"></p>

<p> An image can be assumed to be a matrix of finite such arrays. To compress an image, we carry out these operations for all rows and columns to produce a greatly reduced matrix. We could further achieve more compression by choosing a limit and setting all elements in the array whose absolute value is lower than that limit. In the above example, we could set the limit as 0.5. The newly reduced array would be :</p>
<p align="center"> <img src="https://render.githubusercontent.com/render/math?math=A''' = [4.5, -2.0, -1.0, -1.0, 0, 0, 0, 0, 0]"></p>

<p> There are two approaches to arrive at the same result. We could either iterate through each element of the image and carry out the averaging and subtraction operations. The alternative is to use linear algebra to make the process faster. We could just multiply the image matrix with the Haar transform matrix to get the reduced matrix. This repository makes use of the second method. 
