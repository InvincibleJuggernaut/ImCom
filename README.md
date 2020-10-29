# ImCom

<h2>Introduction</h2>
<p> This repository implements lossless image compression using Haar Transform which is categorized under Discrete Wavelet Transforms. It breaks the signal into two components namely, average and difference. The average operation produces the <i>approximation coefficients</i> and the difference operation produces <i>detail coefficients</i>.
<p> The program takes a RGB image as an input and produces a compressed image which looks visually the same.</p>


<p align="center">
  <img src="/Assets/abc.jpg">&emsp; &emsp; &emsp;
  <img src="/Assets/decompressed.jpg">
  </p>

<p> The first image's original size is 2.7 MB. After compression, the second image was obtained whose size was reduced to 418.7 KB !</p>


<h2>Working</h2>

<p> The core principle can be understood using an example :</p>
<p> Let's imagine we have an array </p> <br>
<p align="center"><img src="https://render.githubusercontent.com/render/math?math=A%20%3D%0A%5Cbegin%7Bbmatrix%7D%0A1%20%26%202%20%26%203%20%26%204%20%26%205%20%26%206%20%26%207%20%26%208%20%0A%5Cend%7Bbmatrix%7D"></p>

<p> First, we group adjacent elements to form pairs.</p>
<p align="center"><img src="https://render.githubusercontent.com/render/math?math=A%20%3D%0A%5Cbegin%7Bbmatrix%7D%0A1%20%26%202%20%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A3%20%26%204%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A5%20%26%206%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A7%20%26%208%0A%5Cend%7Bbmatrix%7D"></p>

<p> Now, average each pair and produce a new array with the first four entries as the averages. Calculate half the difference of the pairs and these four results would occupy the last four slots in the new array.</p>
<p align="center"><img src="https://render.githubusercontent.com/render/math?math=A'%3D%0A%5Cbegin%7Bbmatrix%7D%0A1.5%20%26%203.5%20%26%205.5%20%26%207.5%20%26%20-0.5%20%26%20-0.5%20%26%20-0.5%20%26%20-0.5%20%0A%5Cend%7Bbmatrix%7D"></p>

<p> Here, the first four elements are the approximation coefficients and the last four are detail coefficients.</p>
<p> In the next step, we form pairs from half the length i.e we form two pairs from the first four elements.</p>
<p align="center"><img src="https://render.githubusercontent.com/render/math?math=A%20%3D%0A%5Cbegin%7Bbmatrix%7D%0A1.5%20%26%203.5%20%0A%5Cend%7Bbmatrix%7D%0A%5Cbegin%7Bbmatrix%7D%0A5.5%20%26%207.5%0A%5Cend%7Bbmatrix%7D%0A"></p>

<p> We again average the pairs and find out half the differences and replace the first four entries.</p>
<p align="center"><img src="https://render.githubusercontent.com/render/math?math=A''%3D%0A%5Cbegin%7Bbmatrix%7D%0A2.5%20%26%206.5%20%26%20-1%20%26%20-1%20%26%20-0.5%20%26%20-0.5%20%26%20-0.5%20%26%20-0.5%20%0A%5Cend%7Bbmatrix%7D"></p>

<p> This time, we form one pair from the first two elements and carry out the same operations as we did before.</p>
<p align="center"><img src="https://render.githubusercontent.com/render/math?math=A'''%3D%0A%5Cbegin%7Bbmatrix%7D%0A4.5%20%26%20-2%20%26%20-1%20%26%20-1%20%26%20-0.5%20%26%20-0.5%20%26%20-0.5%20%26%20-0.5%20%0A%5Cend%7Bbmatrix%7D"></p>

<p> We observe that our latest array has reduced greatly with almost all elements close to 0 except the first one. We can reverse this process to obtain the original array.</p>
<p> We originally had an array with 8 elements. We carried out the operations 3 times. So, how did we arrive at this number? Is it just hit and trial? No, we can find out the number of the iterations by using the formula:</p>
<p align="center"> <img src="https://render.githubusercontent.com/render/math?math=n= log(array~length)/log(2)"></p>

<p> An image can be assumed to be a matrix of finite such arrays. To compress an image, we carry out these operations for all rows and columns to produce a greatly reduced matrix. We could further achieve more compression by choosing a limit and setting all elements in the array whose absolute value is lower than that limit. In the above example, we could set the limit as 0.5. The newly reduced array would be :</p>
<p align="center"><img src="https://render.githubusercontent.com/render/math?math=A'''%3D%0A%5Cbegin%7Bbmatrix%7D%0A4.5%20%26%20-2%20%26%20-1%20%26%20-1%20%26%200%20%26%200%20%26%200%20%26%200%0A%5Cend%7Bbmatrix%7D"></p>

<p> There are two approaches to arrive at the same result. We could either iterate through each element of the image and carry out the averaging and subtraction operations. The alternative is to use linear algebra to make the process faster. We could just multiply the image matrix with the Haar transform matrix to get the reduced matrix. This repository makes use of the second method. </p>
  
<p> The image quality can be improved by normalizing the transformation. The 8x8 normalized Haar transform matrix is defined as :</p>
<p align="center"><img src="https://render.githubusercontent.com/render/math?math=H%20%3D%0A%5Cbegin%7Bbmatrix%7D%0A0.35355%20%26%200.35355%20%26%200.50000%20%26%200.00000%20%26%200.70711%20%26%200.00000%20%26%200.00000%20%26%200.00000%5C%5C%0A%5C%5C%0A0.35355%20%26%200.35355%20%26%200.50000%20%26%200.00000%20%26%20-0.70711%20%26%200.00000%20%26%200.00000%20%26%200.00000%5C%5C%0A%5C%5C%0A0.35355%20%26%200.35355%20%26%20-0.50000%20%26%200.00000%20%26%200.00000%20%26%200.70711%20%26%200.00000%20%26%200.00000%5C%5C%0A%5C%5C%0A0.35355%20%26%200.35355%20%26%20-0.50000%20%26%200.00000%20%26%200.00000%20%26%20-0.70711%20%26%200.00000%20%26%200.00000%5C%5C%0A%5C%5C%0A0.35355%20%26%20-0.35355%20%26%200.00000%20%26%200.50000%20%26%200.00000%20%26%200.00000%20%26%200.70711%20%26%200.00000%5C%5C%0A%5C%5C%0A0.35355%20%26%20-0.35355%20%26%200.00000%20%26%200.50000%20%26%200.00000%20%26%200.00000%20%26%20-0.70711%20%26%200.00000%5C%5C%0A%5C%5C%0A0.35355%20%26%20-0.35355%20%26%200.00000%20%26%20-0.50000%20%26%200.00000%20%26%200.00000%20%26%200.00000%20%26%200.70711%5C%5C%0A%5C%5C%0A0.35355%20%26%20-0.35355%20%26%200.00000%20%26%20-0.50000%20%26%200.00000%2C%20%26%200.00000%20%26%200.00000%20%26%20-0.70711%20%20%0A%5C%5C%0A%5Cend%7Bbmatrix%7D"></p>

<!-- To write similar LATEX equations,you can use this link : https://jsfiddle.net/8ndx694g/
Run the code and write the LATEX equation you need to generate the link to be written in README.
-->

<p> A RGB image can be represented as a 3-D matrix. To compress a RGB image, we first need to separate the three colour components, namely R, G & B and store them in separate matrices. The three new matrices obtained are 2-D. Then, we compress them individually, decompress them and combine the three matrices again to form a 3-D matrix. This matrix represents the compressed image after Haar Transform.  </p>

<h2> Dependencies</h2>

<p> All the dependencies can be found <a href="requirements.txt">here</a>.</p>
  
<h2> Comments</h2>
<p> Note that the program is using some user-defined functions wherever possible instead of in-built functions from the libraries. For example, matricex mutliplication has been achieved using raw Python code instead of using the much optimized <i>numpy.dot</i>. Therefore, it shouldn't be a surprise that the program is quite slow. Though, it could be drastically sped up using the in-built functions.</p>
