SP=int(input('enter SP :'))
CP=int(input('enter CP :'))
profit=SP-CP
LOSS=CP-SP
if(SP>CP):
     print(f'profit is :{profit}')
elif(SP<CP):
     print(f'loss is :{LOSS}')
else:
     print('no profit, no loss')     


