from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Veritabanı bağlantısı
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Kullanıcı adınızı girin
        password="Halil____5455",
       database="kullanici_db"
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/kaydet', methods=['POST'])
def kaydet():
    if request.method == 'POST':
        ad = request.form['ad']
        soyad = request.form['soyad']
        email = request.form['email']
        
        # Veritabanına bağlan
        connection = get_db_connection()
        cursor = connection.cursor()
        
        # Veriyi ekle
        sql = "INSERT INTO kullanicilar (ad, soyad, email) VALUES (%s, %s, %s)"
        cursor.execute(sql, (ad, soyad, email))
        connection.commit()
        
        # Bağlantıyı kapat
        cursor.close()
        connection.close()
        
        return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
