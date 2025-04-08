import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class Interfaz:
    def __init__(self, root, sensor):
        self.root = root
        self.sensor = sensor
        self.umbral = 0
        self.historial = []

        self.root.title("Panel de Monitoreo Ambiental")
        self.root.configure(bg="#edf2fb")
        self.root.resizable(False, False)

        ancho_ventana = 500
        alto_ventana = 400
        pantalla_ancho = self.root.winfo_screenwidth()
        pantalla_alto = self.root.winfo_screenheight()
        pos_x = int((pantalla_ancho / 2) - (ancho_ventana / 2))
        pos_y = int((pantalla_alto / 2) - (alto_ventana / 2))
        self.root.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")

        # style ttk
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TLabel", font=("Verdana", 11), background="#edf2fb")
        style.configure("Custom.TButton", font=("Verdana", 10), padding=6, background="#4da6ff", foreground="white")
        style.map("Custom.TButton", background=[('active', '#3399ff')])
        style.configure("Custom.TEntry", fieldbackground="white", background="white", foreground="black")

        self.titulo = ttk.Label(root, text="Panel de Monitoreo de Temperatura y Humedad", font=("Verdana", 13, "bold"))
        self.titulo.pack(pady=10)

        # temperatura y humedad
        self.card = tk.Frame(root, bg="white", highlightbackground="#ccc", highlightthickness=1)
        self.card.pack(padx=20, pady=5, fill=tk.X)

        self.lbl_temp = tk.Label(self.card, text="Temperatura: -- °C", font=("Verdana", 11), bg="white", fg="black")
        self.lbl_temp.pack(pady=8)

        self.lbl_hum = tk.Label(self.card, text="Humedad: -- %", font=("Verdana", 11), bg="white", fg="black")
        self.lbl_hum.pack(pady=8)

        # entry del umbral
        self.frame_umbral = tk.Frame(root, bg="#edf2fb")
        self.frame_umbral.pack(pady=15)

        self.lbl_umbral = tk.Label(self.frame_umbral, text="Umbral de temperatura:", font=("Verdana", 12), bg="#edf2fb")
        self.lbl_umbral.grid(row=0, column=0, padx=5)

        self.entry_umbral = ttk.Entry(self.frame_umbral, width=10, style="Custom.TEntry")
        self.entry_umbral.grid(row=0, column=1, padx=5)

        self.btn_confirmar = ttk.Button(self.frame_umbral, text="Aplicar", command=self.actualizar_umbral, style="Custom.TButton")
        self.btn_confirmar.grid(row=0, column=2, padx=5)

        # estado
        self.lbl_estado = tk.Label(root, text="Estado: Normal", bg="#d0f0c0", font=("Verdana", 11, "bold"), fg="#2d572c")
        self.lbl_estado.pack(fill=tk.X, pady=10, padx=20, ipady=6)

        # historial
        self.lbl_historial = tk.Label(root, text="Historial de lecturas:\n", justify="left", anchor="w", font=("Verdana", 9), bg="#edf2fb")
        self.lbl_historial.pack(fill=tk.X, padx=20)

        self.actualizar_datos()

    def actualizar_umbral(self):
        try:
            self.umbral = float(self.entry_umbral.get())
        except ValueError:
            messagebox.showerror("Error", "Ingrese un valor numérico válido")
        else:
            messagebox.showinfo("Confirmación", f"Umbral actualizado a {self.umbral} °C")

    def actualizar_datos(self):
        temp = self.sensor.temperatura
        hum = self.sensor.humedad

        self.lbl_temp.config(text=f"Temperatura: {temp:.2f} °C")
        self.lbl_hum.config(text=f"Humedad: {hum:.2f} %")

        if temp > self.umbral:
            estado = "Alerta"
            self.lbl_estado.config(text="Estado: Alerta", bg="#f8d7da", fg="#b71c1c")
        else:
            estado = "Normal"
            self.lbl_estado.config(text="Estado: Normal", bg="#d0f0c0", fg="#2d572c")

        # Guardar en historial
        self.historial.append((temp, hum, estado))
        if len(self.historial) > 10:
            self.historial.pop(0)

        # Mostrar historial
        texto_historial = "Historial de lecturas:\n"
        for t, h, e in self.historial:
            texto_historial += f"Temp: {t:.1f} °C | Hum: {h:.1f} % | Estado: {e}\n"
        self.lbl_historial.config(text=texto_historial)

        self.root.after(2000, self.actualizar_datos)
