def setup_input_handlers(window, slider_a, slider_b):
    window.listen()
    window.onkeypress(slider_a.go_up, "w")
    window.onkeypress(slider_a.go_down, "s")
    window.onkeypress(slider_b.go_up, "Up")
    window.onkeypress(slider_b.go_down, "Down")
