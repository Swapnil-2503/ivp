a=imread("image.jpg");
a1=fft2(double(a));
b=abs(a1);
c=angle(a1);
d=b.*(exp(li*c));
e=ifft2(d);
f=unit8(e);
imshow(f);


a = [0,1,2,1,;1,2,3,2;2,3,4,3;1,2,3,2];
N = 4;
k = dftmtx(N);

m1 = k * reshape(a, N, []) * k.';
display(m1);

m2 = fft2(reshape(a, [N, N]));
display(m2);

