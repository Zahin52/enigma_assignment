#MD Zahin Uddin
#ID:17701052
#initaial rotor setting
initial_rotor1 = [['a','e'], ['b', 'k'], ['c','m'],['d', 'f'],['e', 'l'],['f', 'g'],['g', 'd'],['h', 'q'],['i', 'v'],['j', 'z'],['k', 'n'],['l', 't'],['m', 'o'],['n', 'w'],['o', 'y'],['p', 'h'],['q', 'x'],['r', 'u'],['s', 's'],['t', 'p'],['u', 'a'],['v', 'i'],['w', 'b'],['x', 'r'],['y', 'c'],['z', 'j']]

initial_rotor2 = [['a','a'], ['b', 'j'], ['c','d'],['d', 'k'],['e', 's'],['f', 'i'],['g', 'r'],['h', 'u'],['i', 'x'],['j', 'b'],['k', 'l'],['l', 'h'],['m', 'w'],['n', 't'],['o', 'm'],['p', 'c'],['q', 'q'],['r', 'g'],['s', 'z'],['t', 'n'],['u', 'p'],['v', 'y'],['w', 'f'],['x', 'v'],['y', 'o'],['z', 'e']]

initial_rotor3 = [['a','b'], ['b', 'd'], ['c','f'],['d', 'h'],['e', 'j'],['f', 'l'],['g', 'c'],['h', 'p'],['i', 'r'],['j', 't'],['k', 'x'],['l', 'v'],['m', 'z'],['n', 'n'],['o', 'y'],['p', 'e'],['q', 'i'],['r', 'w'],['s', 'g'],['t', 'a'],['u', 'k'],['v', 'm'],['w', 'u'],['x', 's'],['y', 'q'],['z', 'o']]

#reflector
reflector = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'd', 'i', 'j', 'k', 'g', 'm', 'k', 'm', 'i', 'e', 'b', 'f', 't', 'c', 'v', 'v', 'j', 'a', 't']

rotor1 = initial_rotor1
rotor2 = initial_rotor2
rotor3 = initial_rotor3

#rotors' cycle end_mark
rotor1_end = ['z', 'j']
rotor2_end = ['z', 'e']
rotor3_end = ['z', 'o']

#resetting rotors
def reset():
    rotor1 = initial_rotor1
    rotor2 = initial_rotor2
    rotor3 = initial_rotor3 

#rotating a rotor clockwise(1 element)
def rotate(r):
    temp = r[1:26]
    temp.append(r[0])
    return temp

#getting 'first member' of a rotor equal to "second member"
def findFirst(r,l):
    j = 0
    #print(r)
    while j<26:
        if r[j][0]==l:
            break
        j+=1
    return j

#getting "Second member" of a rotor equal to 'first member'
def findSecond(r,l):
    j = 0
    while j<26:
        if r[j][1] == l:
            break
        j+=1
    return j

#Going in forward direction while finding letter
#(from right to left rotor)
def goForward(index):
    letter1 = rotor3[index][1] #the letter in that position
    index1 = findFirst(rotor3,letter1) #index of that letter as first member in rotor3
    letter2 = rotor2[index1][1] #the letter(second mem) in the rotor2 in that index
    index2 = findFirst(rotor2,letter2) #index of that letter as (first member) in rotor2
    letter3 = rotor1[index2][1] #the letter(second mem) in the rotor1 in that index
    index3 = findFirst(rotor1,letter3) #index of that letter as (first member) in rotor1

    return index3

#Get reflect_back index
def getReflected(index):
    i=0
    while i<26:
        if i==index:
            i+=1
            continue
        if reflector[i]==reflector[index]:
            break
        i+=1
    return i

#Going in backward direction while finding letter
#(from left to right rotor)
def goBackward(index):
    letter1 = rotor1[index][0] #the letter(first mem) in the rotor1 in that relected_index
    index1 = findSecond(rotor1,letter1) #index of that letter as (second member) in rotor1
    letter2 = rotor2[index1][0] #the letter(first mem) in the rotor2 in that index
    index2 = findSecond(rotor2,letter2) #index of that letter as (second member) in rotor2
    letter3 = rotor3[index2][0] #the letter(first mem) in the rotor3 in that index
    index3 = findSecond(rotor3,letter3) #index of that letter as (Second member) in rotor3
    letter = chr(index3+97)
    
    return letter
        
#getting code letter
def getLetter(m):
    index = ord(m)-97 #the position of the input letter
    
    index = goForward(index) #GoForward (from right to left rotor)
    reflected_index = getReflected(index) #Get reflect_back index
    code = goBackward(reflected_index) #GoBackward (from left to right rotor)
    
    return code

#Setting rotor with user's setting
def setRotor(r,x):
    index = 0
    while index<26:
        if r[index][0]==x:
            break
        index+=1

    temp = r[index:26]
    temp += r[0:index]
    
    return temp
        
######################################################
######################################################

#taking input
c = input("Do you have a setting for the machine?(y/n):")
if c=='y':
    setting = input("Give your 3 letter setting( *small letter* ):")
    while len(setting)!=3:
        setting = input("The length of the setting must be 3.\nGive your 3 letter setting(* small letter* ):")
    rotor1 = setRotor(rotor1,setting[0])
    rotor2 = setRotor(rotor2,setting[1])
    rotor3 = setRotor(rotor3,setting[2])

msg_code = input("Give your msg/code( *small letter* ):")
print("\ninput:",msg_code)

output = ''

#reset()
i=0
length = len(msg_code)

while i<length:
    m = msg_code[i]
    if not(m>chr(96) and m<chr(123)):
        output+=m
        i+=1
        continue
        
    if rotor3[0]==rotor3_end:
        rotor2 = rotate(rotor2) #rotor2 will get rotated if rotor3 reach end_mark
        #print("Rotor 2 got rotated!")
        
    if rotor2[0]==rotor2_end:
        rotor1 = rotate(rotor1) #rotor1 will get rotated if rotor2 reach end_mark
        #print("Rotor 3 got rotated!")
        
    rotor3 = rotate(rotor3) #rotor3 will get rotated with every input letter
    
    output += getLetter(m)
    i+=1

#this is the output:(msg/code)abc
print("\noutput:",output)
