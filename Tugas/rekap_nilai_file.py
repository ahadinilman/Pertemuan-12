def baca_data(nama_file):
    """Membaca dan memvalidasi data nilai dari file teks per baris."""
    data = []
    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for nomor, baris in enumerate(file, start=1):
                baris = baris.strip()
                if not baris:
                    continue  # Lewati baris kosong
                try:
                    nim, teks_nilai = baris.split(",")
                    nilai = float(teks_nilai.strip())
                    data.append((nim.strip(), nilai))
                except (ValueError, IndexError):
                    print(f"[Peringatan] Baris {nomor} tidak valid/dilewati: '{baris}'")
    except FileNotFoundError:
        print(f"[Error] File '{nama_file}' tidak ditemukan.")
        return None
    return data


def tulis_rekap(nama_file, data):
    """Menghitung statistik rekapitulasi nilai dan menuliskannya ke file output."""
    if not data:
        print("Tidak ada data valid untuk direkap.")
        return

    nilai_list = [item[1] for item in data]
    jumlah_valid = len(nilai_list)
    rata_rata = sum(nilai_list) / jumlah_valid
    nilai_min = min(nilai_list)
    nilai_max = max(nilai_list)
    jumlah_lulus = sum(1 for x in nilai_list if x >= 60)

    with open(nama_file, "w", encoding="utf-8") as file:
        file.write(f"Jumlah data valid: {jumlah_valid}\n")
        file.write(f"Rata-rata: {rata_rata:.2f}\n")
        file.write(f"Minimum: {nilai_min:.2f}\n")
        file.write(f"Maksimum: {nilai_max:.2f}\n")
        file.write(f"Jumlah lulus: {jumlah_lulus}\n")


def main():
    input_file = "data/nilai.txt"
    output_file = "data/hasil_rekap.txt"

    print("--- Memulai Pemrosesan Data Nilai ---")
    data = baca_data(input_file)

    if data is not None and len(data) > 0:
        tulis_rekap(output_file, data)
        print(f"[Sukses] Rekap berhasil ditulis ke '{output_file}'.")
    elif data is not None:
        print("[Info] File dibaca tetapi tidak ditemukan data yang valid.")


if __name__ == "__main__":
    main()