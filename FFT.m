a=imread("cameraman.jpg");
b=fft2(a);
f1=abs(b);
f2=log(f1);
f3=log(abs(fftshift(f1)));

imtool(f1,[]);
imtool(f2,[]);
imtool(f3,[]);

f(1:20, 20:40)=0;
imtool(log(abs(f)),[]);
