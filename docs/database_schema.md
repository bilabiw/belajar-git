# Skema Database

  ## Tabel: users
  | Kolom       | Tipe Data    | Keterangan              |
  |-------------|--------------|-------------------------|
  | id          | INT (PK)     | Primary key, auto increment |
  | username    | VARCHAR(50)  | Nama pengguna, unik     |
  | email       | VARCHAR(100) | Email, unik             |
  | password    | VARCHAR(255) | Password terenkripsi    |
  | created_at  | TIMESTAMP    | Waktu registrasi        |

  ## Tabel: profiles
  | Kolom       | Tipe Data    | Keterangan              |
  |-------------|--------------|-------------------------|
  | id          | INT (PK)     | Primary key             |
  | user_id     | INT (FK)     | Relasi ke tabel users   |
  | avatar_url  | VARCHAR(255) | Link foto profil        |
  | bio         | TEXT         | Deskripsi diri          |
