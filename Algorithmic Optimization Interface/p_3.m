function [H] = p_3(g,h,i)
fileID=fopen('parameter angle.txt','w');
fileID2=fopen('parameter thickness.txt','w');
fileID3=fopen('parameter width.txt','w');
fprintf(fileID,'%12.8f\n',g);
fprintf(fileID2,'%12.8f\n',h);
fprintf(fileID3,'%12.8f\n',i);
system('ForceIO.py');
fclose(fileID);
fID3=fopen('result3.txt','r');
formatSpec='%f';
OutData=fscanf(fID3,formatSpec);
H=[OutData];
fclose(fID3);

end