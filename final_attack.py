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
	a=input("please specify wifi name,example: ['D_link_sagar']")
	b=a+" -01.cap"
	c=input("please specify thw wordlist name,example: ['sagar.txt']")
	subprocess.run(["aircrack-ng",b,"-w",c])
