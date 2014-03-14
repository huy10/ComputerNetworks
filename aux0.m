clear all; close all; clc;

fid = fopen('statistics_5_final.txt', 'r');
data = fscanf(fid, '%f',[1,inf]);
for n = 2:length(data)
    data1(n-1) = data(n);
    %data1(n-1) = data1(n-1)/data(1);
end
fclose(fid);
data1 = data1/data(1);
figure; bar(data1);xlabel('1-9 represents NS,CWR,ECE,URG,ACK,PSH,RST,SYN,FIN, respectively'),...
    ylabel('number');
