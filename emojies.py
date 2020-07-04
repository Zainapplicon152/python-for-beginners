print('\U0001F64B')  # \U000code
print(end="\n")
for i in range(0, 5):
    for j in range(0, 16):
        z = format(j, 'x')
        d = ('\\U0001F6%s%s' % (i, z)).encode('utf-8')
        print(d.decode('raw_unicode_escape'), end=" ")
print(end="\n")

print("\u2776")
