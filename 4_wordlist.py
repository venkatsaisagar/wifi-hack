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
	a=input("please specify the minimun length of wordlist,example: [2,3,4,5]")
	b=input("please specify the maximum length of wordlist,example: [8,9,10]")
	c=input("please specify the characteristics of words to generate the wordlist,example: [abc@#$123] ")
	d=input("please give any name for worlsit,example: [sagar]")
	subprocess.run(['crunch',a,b,c,'-o',d])
	subprocess.run(['cat',d ])
