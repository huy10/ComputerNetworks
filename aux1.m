clear all; close all; clc;

%task1
fid = fopen('statistics_1_final.txt', 'r');
tline = fgetl(fid);
data = fscanf(fid, '%f',[3,inf]);
fclose(fid);

test(1) = data(2,4);
test(2) = data(2,10);
test2(1) = data(3,4);
test2(2) = data(3,10);
figure; pie(test,{'TCP','UDP'}),title('by segments');
figure; pie(test2,{'TCP','UDP'}),title('by datagrams');
