import os

  DB_CONFIG = {
      "host": os.environ.get("DB_HOST", "localhost"),
      "name": os.environ.get("DB_NAME", "prediksi_kemiskinan"),
      "password": os.environ.get("DB_PASSWORD", ""),
      "api_key": os.environ.get("API_KEY", ""),
  }

  def get_db_connection():
      """
      Fungsi untuk mendapatkan koneksi database.
      Kredensial diambil dari environment variable, bukan hardcoded.
      """
      print(f"Connecting to database: {DB_CONFIG['name']}")
      # Di sini nanti diganti dengan koneksi database sungguhan
      return DB_CONFIG
