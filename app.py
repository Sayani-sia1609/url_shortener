from flask import Flask, request, redirect, render_template
import re
import random
import mysql.connector
app=Flask(__name__)

length=10

def generate_short_code(length):
               
               characters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
               short_code=''.join(random.choices(characters,k=length))
               return short_code


def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Sayani@16',
        database='url_shortener'
    )
    return connection

url_pattern = re.compile(               
            r'^(https?:\/\/)?'  # http:// or https://
            r'(([A-Za-z0-9-]+\.)+[A-Za-z]{2,6})'  # domain...
            r'(:\d+)?'  # optional port
            r'(\/[A-Za-z0-9\-._~:\/?#[\]@!$&\'()*+,;=]*)?$'  # path
        )
def is_valid_url(url):
    return re.match(url_pattern, url) is not None

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        url_received=request.form["url"]
        
        if not url_received:
           return render_template('index.html', error="Please enter a URL.")
        
        if not is_valid_url(url_received):
           return render_template('index.html', error="Invalid URL. Please enter a valid URL.")
        else:
          
           short_code=generate_short_code(length)
           
           conn = get_db_connection()
           cursor = conn.cursor()
           try:
                
                cursor.execute("INSERT INTO urls (long_url, short_url) VALUES (%s, %s)", (url_received, short_code))
                conn.commit()
                
           except mysql.connector.Error:
                cursor.close()
                conn.close()
                return render_template('index.html', error="Attempt failed. Please try again.")
           cursor.close()
           conn.close()
           short_url = f"http://localhost:5000/{short_code}"
           return render_template('index.html', short_url=short_url, original_url=url_received)
        
    # GET request return
    return render_template("index.html")

    

@app.route('/<short_code>')
def redirect_to_url(short_code):
     conn=get_db_connection()
     cursor=conn.cursor()
     cursor.execute("SELECT long_url FROM urls WHERE short_url=%s",(short_code,))
     row=cursor.fetchone()
     cursor.close()
     conn.close()
     if row:
          long_url=row[0]
          return redirect(long_url)
     else:
            return render_template('index.html', error="URL not found.")

if __name__ == '__main__':
    app.run(debug=True)