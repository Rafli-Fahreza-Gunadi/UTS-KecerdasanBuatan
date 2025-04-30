def identifikasi_hama(gejala):
    if 'daun menguning' in gejala:
        return "Kemungkinan hama: Kutu Daun"
    elif 'bercak hitam' in gejala:
        return "Kemungkinan hama: Jamur"
    elif 'daun berlubang' in gejala:
        return "Kemungkinan hama: Ulat"
    elif 'tanaman layu' in gejala:
        return "Kemungkinan hama: Penyakit Busuk"
    else:
        return "Gejala tidak dikenali"

# Contoh penggunaan
gejala_input = ['daun menguning', 'bercak hitam']
hasil = identifikasi_hama(gejala_input)
print(hasil)