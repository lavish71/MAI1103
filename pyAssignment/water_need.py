
zoo_file = open("zoo.csv","rt")

read_zoo = zoo_file.readlines()

water = 0
# Total water taken by elephant
for i in read_zoo:
    split= i.split(',')
    if(split[0]=='elephant'):
        water = water + int(split[2])
        

print 'Total water taken by elephant = ',water  
zoo_file.close()
water = 0
#Total water taken by tiger
for i in read_zoo:
    split= i.split(',')
    if(split[0]=='tiger'):
        water = water + int(split[2])
e=0        

print 'Total water taken by tiger is = ',water
water =0
#Total water taken by zebra
for i in read_zoo:
    split= i.split(',')
    if(split[0]=='zebra'):
        water = water + int(split[2])
e=0        

print 'Total water taken by zebra = ',water
water =0      
#Total water taken by lion
for i in read_zoo:
    split= i.split(',')
    if(split[0]=='lion'):
        water = water + int(split[2])
e=0        

print 'total water dirnk by lion = ',water
water =0
#Total water taken by kangaroo
for i in read_zoo:
    split= i.split(',')
    if(split[0]=='kangaroo'):
        water = water + int(split[2])
e=0        

print 'Total water taken by kangaroo = ',water

