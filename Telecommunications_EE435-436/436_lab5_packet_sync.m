% EE436 Lab5: Packet Synchronisation

close all
clear all

Own13 = [1 1 -1 -1 1 1 -1 -1 1 1 -1 -1 1]; 
barker5 = [+1 +1 +1 -1 +1];
barker13 = [+1 +1 +1 +1 +1 -1 -1 +1 +1 -1 +1 -1 +1];

%MF
h5 = fliplr(barker5);
h13 = fliplr(barker13);

y5 = conv(Own13,h5);
y13 = conv(Own13,h13);

% plot(y5)
% figure(2)
% plot(y13)


%% 1.b
packet_1 = 0;
packet_2 = 0;
packet_3 = 0;

for i=1:20
    data1 = 2*randi([0 1], 1, 100)-1;
    packet_1 = [packet_1 barker13 data1];
end
frame1 = packet_1(2:length(packet_1));

for i=1:20
    data2 = 2*randi([0 1], 1, 100)-1;
    packet_2 = [packet_2 Own13 data2];
end
frame2 = packet_2(2:length(packet_2));

for i=1:20
    data3 = 2*randi([0 1], 1, 100)-1;
    packet_3 = [packet_3 barker5 data3];
end
frame3 = packet_3(2:length(packet_3));

% MF:
mf1 = fliplr(barker13);
mf2 = fliplr(Own13);
mf3 = fliplr(barker5);

y1 = conv(mf1,frame1);
y2 = conv(mf2, frame2);
y3 = conv(mf3, frame3);


