# Final Report - Kontribusi Individu Proyek Akhir
**Nama:** [Isi Nama Kamu]
**NIM:** [Isi NIM Kamu]
**Peran:** Backend & DevOps Engineer
**Project:** Prediksi Tingkat Kemiskinan Regional

---

##  1. Ringkasan Kontribusi Spesifik (Minggu 1 - 16)
Selama 16 minggu jalannya proyek, kontribusi utama saya berfokus pada pengembangan arsitektur API Backend menggunakan Flask, integrasi model Machine Learning, manajemen database PostgreSQL, serta otomatisasi deployment menggunakan Docker Multi-Container.

### **Kontribusi Utama:**
* **Arsitektur Backend (Flask):** Membangun endpoint API `/predict` untuk memproses input data spasial/regional dan mengembalikan hasil klasifikasi kemiskinan secara real-time.
* **Integrasi Model Machine Learning V2:** Mengintegrasikan model *Random Forest*, *Label Encoders*, dan *Scaler* ke dalam sistem backend agar siap dikonsumsi oleh Frontend.
* **Containerization (Docker & Docker Compose):** Menyusun `Dockerfile.backend`, `Dockerfile.frontend`, dan mengonfigurasi `docker-compose.yml` untuk menyatukan ekosistem aplikasi (Database, BE, dan FE) sehingga dapat dijalankan dengan satu perintah.
* **Otomatisasi Deployment:** Membuat shell script `deploy.sh` untuk melakukan rolling update container dan mengintegrasikannya dengan GitHub Container Registry (GHCR) guna keperluan CI/CD kelompok.
* **Troubleshooting & Git Management:** Menyelesaikan isu versioning (seperti conflict merge branch development dan inkonsistensi modul Numpy/Scikit-Learn pada Docker).

---

## 🔗 2. Link Commit Terbaik (Bukti Kontribusi di Repositori Kelompok)
Berikut adalah bukti commit kontribusi kode yang telah saya dorong (*push*) ke repositori kelompok sebagai bagian dari pengembangan sistem:

1. **Commit Integrasi Backend & Docker Multi-Container:** 
   `[feat: integrasi backend flask, multi-dockerfile, dan model ml v2]`
   👉 *[Ganti teks ini dengan link commit merge bersih kamu yang ada di GitHub]*
2. **Commit Resolusi Konflik Git & Sinkronisasi Branch:** 
   `[fix: resolve merge conflicts with development branch]`
   👉 *[Ganti teks ini dengan link commit fix conflict kamu]*
3. **Commit Hotfix Perbaikan Versi Library & Deprecations:**
   `[fix: upgrade library version for numpy core and streamlit rerun hotfix]`
   👉 *[Ganti teks ini dengan link commit perbaikan terakhir]*

---

## 📸 3. Lampiran Dokumentasi Sistem
*(Opsional: Anda bisa memasukkan screenshot hasil akhir web yang berhasil berjalan di localhost:8501 dan log sukses rolling update di sini)*
