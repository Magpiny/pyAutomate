import pyperclip
print(1+2)

lws = "I love taking lemon juice every morning"
spm = lws.upper()
print(lws.center(80, '>'))
name = 'Samm'
jst = name.center(20, '=')
print(jst)

print(lws.replace('love', 'like'))

# piper clip module
# Has copy and paste functions
pyperclip.copy(lws)

print(pyperclip.paste())