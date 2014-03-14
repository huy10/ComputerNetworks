clear all; close all; clc;

fid = fopen('stat_UDP_dest_out_top10.txt', 'r');
flag = 1;
count = zeros(1:11);
for m = 1:11
    while flag == 1 && ~feof(fid)
        tline = fgetl(fid);
        for i = 1:length(tline)
            if tline(i) == ':'
                flag = 0;
                port(m) = str2num(tline(i+1:length(tline)));
            end
        end
        count(1,m) = count(1,m) + 1;
    end
    flag = 1;
end

fclose(fid);
figure;
fid = fopen('stat_UDP_dest_out_top10.txt', 'r');
for j = 1:10
    tline = fgetl(fid);
    data = fscanf(fid, '%f',[2,count(1,j+1)]);    
    data1 = zeros(1,length(data(2,:)));
    for n = 1:length(data(2,:))
        for m = 1:n
            data1(n) = data1(n) + data(2,m);
        end
    end
    subplot(5,2,j),plot(data(1,1:length(data1)),data1);
end
fclose(fid);

fid = fopen('stat_UDP_dest_out_top10.txt', 'r'),title('sum in each port');;
figure;
sum = zeros(1,10);
for j = 1:10
    tline = fgetl(fid);
    data = fscanf(fid, '%f',[2,count(1,j+1)]);    
    data1 = zeros(1,length(data(2,:)));
    for n = 1:length(data(2,:))
        sum(j) = sum(j) + data(2,n);
    end
    
end

bar(sum ),colormap(cool),title('datas in each port');
fclose(fid);
%{
fid = fopen('stat_TCP_dest_in_top10.txt', 'r');
flag = 1;
count = zeros(1,10);
m = 0;
while  ~feof(fid)
        tline = fgetl(fid);
        for i = 1:length(tline)
            if tline(i) == ':'
               flag = 0;
               m = m +1;
            end
        end
       if flag == 1 && m ~= 11
           count(m) = count(m) + 1;
       end
       flag = 1;
 end
  fclose(fid);
  fid = fopen('stat_TCP_dest_in_top10.txt', 'r');
figure; 
m = 0;
while  ~feof(fid)
        tline = fgetl(fid);
        for i = 1:length(tline)
            if tline(i) == ':'
               flag = 0;
               m = m +1;
            end
        end
        
       if flag == 1 && m < 11
           sum(m,:) = zeros(1,1000);
             for t = 1: count(m)
                 data(t,:) = sscanf(tline, '%f',[1 2]);         
             end
             
       end
       if flag == 1 && m < 11
       for t = 1: count(m)
                  for s = 1:t
                        sum(m,t) = sum(m,t) + data(s,2);
                        
                  end
       end
         subplot(5,2,m);
        plot([1:count(m)],sum(m,:));
       end
       
       
      
       
       
       flag = 1;
 end

fclose(fid);
%}
%{
fid = fopen('stat_TCP_dest_in_top10.txt', 'r');
figure; 
for j = 1:10
    tline = fgetl(fid);
   if flag == 1 
            if tline(i) == ':'
               tline = fgetl(fid)
               flag = 0;
            end
   end
     
    
    data = zeros(count(j),2);
    for t = 1: count(j)
        data(t,:) = sscanf(tline, '%f',[1 2]);
    end
    data1 = zeros(1,length(data(2,:)));
   for n = 1:length(data(2,:))
       for m = 1:n
            data1(n) = data1(n) + data(2,m);
       end
   end
    
    %for n = 1:length(data(2,:))
    %    data1(j) = data1(j) + data(2,n)
    %end
    subplot(5,2,j);
    plot(data(1,:),data1);
   
end
% legend(1,2,3,4,5,6,7,8,9,10);
fclose(fid);
%}
