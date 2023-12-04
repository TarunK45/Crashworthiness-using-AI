function [G] = p_1(a,b,c)
fileID=fopen('parameter angle.txt','w');
fileID2=fopen('parameter thickness.txt','w');
fileID3=fopen('parameter width.txt','w');
fprintf(fileID,'%12.8f\n',a);
fprintf(fileID2,'%12.8f\n',b);
fprintf(fileID3,'%12.8f\n',c);
system('MassIO.py');
fclose(fileID);
fID=fopen('result.txt','r');
formatSpec='%f';
OutData=fscanf(fID,formatSpec);
G=[OutData];
fclose(fID);

end