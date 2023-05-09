import re

html = '''
<!DOCTYPE html>
<html>
<head>
  <title>Example</title>
</head>
<body>
  <!-- This is a comment -->
  <h1>Welcome to my website</h1>
  <p>Here you can find all kinds of interesting stuff.</p>
  <!-- Another comment -->
</body>
</html>
'''

comments = re.findall(r'<!--(.*?)-->', html, re.DOTALL)
print(comments)
'''
html안의 주석들을 검출하는 코드
'''
