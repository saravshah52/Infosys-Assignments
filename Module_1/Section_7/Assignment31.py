'''
@author: SOURABH GUPTA
'''
'''
Write a Python program to:
1.read a ﬁle.
2.add backslash (\) before every double quote in the ﬁle contents.
3.write it to another ﬁle in the same folder.
4.print the contents of both the ﬁles.
'''
f = open("TestFile1.txt","r")
sentence = f.read()

result = open("TestFile2.txt","w")
for i in range(0,sentence.__len__()):
    if sentence[i] == '"':
        result.write('\\"')
    else:
        result.write(sentence[i])
