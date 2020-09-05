def valid(s):
    stack = []
    for i in range(0, len(s)):
        if s[i] == '(' or s[i] == '{' or s[i] == '[':
            stack.append(s[i])
        if s[i] == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                return 'false'
        if s[i] == '}':
            if stack[-1] == '{':
                stack.pop()
            else:
                return 'false'
        if s[i] == ']':
            print('revati')
            if stack[-1] == '[':
                stack.pop()
            else:
                return 'false'
                print(1)
    if stack == []:
        return 'true'
    else:
        return 'false'
s = "()[]"
print(valid(s))