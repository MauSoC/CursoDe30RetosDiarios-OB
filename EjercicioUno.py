import pandas as pd
def main():
    #Path del archivo excel
    path = "Correos_Usuarios.xlsx"
    #Lectura del archivo excel
    excelCorr = pd.read_excel(path)
    #Asignamos los valores de la columna correo se asigna como un array
    correo = excelCorr['Correo'].values
    #Ocupamos el metodo set para quitar duplicados
    excelSinDup =list(set(correo))
    print(f"Lista Con datos completos: {correo}\n\n\n Lista sin duplicados{excelSinDup}")


if __name__ == "__main__":
    main()