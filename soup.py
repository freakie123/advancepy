from bs4 import BeautifulSoup


 html_doc = """
... <html>
...     </head>
...         <title>hello world</title>
...     </head>
...     <body>
...     <p>I Like Python</p>
...     </body>
... </html>
... """
>>> 
>>> soup = BeautifulSoup(html_doc,'html.parser')
