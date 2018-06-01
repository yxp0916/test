# f=open('555.txt','r')
# lines=f.readlines()
# print(lines)
#
# for line in lines:
#     print(line.split(',')[2])
import csv
# csv_file=csv.reader(open('stu_info.csv','r'))
# #print(csv_file)
#
# for stu in csv_file:
#     print(stu)

stu1=['Marry',30,'Chengdu']
stu2=['Rom',23,'Chengdu']

out=open('stu_info.csv','a',newline='')
csv_write=csv.writer(out,dialect='excel')
csv_write.writerow(stu1)
csv_write.writerow(stu2)
print("Write file over!")