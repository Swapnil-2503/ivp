a=imread('image.jpg');

figure(1);
subplot(2,2,1);
title("original image");
imshow(a);

b=0.3.*a(:,:,1)+0.59.*a(:,:,2)+0.11.*a(:,:,3);
figure(2);
subplot(2,2,2);
title("by formula");
imshow(b);

c=rgb2gray(a);
figure(3);
subplot(2,2,3);
title("by function rgb2gray");
imshow(c);

d=im2bw(c);
figure(4);
subplot(2,2,4);
title("by function im2bw");
imshow(d);