camList = webcamlist;
cam = webcam(1);
bild = snapshot(cam);
figure1 = figure;
bild_grau = rgb2gray(bild);
imshow(bild_grau);
