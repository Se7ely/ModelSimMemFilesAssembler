filename = input("Enter filename to assemble: ")
fr = open(filename,'r')
lines=[]
nocomments=[]
nospaces=[]
notabs=[]
nonls=[]
input=[]
binput=[]
output=[]

while True:
    line = fr.readline()
    if not line:
        break
    else:
        lines.append(line)

for i in lines:
    if '#' in i:
        nocomments.append(i.replace(i[i.index('#'):],''))
    else :
        nocomments.append(i)

for i in nocomments:
    nospaces.append(i.replace(' ','',100))


for i in nospaces:
    notabs.append(i.replace('\t','',100))


for i in notabs:
    nonls.append(i.replace('\n','',100))

for i in nonls:
    if i != '':
        input.append(i.lower())

for ins in input:
    if 'org' in ins:
        binput.append(ins)
    elif 'nop' in ins:
        binput.append("0000000000000000")

    elif 'setc' in ins:
        binput.append("0000000000001000")

    elif 'clrc' in ins:
        binput.append("0000000000010000")

    elif 'not' in ins:
        rd=ins[ins.index('r')+1:]
        rds=bin(int(rd)).replace('b','0')[-3:]
        binput.append("001000"+rds+"0000000")

    elif 'dec' in ins:
        rd = ins[ins.index('r')+1:]
        rds = bin(int(rd)).replace('b', '0')[-3:]
        binput.append("001000"+rds+"0001000")

    elif 'inc' in ins:
        rd = ins[ins.index('r')+1:]
        rds = bin(int(rd)).replace('b', '0')[-3:]
        binput.append("001000"+rds+"0010000")

    elif 'mov' in ins:
        ir1=ins.index('r')+1
        ir2=ins.index('r',ir1)+1
        icomma=ins.index(',')
        rs=ins[ir1:icomma]
        rd=ins[ir2:]
        rss=bin(int(rs)).replace('b', '0')[-3:]
        rds=bin(int(rd)).replace('b', '0')[-3:]

        binput.append("001"+rss+rds+"0011000")

    elif 'add' in ins:
        ir1 = ins.index('r')+1
        ir2 = ins.index('r', ir1)+1
        icomma = ins.index(',')
        rs = ins[ir1:icomma]
        rd = ins[ir2:]
        rss = bin(int(rs)).replace('b', '0')[-3:]
        rds = bin(int(rd)).replace('b', '0')[-3:]

        binput.append("001"+rss+rds+"0100000")

    elif 'sub' in ins:
        ir1 = ins.index('r')+1
        ir2 = ins.index('r', ir1)+1
        icomma = ins.index(',')
        rs = ins[ir1:icomma]
        rd = ins[ir2:]
        rss = bin(int(rs)).replace('b', '0')[-3:]
        rds = bin(int(rd)).replace('b', '0')[-3:]

        binput.append("001"+rss+rds+"0101000")

    elif 'and' in ins:
        ir1 = ins.index('r')+1
        ir2 = ins.index('r', ir1)+1
        icomma = ins.index(',')
        rs = ins[ir1:icomma]
        rd = ins[ir2:]
        rss = bin(int(rs)).replace('b', '0')[-3:]
        rds = bin(int(rd)).replace('b', '0')[-3:]

        binput.append("001"+rss+rds+"0110000")

    elif 'or' in ins:
        ir0 = ins.index('r')+1
        ir1 = ins.index('r', ir0)+1
        ir2 = ins.index('r', ir1)+1
        icomma = ins.index(',')
        rs = ins[ir1:icomma]
        rd = ins[ir2:]
        rss = bin(int(rs)).replace('b', '0')[-3:]
        rds = bin(int(rd)).replace('b', '0')[-3:]

        binput.append("001" + rss + rds + "0111000")

    elif 'shl' in ins:
        ir1 = ins.index('r') + 1
        icomma = ins.index(',')
        rd= ins[ir1:icomma]
        imm=ins[icomma+1:]
        rds=bin(int(rd)).replace('b', '0')[-3:]
        imms=bin(int(imm,16)).replace('b','000')[-5:]
        binput.append("001"+imms[0:3]+rds+"1000"+imms[3:]+"0")

    elif 'shrr' in ins:
        ir0 = ins.index('r') + 1
        ir1 = ins.index('r', ir0) + 1
        icomma = ins.index(',')
        rd = ins[ir1:icomma]
        imm = ins[icomma + 1:]
        rds = bin(int(rd)).replace('b', '0')[-3:]
        imms = bin(int(imm,16)).replace('b', '000')[-5:]
        binput.append("001"+imms[0:3]+rds+"1001"+imms[3:]+"0")

    elif 'mul' in ins:
        ir1 = ins.index('r')+1
        ir2 = ins.index('r', ir1)+1
        icomma = ins.index(',')
        rs = ins[ir1:icomma]
        rd = ins[ir2:]
        rss = bin(int(rs)).replace('b', '0')[-3:]
        rds = bin(int(rd)).replace('b', '0')[-3:]
        binput.append("001"+ rss + rds +"0000100")
        binput.append("001"+ rds + rss +"0001100")

    elif 'push' in ins:
        rd = ins[ins.index('r')+1:]
        rds = bin(int(rd)).replace('b', '0')[-3:]

        binput.append("011000"+rds+"0000000")

    elif 'pop' in ins:
        rd = ins[ins.index('r')+1:]
        rds = bin(int(rd)).replace('b', '0')[-3:]

        binput.append("011000"+rds+"0100000")

    elif 'ldm' in ins:
        ir1 = ins.index('r') + 1
        icomma = ins.index(',')
        rd = ins[ir1:icomma]
        imm = ins[icomma + 1:]
        rds = bin(int(rd)).replace('b', '0')[-3:]
        imms = bin(int(imm,16)).replace('b', '00000000000000')[-16:]
        binput.append("1000"+imms[14:]+rds+"0000000")
        binput.append("1"+imms[0:14]+"1")

    elif 'ldd' in ins:
        ir1 = ins.index('r') + 1
        icomma = ins.index(',')
        rd = ins[ir1:icomma]
        ea = ins[icomma + 1:]
        rds = bin(int(rd)).replace('b', '0')[-3:]
        eas = bin(int(ea,16)).replace('b', '000000000000000000')[-20:]
        binput.append("101"+eas[14:17]+rds+eas[17:20]+"0000")
        binput.append("1"+eas[0:14]+"1")

    elif 'std' in ins:
        ir1 = ins.index('r') + 1
        icomma = ins.index(',')
        rd = ins[ir1:icomma]
        ea = ins[icomma + 1:]
        rds = bin(int(rd)).replace('b', '0')[-3:]
        eas = bin(int(ea,16)).replace('b', '000000000000000000')[-20:]
        binput.append("110"+eas[14:17]+rds+eas[17:20]+"0000")
        binput.append("1"+eas[0:14]+"1")

    elif 'jz' in ins:
        rd = ins[ins.index('r')+1:]
        rds = bin(int(rd)).replace('b', '0')[-3:]
        binput.append("000000"+rds+"1000000")

    elif 'jn' in ins:
        rd = ins[ins.index('r')+1:]
        rds = bin(int(rd)).replace('b', '0')[-3:]
        binput.append("000000"+rds+"1001000")

    elif 'jc' in ins:
        rd = ins[ins.index('r')+1:]
        rds = bin(int(rd)).replace('b', '0')[-3:]
        binput.append("000000"+rds+"1010000")

    elif 'jmp' in ins:
        rd = ins[ins.index('r')+1:]
        rds = bin(int(rd)).replace('b', '0')[-3:]
        binput.append("000000"+rds+"1011000")

    elif 'call' in ins:
        rd = ins[ins.index('r')+1:]
        rds = bin(int(rd)).replace('b', '0')[-3:]
        binput.append("111100"+rds+"1000000")

    elif 'ret' in ins:
        binput.append("1110000001100000")

    elif 'rti' in ins:
        binput.append("1110100001100000")

    elif 'in' in ins:
        rd = ins[ins.index('r')+1:]
        rds = bin(int(rd)).replace('b', '0')[-3:]
        binput.append("001000"+rds+"0011010")

    elif 'out' in ins:
        rd = ins[ins.index('r')+1:]
        rds = bin(int(rd)).replace('b', '0')[-3:]
        binput.append("001"+rds+"0000011100")

    else:
        num=bin(int(ins,16)).replace('b','000000000000000000000000000000')[-32:]
        binput.append(num[16:])
        binput.append(num[0:16])

writeline=0
org=0
for instruction in binput:
    if '.org' in instruction:
        org=int(instruction[4:],16)

        while org!=writeline:
            output.append('0000000000000000')
            writeline=writeline+1

    else:
        output.append(instruction)
        writeline=writeline+1


of=open(filename[0:-3]+"mem",'w')

of.write('// memory data file (do not edit the following line - required for mem load use)')
of.write('\n')
of.write('// instance=/integration/FandM/MemoryI/ram')
of.write('\n')
of.write('// format=bin addressradix=h dataradix=b version=1.0 wordsperline=1')
of.write('\n')
address=0
for p in output:
    of.write(("      @"+hex(address).replace('0x','')+' ')[-7:])
    of.write(p)
    of.write('\n')
    address = address + 1

while writeline != 2**20:
    of.write(("      @" + hex(address).replace('0x', '') + ' ')[-7:])
    of.write('0000000000000000')
    of.write('\n')
    writeline=writeline+1
    address=address+1
fr.close()
of.close()
