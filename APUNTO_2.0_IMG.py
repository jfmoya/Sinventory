import CONF_APUNTO
import tkinter as tk
from tkinter import messagebox
import reporte_global, reporte_ampm, reporte_socio
import correccion_codigo, correccion_cantidad, correccion_ingreso
import carga_socios, respaldo_transacciones


def hello():
    print('hellouu')

class App:
    def __init__(self, master):

        container = tk.Frame(master)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        for F in (RGlob_F, RAmPm_F, RSoc_F, CCod_F, CCant_F, CIngreso_F, CaSoc_F, Res_F, Home_F):
            frame = F(container)
            self.frames[F] = frame


        menubar = tk.Menu(master)
        
        m_reporte = tk.Menu(menubar)
        m_reporte.add_command( label = 'R. Global', command = lambda: self.show_frame(RGlob_F))
        m_reporte.add_command( label = 'R. AM-PM', command = lambda: self.show_frame(RAmPm_F))
        m_reporte.add_command( label = 'R. Socio', command = lambda: self.show_frame(RSoc_F))
        menubar.add_cascade( label = 'Reportes', menu = m_reporte)
        
        m_correccion = tk.Menu(menubar)
        m_correccion.add_command( label = 'C. Codigo', command = lambda: self.show_frame(CCod_F))
        m_correccion.add_command( label = 'C. Cantidad', command = lambda: self.show_frame(CCant_F))
        m_correccion.add_command( label = 'Ingreso Manual', command = lambda: self.show_frame(CIngreso_F))
        menubar.add_cascade( label = 'Correcciones', menu = m_correccion)

        m_carga = tk.Menu(menubar)
        m_carga.add_command( label = 'Carga Socios', command = lambda: self.show_frame(CaSoc_F))
        menubar.add_cascade( label = 'Datos', menu = m_carga)

        menubar.add_command( label = 'Respaldar', command = lambda: self.show_frame(Res_F))
        menubar.add_command( label = 'Inicio', command = lambda: self.show_frame(Home_F))
        
        root.config(menu = menubar)

    def show_frame(self, F):
        frame = self.frames[F]
        frame.tkraise()

    

class RGlob_F:
    def __init__(self, master):
        self.frame = tk.Frame(master)
        self.frame.grid(row=0, column=0, sticky="nsew")
        sframe = reporte_global.RGlob(self.frame)
    def tkraise(self):
        self.frame.tkraise()
        
class RAmPm_F:
    def __init__(self, master):
        self.frame = tk.Frame(master)
        self.frame.grid(row=0, column=0, sticky="nsew")
        sframe = reporte_ampm.RAmPm(self.frame)
    def tkraise(self):
        self.frame.tkraise()

class RSoc_F:
    def __init__(self, master):
        self.frame = tk.Frame(master)
        self.frame.grid(row=0, column=0, sticky="nsew")
        sframe = reporte_socio.RSoc(self.frame)
    def tkraise(self):
        self.frame.tkraise()
#########        
class CCod_F:
    def __init__(self, master):
        self.frame = tk.Frame(master)
        self.frame.grid(row=0, column=0, sticky="nsew")
        sframe = correccion_codigo.CCod(self.frame)
    def tkraise(self):
        self.frame.tkraise()

class CCant_F:
    def __init__(self, master):
        self.frame = tk.Frame(master)
        self.frame.grid(row=0, column=0, sticky="nsew")
        sframe = correccion_cantidad.CCant(self.frame)
    def tkraise(self):
        self.frame.tkraise()

class CIngreso_F:
    def __init__(self, master):
        self.frame = tk.Frame(master)
        self.frame.grid(row=0, column=0, sticky="nsew")
        sframe = correccion_ingreso.CIngreso(self.frame)
    def tkraise(self):
        self.frame.tkraise()
#########        
class CaSoc_F:
    def __init__(self, master):
        self.frame = tk.Frame(master)
        self.frame.grid(row=0, column=0, sticky="nsew")
        sframe = carga_socios.CaSoc(self.frame)
    def tkraise(self):
        self.frame.tkraise()
#########        
class Res_F:
    def __init__(self, master):
        self.frame = tk.Frame(master)
        self.frame.grid(row=0, column=0, sticky="nsew")
        sframe = respaldo_transacciones.Res(self.frame)
    def tkraise(self):
        self.frame.tkraise()
#########        
class Home_F:
    def __init__(self, master):
        self.frame = tk.Frame(master)
        self.frame.grid(row=0, column=0, sticky="nsew")
        label = tk.Label(self.frame, text = "Apunto de PCServ - 0987090445 - J. Moya")
        label.pack()
        try:
            label_2 = tk.Label(self.frame, image = logo)
            label_2.pack()
        except:
            pass
    def tkraise(self):
        self.frame.tkraise()

root = tk.Tk()
root.title("APunto")
try:
    root.iconbitmap(CONF_APUNTO.icon_path)
except:
    pass
try:
    logo = tk.PhotoImage(file=CONF_APUNTO.logo_path)
except:
    pass


app = App(root)

root.mainloop()
try:
    root.destroy()
except:
    pass


##button = tk.Button(root, text = 'Hola', command = root.quit)
##button.pack()
