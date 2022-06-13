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
	b=input("please psecify wifi bssid number,example: [00:11:22:33:44:55:66] ...-------->")
	c=input('please specify wifi channel number,example: ["8"] ...--------> ')
	d=input('please specify wifi name,example: ["sagar"] ...-------->')
	f=input('please specify your interface name, [example:wlan0] ...-------->')
	subprocess.run(["airodump-ng","--bssid",b ,"--channel",c,"--write",d,f])

