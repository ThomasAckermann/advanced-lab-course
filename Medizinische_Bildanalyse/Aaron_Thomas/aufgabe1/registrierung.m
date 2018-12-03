bild1 = imread('bild4.png');
bild1 = rgb2gray(bild1);
bild2 = imread('bild5.png');
% bild2 = imread(['bild',i,'.png']);
bild2 = rgb2gray(bild2);

[optimizer,metric] = imregconfig('monomodal');
T = imregtform(bild1,bild2,'translation',optimizer,metric);
Referenz = imref2d(size(bild2));
bild_transformiert = imwarp(bild1,T,'OutputView',Referenz);
figure
imshowpair(bild_transformiert,bild2)

tx=T.T(3,1);
ty=T.T(3,2);
disp(tx)
disp(ty)


