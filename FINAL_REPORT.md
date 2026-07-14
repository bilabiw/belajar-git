# Final Report - Kontribusi Individu Proyek Akhir
**Nama:** [LAILA  NABILA RAHMANISA]
**NIM:** [2313020243]
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

## 2. Link Commit Terbaik (Bukti Kontribusi di Repositori Kelompok)
Berikut adalah bukti commit kontribusi kode yang telah saya dorong (*push*) ke repositori kelompok sebagai bagian dari pengembangan sistem:

https://github.com/lievlya/Project-Prediksi-Kemiskinan/commit/3505f17767731c18838e24b353a33811b9bcd851
https://github.com/lievlya/Project-Prediksi-Kemiskinan/commit/13cf4d70518b070df763cf59f7fbd385afee494f
https://github.com/lievlya/Project-Prediksi-Kemiskinan/commit/9fc899007cee34e038ad7879b2e0b8bb486f95f4
https://github.com/lievlya/Project-Prediksi-Kemiskinan/commit/b8c46d7f441bdf2e86a40300e36f5d0427424026
https://github.com/lievlya/Project-Prediksi-Kemiskinan/commit/05823a281c542b651e19e1e8deb82eee60017108
https://github.com/lievlya/Project-Prediksi-Kemiskinan/commit/59deed4b23e5c15ea30fa95fc741b5cda9fb121b
https://github.com/lievlya/Project-Prediksi-Kemiskinan/commit/74baa20a4ac3247220409f5d536d47604d89742c
https://github.com/lievlya/Project-Prediksi-Kemiskinan/commit/f9b2aa5147c9037d885d104ef25a8b42e9d3dd82
https://github.com/lievlya/Project-Prediksi-Kemiskinan/commit/106e5596efe8801519516365518b70d8af49ddeb
https://github.com/lievlya/Project-Prediksi-Kemiskinan/commit/e9fb89048a82ce6b7f4f8793f5e118e97a681b89
https://github.com/lievlya/Project-Prediksi-Kemiskinan/commit/44e5e4c642f3d34b108af67a218f0c202db56365
https://github.com/lievlya/Project-Prediksi-Kemiskinan/commit/52ca896df90c90661f1a795d72efb4048890a216

