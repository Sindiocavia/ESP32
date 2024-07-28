#TECHNICAL ASSIGNMENT 1
Tugas ini menggunakan ESP32 yang terhubung dengan sensor DHT11 untuk mengukur kelembapan dan data yang terdeteksi akan dikirim ke server Flask 

## Komponen

1. **ESP32** - Mikrokontroler yang digunakan untuk membaca data dari sensor DHT11 dan mengirimkannya ke server Flask.
2. **Sensor DHT11** - Digunakan untuk mengukur kelembapan.
3. **Server Flask** - Server berbasis Python yang digunakan untuk menerima dan memproses data dari ESP32.

## Isi Repository

- `LembapFlask.py` - File Python yang berisi kode server Flask untuk menangani permintaan POST dan GET.
- `DHT11Kelembapan.ino` - File Arduino yang berisi kode untuk membaca data kelembapan dari sensor DHT11 dan mengirimkannya ke server Flask.


### Perangkat Lunak

- Arduino IDE dengan dukungan ESP32
- Python 3.x
- Flask (dapat diinstal melalui `pip install flask`)


