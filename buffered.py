import io
with open ("test.txt","wb") as f:
    file=io.BufferedWriter(f)

    file.write(b"this is my first line\n")
    file.write(b"this is my second line\n")
    file.flush()

with open("test.txt","rb") as f:
    file=io.BufferedReader(f)
    a=file.read(5)
    print(a)
