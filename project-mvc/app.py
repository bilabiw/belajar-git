from views.dashboard_component import render_dashboard

  # Simulasi State
  app_state = {"items": [], "is_loading": True}

  def update_state(new_data):
      app_state["items"] = new_data
      app_state["is_loading"] = False

  if __name__ == "__main__":
      # Tampilkan loading state dulu
      print("Loading data...")
      render_dashboard(app_state["items"], is_loading=app_state["is_loading"])

      print("\n--- Setelah data masuk dari Backend ---\n")

      # Simulasi data masuk dari Backend
      mock_data = [
          {"id": 101, "name": "Wilayah Kediri"},
          {"id": 102, "name": "Wilayah Surabaya"}
      ]
      update_state(mock_data)
      render_dashboard(app_state["items"], is_loading=app_state["is_loading"])
