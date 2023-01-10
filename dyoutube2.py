#!/usr/bin/env python3
import pytube
import webbrowser
import os
import shutil
import subprocess
from tkinter import Tk, Label, Button, Entry, Frame
from moviepy.editor import *



class Aplicacion(Frame):
    def __init__(self, master=None):
        super().__init__(master,width=700,height= 400,cursor="arrow")
        self.master = master
        self.pack()
        self.create_widgets()
        
       
   
    def descargar_single(self):
        url = self.url.get()
        self.yt = pytube.YouTube("{}".format(url))
        self.download = self.yt.streams.filter(progressive=True, file_extension='mp4').first().download("/home/black1/Descargas/pytube")
        

    def descargar_list(self):
        urlist = self.urlist.get()
        self.listarep = pytube.Playlist("{}".format(urlist))

        for video in self.listarep.videos:
            video.streams.first().download("/home/black1/Descargas/pytube")

    def web_youtube(self):
        self.pagina = webbrowser.open_new("http://www.youtube.com")

    def abrir_carpeta_descargas(self):
        self.ruta_carpeta = "/home/black1/Descargas/pytube"
        #self.ruta = os.system(f'nautilus {os.path.realpath(self.ruta_carpeta)}')
        #subprocess.run(['nautilus', os.path.realpath(self.ruta_carpeta)])
        #webbrowser.open(os.path.realpath(self.ruta_carpeta))
        self.proceso = subprocess.Popen(['nautilus', os.path.realpath(self.ruta_carpeta)])
        #self.proceso.kill()


    def conversion_mp3(self):
        #descarga video de youtube
        
        url_mp3 = self.url_mp3.get()
        self.yt = pytube.YouTube(f"{url_mp3}")
        self.ruta_path = "/home/black1/Descargas/pytube/pytubemp3"
        self.download_mp3 = self.yt.streams.first().download(self.ruta_path)

        #listar y elegir archivo mp4

        contenido = os.listdir(self.ruta_path)
        audio_mp4 = ""

        for fichero in contenido:
            if os.path.isfile(os.path.join(self.ruta_path, fichero)) and fichero.endswith('.3gpp'):
                audio_mp4 = str(fichero)

        #crea ruta de audio para ser convertida
        tupla_ruta = (self.ruta_path, audio_mp4)
        ruta_final = "/".join(tupla_ruta)

        #combierte video mp4 a mp3
        clip = VideoFileClip(ruta_final)
        audio_mp3 = audio_mp4.split('.')
        clip.audio.write_audiofile(f"{audio_mp3[0]}.mp3")

        #eliminacion de archivo mp4 y mueve archivo convertido a carpeta de destino

        os.remove(ruta_final)
        ruta_script = os.path.dirname(os.path.abspath(__file__))
        contenido_ruta_actual = os.listdir(ruta_script)

        for fichero in contenido_ruta_actual:
            if os.path.isfile(os.path.join(ruta_script,fichero)) and fichero.endswith('.mp3'):
                audio_definitivo_mp3 = str(fichero)

        shutil.move(audio_definitivo_mp3,f"{self.ruta_path}/{audio_definitivo_mp3}")

    def create_widgets(self):
        #label de url y boton de descargas single
        self.titulo_descarga = Label(self,text="Descargar un video.", bd=2)
        self.primerurl = Label(self,text="Ingrese URL: ",bg="blue")
        self.url = Entry(self,bg="pink")
        self.unboton = Button(self,text="Descargar",command=self.descargar_single)
        
        self.titulo_descarga.place(x=260,y=10)
        self.primerurl.place(x=10, y=40, width=100, height=30)
        self.url.place(x=120, y=40, width=400, height=30)
        self.unboton.place(x=550, y=40, width=80, height=30)

        #label de descarga lista y boton
        self.titulo_descarga_lista = Label(self, text="Descargar lista de video.", bd=3)
        self.seg_url_list= Label(self,text="Ingrese URL: ", bg="blue")
        self.urlist = Entry(self,bg="pink")
        self.dosbuton = Button(self,text="Descargar",command=self.descargar_list)

        self.titulo_descarga_lista.place(x=245, y=90)
        self.seg_url_list.place(x=10, y=120, width=100, height=30)
        self.urlist.place(x=120,y=120, width=400, height=30)
        self.dosbuton.place(x=550,y=120, width=80, height=30)

        #label convertir a mp3
        self.convertir_mp3 = Label(self, text="Convertir video a mp3.", bd=5)
        self.tercer_url = Label(self, text="Ingrese URL: ",bg="blue")
        self.url_mp3 = Entry(self, bg="pink")
        self.tres_buton = Button(self, text="Convertir", command=self.conversion_mp3)

        self.convertir_mp3.place(x=250, y= 170)
        self.tercer_url.place(x=10, y=200, width=100, height=30)
        self.url_mp3.place(x=120, y=200, width=400, height=30)
        self.tres_buton.place(x=550, y=200, width=80, height=30)

        #boton de abrir youtube 
        self.boton_youtube = Button(self, text= "Abrir YouTube", command=self.web_youtube)

        self.boton_youtube.place(x=150, y=300, width=120,height=30)

        #boton abrir carpeta descargas

        self.boton_descargas = Button(self, text = "Abrir descargas", command = self.abrir_carpeta_descargas)

        self.boton_descargas.place(x = 350, y= 300, width=150, height=30)


root = Tk()
root.wm_title("Dyoutube    versión 1.0")
app = Aplicacion(root)
app.mainloop()