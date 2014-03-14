clear all; close all; clc;

fid = fopen('statistics_3_UDP_final.txt', 'r');
%tline = fgetl(fid);
data = fscanf(fid, '%f',[2,inf]);
data1 = zeros(1,length(data(2,:)))
for n = 1:length(data(2,:))
    for m = 1:n
        data1(n) = data1(n) + data(2,m);
    end
end
fclose(fid);

figure; plot(data(1,:),data1);xlabel('length of the packet'),...
    ylabel('total length of datagram'),legend('UDP');
