# Simulasikan data dari database
  users = [{"id": 1, "name": "Admin"}, {"id": 2, "name": "User"}]

  def get_users():
      return {"status": "success", "data": users}

  def get_user_by_id(user_id):
      user = next((u for u in users if u["id"] == user_id), None)
      if user:
          return {"status": "success", "data": user}
      return {"status": "error", "message": "User tidak ditemukan"}
