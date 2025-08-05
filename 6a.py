OP=set(['+','-','*','/','(',')','^'])
PR={'+':1,'-':1,'*':2,'^':3}
def i_to_p(exp):
    stack=[]
    output=''
    for ch in exp:
        if ch not in OP:
            output+=ch
        elif ch=='(':
            stack.append('(')
        elif ch==')':
            while stack and stack[-1]!='(':
                output+=stack.pop()
            stack.pop()
        else:
            while stack and stack[-1]!='(' and PR[ch]<=PR[stack[-1]]:
                output+=stack.pop()
            stack.append(ch)
    while stack:
        output+=stack.pop()
    return output
exp=input('Enter infix expression')
print('infix expression:',exp)
print('postfix expression:',i_to_p(exp))
