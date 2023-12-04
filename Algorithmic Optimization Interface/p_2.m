function [F] = p_2(d,e,f)
fileID=fopen('parameter angle.txt','w');
fileID2=fopen('parameter thickness.txt','w');
fileID3=fopen('parameter width.txt','w');
fprintf(fileID,'%12.8f\n',d);
fprintf(fileID2,'%12.8f\n',e);
fprintf(fileID3,'%12.8f\n',f);
system('EnergyIO.py');
fclose(fileID);
fID1=fopen('result2.txt','r');
formatSpec='%f';
OutData=fscanf(fID1,formatSpec);
F=-[OutData];
fclose(fID1);

end

