import subprocess



print(r""" 
  _      _     _ _ _ _      _      _     _    _         ____       _________
 \ \    / /   |  _ _ _|    |  \   | |   | |  / /       /    \     |___   ___|
  \ \  / /    | |_ _ _     | |\\  | |   | | / /       /  /\  \        | |
   \ \/ /     |  _ _ _|    | | \\ | |   | |/_/\      |  /__\  |       | |
    \  /      | |_ _ _     | |  \\| |   | |  \ \     | |    | |       | |
     \/       |_ _ _ _|    |_|   \ _|   |_|   \_\    |_|    |_|       |_|

DINDI VENKAT SAI SAGAR... ... ...
""")

print('\n')
print("THANKS FOR USING MY TOOL :)")
print('\n')
print("YOU CAN REACH OUT TO ME BY :) ")
print('\n')
print("""
    _____
    | S |
    | A |
   _| G |_
   \  A  /
    \ R /
     \ /
      v
""")
print("venkatsaisagar.github@gmail.com")
print('\n')

if __name__=="__main__":
	print('\n')
	subprocess.run(['ifconfig'])

	interface=input("please specify your network card name:...-------->")
	print('\n')
	print('ifconfig')
	subprocess.run(['ifconfig'])
	subprocess.run(['ifconfig',interface,'down'])
	subprocess.run(['airmon-ng','check','kill'])
	subprocess.run(['iwconfig',interface,'mode','monitor'])
	subprocess.run(['ifconfig',interface,'up'])
	subprocess.run(['iwconfig'])
	subprocess.run(['airmon-ng','start',interface])
	new_face=input('please specify the new interface one:...--------> ')
	subprocess.run(['airodump-ng',new_face])
	subprocess.run([])


