% Yekta Demirci 2093607
% Zumrud Shukurlu 2174761

%3 level discrete wavelet transform
A1 = imread('A1.png');
[cA1,cH1,cV1,cD1]=dwt2(A1,'haar');
[cA2,cH2,cV2,cD2]=dwt2(cA1,'haar');
[cA3,cH3,cV3,cD3]=dwt2(cA2,'haar');

%To find the corrupted ones
%subplot(1,4,1)
%imagesc(uint8(cA2))
%subplot(1,4,2)
%imagesc(uint8(cH2))
%subplot(1,4,3)
%imagesc(uint8(cV2))
%subplot(1,4,4)
%imagesc(uint8(cD2))

%3 level discrete wavelet transform
A2 = imread('A2.png');
[ccA1,ccH1,ccV1,ccD1]=dwt2(A2,'haar');
[ccA2,ccH2,ccV2,ccD2]=dwt2(ccA1,'haar');
[ccA3,ccH3,ccV3,ccD3]=dwt2(ccA2,'haar');

%To find the corrupted ones
%subplot(1,4,1)
%imagesc(uint8(a2recon1))
%subplot(1,4,2)
%imagesc(uint8(ccH1))
%subplot(1,4,3)
%imagesc(uint8(cH1))
%subplot(1,4,4)
%imagesc(uint8(cV1))

%Reconstruction of the images
a1recon2 = idwt2(cA3,cH3,cV3,cD3,'haar');
a1recon1 = idwt2(a1recon2,cH2,cV2,ccH2,'haar');
a1recon1=a1recon1(:,1:211);
a1recon = idwt2(a1recon1,cD1,ccV1,ccD1,'haar');

%Reconstruction of the images
a2recon2 = idwt2(ccA3,ccH3,ccV3,ccD3,'haar');
a2recon1 = idwt2(a2recon2,ccV2,cD2,ccD2,'haar');
a2recon1=a2recon1(:,1:211);
a2recon = idwt2(a2recon1,ccH1,cH1,cV1,'haar');

imwrite(uint8(a1recon), 'A1_output.png');

imwrite(uint8(a2recon), 'A2_output.png');
