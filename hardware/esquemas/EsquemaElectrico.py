from graphviz import Digraph

# flujo de funciones
flow_chart = Digraph(format="png", engine="dot")

# nodos para hardware
flow_chart.node("ESP32", "ESP32\n(Controlador principal)",
                shape="box", style="filled", color="lightblue")
flow_chart.node("mmWave", "Sensor mmWave\n(Detección lateral)",
                shape="ellipse", style="filled", color="lightyellow")
flow_chart.node("LDR", "Sensor LDR\n(Detección de luz ambiental)",
                shape="ellipse", style="filled", color="lightyellow")
flow_chart.node("Camera", "Cámara Trasera", shape="ellipse",
                style="filled", color="lightyellow")
flow_chart.node("LEDs", "Luces LED\n(Laterales y Ambientales)",
                shape="box", style="filled", color="lightgreen")
flow_chart.node("Relays", "Relés de Potencia",
                shape="parallelogram", style="filled", color="lightgrey")
flow_chart.node("Display", "Pantalla\n(Interfaz visual)",
                shape="box", style="filled", color="lightgreen")

# nodos para software
flow_chart.node("DataProcessing", "Procesamiento\n(OpenCV & Lógica)",
                shape="oval", style="filled", color="lightcoral")
flow_chart.node("ControlLogic", "Lógica de Control\n(ESP32 GPIO)",
                shape="oval", style="filled", color="lightcoral")

# Conexiones de hardware
flow_chart.edges([
    ("mmWave", "ESP32"),
    ("LDR", "ESP32"),
    ("Camera", "DataProcessing"),
    ("ESP32", "LEDs"),
    ("ESP32", "Relays"),
    ("Relays", "LEDs"),
    ("DataProcessing", "Display"),
])

# Conexiones de software
flow_chart.edges([
    ("ESP32", "ControlLogic"),
    ("ControlLogic", "Relays"),
])
