print("Start")
print("Buat kopi")
print("Masak air dan nyalakan kompor")
print("Siapkan gelas")
print("Ambil gula satu sendok teh")
print("Matikan kompor")
print("Tuang dan aduk")
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('buatkopi2.html')

if __name__ == '__main__':
    app.run(debug=True)

# Pilih bubuk
bubuk = "kopi"  # bisa diubah jadi "kopi","jahe", "teh", atau "susu"

if bubuk == "teh":
    print("Ambil bubuk teh")
elif bubuk == "jahe":
    print("Ambil bubuk jahe")
elif bubuk == "susu":
    print("Ambil bubuk susu")
elif bubuk == "kopi":
    print("Ambil bubuk kopi")

# Pakai es atau tidak
pakai_es = True
if pakai_es:
    print("Pakai es batu")
else:
    print("Tidak pakai es batu")

print("Sajikan")

print("Selesai")
print("Terima kasih telah membuat kopi")
