

# -*- coding: utf-8 -*-
"""
Created on Fri May 31 11:50:54 2019

@author:
Pablo La Grutta
pablo.lg@hotmail.com.ar

"""

import tkinter as tk
from tkinter import ttk, StringVar,scrolledtext as st
from tkinter.ttk import Style
from tkinter.filedialog import askopenfilename, askdirectory
from tkinter.messagebox import showinfo

import datetime
import os

import pandas as pd
import sys, os
if getattr(sys, 'frozen', False):
    # If the application is run as a bundle, the pyInstaller bootloader
    # extends the sys module by a flag frozen=True and sets the app 
    # path into variable _MEIPASS'.
    application_path = sys._MEIPASS
    print('application_path de Py', application_path)
else:
    application_path = os.path.dirname(os.path.abspath(__file__))
    

class GUI(tk.Tk):
    
   def __init__(self, window): 
               
        self.path_resultados = ''
        self.input_text_resultados= ''  
        etiq_bt1 = "Archivo u2020"
        etiq_bt2 = "Descargar en..."
        etiq_bt3 = "Resultados"
        window.title("Huawei RET Checker 1.1")
        window.config(bg='#321899')
        window.resizable(0, 0) 
        window.geometry("800x300")  #ancho largo
           
        style = Style() 
        style.configure('W.TButton', font =('calibri', 10, 'bold', 'underline'), background = "orange", foreground = 'blue') 
               
        ttk.Button(window, text = etiq_bt1,style = 'W.TButton', command = lambda: self.set_path_log()).grid(row = 0) 
        self.scrolledtext0=st.ScrolledText(window, width=80, height=2)
        self.scrolledtext0.grid(column=1,row=0, padx=0, pady=10)

        ttk.Button(window, text = etiq_bt2, style = 'W.TButton',command = lambda: self.set_path_descarga()).grid(row = 4) 
        self.scrolledtext1=st.ScrolledText(window, width=80, height=2)
        self.scrolledtext1.grid(column=1,row=4, padx=0, pady=10)
        ttk.Button(window, text = etiq_bt3, style = 'W.TButton',command = lambda: self.Proceso1()).grid(row = 6) 

             
    def Proceso1(self):  
        ##-- consultar por nombres de cabeceras; depende las que tenga elijo un algoritmo u otro
        ## nombres de LST/DSP RETSUBUNIT: Device No.  Device Name          Subunit No.  Subunit Name  Online Status  Actual Tilt(0.1degree)  Actual Sector ID  RET Configuration Data File Name  Configuration Data File Load Time
        ## nombres de LST/DSP RET
        ## nombrs de LST/DSP RETPORT
        ## nombre de LST/DSP ANTENNAPORT
        ## nombres de SCN ALD
        ## nombres de DSP RETDEVICEDATA
        lista_etiq_ret = ["G850_H1","G850_H2","G850_H3","G1900_G1","G1900_G2","G1900_G3","G850/U850_HV1","G850/U850_HV2","G850/U850_HV3","G1900/U1900_GU1","G1900/U1900_GU2","G1900/U1900_GU3","G850/L700_HN1","G850/L700_HN2","G850/L700_HN3","G1900/L1900_GM1","G1900/L1900_GM2","G1900/L1900_GM3","G1900/LAWS_GL1","G1900/LAWS_GL1","G1900/LAWS_GL2","G1900/LAWS_GL2","G1900/LAWS_GL3","G1900/LAWS_GL3","G1900/U1900/LAWS_GUL1","G1900/U1900/LAWS_GUL1","G1900/U1900/LAWS_GUL2","G1900/U1900/LAWS_GUL2","G1900/U1900/LAWS_GUL3","G1900/U1900/LAWS_GUL3","G1900/L1900/LAWS_GML1","G1900/L1900/LAWS_GML1","G1900/L1900/LAWS_GML2","G1900/L1900/LAWS_GML2","G1900/L1900/LAWS_GML3","G1900/L1900/LAWS_GML3","G850/U850/L700_HVN1","G850/U850/L700_HVN2","G850/U850/L700_HVN3","U850_V1","U850_V2","U850_V3","U850_V4","U850_V5","U850_V6","U1900_U1","U1900_U2","U1900_U3","U1900_U4","U1900_U5","U1900_U6","U850/L700_VN1","U850/L700_VN2","U850/L700_VN3","L1900/LAWS_ML1","L1900/LAWS_ML2","L1900/LAWS_ML3","L1900/LAWS_ML4","L1900/LAWS_ML5","L1900/LAWS_ML6","U1900/LAWS_UL1","U1900/LAWS_UL1","U1900/LAWS_UL2","U1900/LAWS_UL2","U1900/LAWS_UL3","U1900/LAWS_UL3","L700_N1","L700_N2","L700_N3","L1900_M1","L1900_M2","L1900_M3","L1900_M4","L1900_M5","L1900_M6","LAWS_L1","LAWS_L1","LAWS_L2","LAWS_L2","LAWS_L3","LAWS_L3","L2600_F1","L2600_F1","L2600_F2","L2600_F2","L2600_F3","L2600_F3","L1900/LAWS_ML1","L1900/LAWS_ML1","L1900/LAWS_ML2","L1900/LAWS_ML2","L1900/LAWS_ML3","L1900/LAWS_ML3","LAWS/L2600_LF1","LAWS/L2600_LF1","LAWS/L2600_LF2","LAWS/L2600_LF2","LAWS/L2600_LF3","LAWS/L2600_LF3","G850_HG","G850_HH","G850_HI","G1900_GG","G1900_GH","G1900_GI","G850/U850_HVG","G850/U850_HVH","G850/U850_HVI","G1900/U1900_GUG","G1900/U1900_GUH","G1900/U1900_GUI","G850/L700_HNG","G850/L700_HNH","G850/L700_HNI","G1900/LAWS_GLG","G1900/LAWS_GLH","G1900/LAWS_GLI","G850/U850/L700_HVNG","G850/U850/L700_HVNH","G850/U850/L700_HVNI","G1900/U1900/LAWS_GULG","G1900/U1900/LAWS_GULH","G1900/U1900/LAWS_GULI","G1900/L1900/LAWS_GMLG","G1900/L1900/LAWS_GMLH","G1900/L1900/LAWS_GMLI","U850_VG","U850_VH","U850_VI","U850_VJ","U850_VK","U850_VL","U1900_UG","U1900_UH","U1900_UI","U1900_UJ","U1900_UK","U1900_UL","U850/L700_VNG","U850/L700_VNH","U850/L700_VNI","U1900/LAWS_ULG","U1900/LAWS_ULH","U1900/LAWS_ULI","L700_NG","L700_NH","L700_NI","L1900_MG","L1900_MH","L1900_MI","L1900_MJ","L1900_MK","L1900_ML","LAWS_LG","LAWS_LH","LAWS_LI","L2600_FG","L2600_FH","L2600_FI","L1900/LAWS_MLG","L1900/LAWS_MLH","L1900/LAWS_MLI","LAWS/L2600_LFG","LAWS/L2600_LFH","LAWS/L2600_LFI","G1900/U1900/LAWS/L2600_GUMLF1','G1900/U1900/LAWS/L2600_GUMLF2','G1900/U1900/LAWS/L2600_GUMLF3','G1900/U1900/LAWS/L2600_GUMLF4','G1900/U1900/LAWS/L2600_GUMLF5','G1900/U1900/LAWS/L2600_GUMLF6','G1900/U1900/LAWS/L2600_GULF1','G1900/U1900/LAWS/L2600_GULF2','G1900/U1900/LAWS/L2600_GULF3','G1900/U1900/LAWS/L2600_GULF4','G1900/U1900/LAWS/L2600_GULF5','G1900/U1900/LAWS/L2600_GULF6"]    


        delStrings = [r'RET','--+',r'O&M',r'Report',r'Command',r'===+',r'Number']
        df = self.df
        df = df[~df['raw'].str.contains(('|'.join(delStrings)))].reset_index(drop=True)
        print("df post quita de cosas feas\n",df)
        """"raw	del	name	Device No.	Device Name	Subunit No.	Online Status	Actual Tilt(0.1degree)	cmp_naming"""

        df['Device No.']= df['raw'].str.split(r'\s+\s',n=6,expand=True)[0]  #--3 6 7 8 
        df['sectorID']= df['raw'].str.split(r'\s+\s',n=6,expand=True)[1]
        df['Subunit No.']= df['raw'].str.split(r'\s+\s',n=6,expand=True)[2]
        df['Device Name']= df['raw'].str.split(r'\s+\s',n=6,expand=True)[3] 
        df['name'] = df['raw'].str.split(r'\s+:+\s',n=6,expand=True)[1]
        df['Online Status']= df['raw'].str.split(r'\s+\s',n=6,expand=True)[4] 
        df['Actual Tilt(0.1degree)']= df['raw'].str.split(r'\s+\s',n=6,expand=True)[5]
        df['cmp_naming'] = df['Device Name'].apply(lambda x: x in lista_etiq_ret)
   

        inicioTabla = (df['raw'].str.contains('AVAILABLE')).idxmax()
        df_falla = df.iloc[0:inicioTabla]
        df_ret = df.iloc[inicioTabla+1:]       
        df_ret['name'].replace(to_replace=None, method='ffill',inplace=True)

##----REPORTE----##

        ct = str(datetime.datetime.now() ).replace(' ','_').replace(':','').replace('.','')[0:17]
        with pd.ExcelWriter(self.path_res + '/'+ self.path_logSep[-1][0:-4] + '_Resultado_' + ct + '.xlsx') as writer:  # el argumento de ExcelWriter es el path al archivo, ahi tengo que cargar el path deseado

            df.to_excel(writer,sheet_name='Original',index=False)
            df_falla.to_excel(writer,sheet_name='Sitios en falla',index=False) 
            df_ret.to_excel(writer,sheet_name='Sitios con RET',index=False) 
        print(showinfo("Resultados", "Resultados listos!\nCargue nuevos CSV o cierre el programa.")
        gui.__init__(window)

    def set_path_log(self):
        self.path_log = askopenfilename( filetypes = [("Archivo u2020","*.txt"),("Todos los archivos","*.*")], title = "Seleccionar archivo u2020")
        print('path_log',self.path_log)
        self.path_logSep = str(self.path_log).split('/')
        self.scrolledtext0.insert("1.0", self.path_logSep[-1])
        self.df= pd.read_csv(self.path_log, header=None) #  , utf-16, mbcs,chardet, utf-8, chardet
        self.df.dropna(inplace=True)
        self.df.rename(columns={0:'raw'},inplace=True)
        print('df original',self.df,self.df.columns)

    def set_path_descarga(self):
        self.path_res = askdirectory( )
        print('path_res',self.path_res)
        self.scrolledtext1.insert("1.0",self.path_res)


if __name__ == '__main__':
    window = tk.Tk()
    gui = GUI(window)
    window.mainloop()
 





       

    
    
