import reader 

r = reader.Reader('test.bz2')
print(r.read())
r.close()
r = reader.Reader('test.gz')
print(r.read()) 
r.close()