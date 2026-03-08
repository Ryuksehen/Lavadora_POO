import os
from datetime import datetime
from openpyxl import Workbook, load_workbook


class Reportes:

    CARPETA = "reportes"

    @staticmethod
    def crear_carpeta():

        if not os.path.exists(Reportes.CARPETA):
            os.makedirs(Reportes.CARPETA)

    # FACTURA CLIENTE
    @staticmethod
    def generar_factura_txt(datos):

        Reportes.crear_carpeta()

        archivo = os.path.join(Reportes.CARPETA, "factura.txt")

        with open(archivo, "w", encoding="utf-8") as f:

            f.write("========== LAVA SMART ==========\n")
            f.write("         COMPROBANTE\n\n")

            f.write(f"Cliente: {datos['cliente']}\n")
            f.write(f"Fecha: {datos['fecha']}\n\n")

            f.write(f"Kilos lavados: {datos['kilos']}\n")
            f.write(f"Tipo de prenda: {datos['tipo_ropa']}\n")
            f.write(f"Método de lavado: {datos['metodo']}\n\n")

            f.write(f"Costo por kilo: ${datos['precio_kilo']}\n")
            f.write(f"Costo sin IVA: ${datos['costo_base']}\n")

            if datos["recargo"] > 0:
                f.write(f"Recargo prenda especial (5%): ${datos['recargo']}\n")

            f.write(f"IVA (19%): ${datos['iva']}\n\n")

            f.write(f"TOTAL A PAGAR: ${datos['total']}\n\n")

            f.write("Gracias por usar Lava Smart\n")

        print("✔ factura.txt generada")

    # REPORTE ADMINISTRADOR
    @staticmethod
    def generar_excel(datos):

        Reportes.crear_carpeta()

        archivo = os.path.join(Reportes.CARPETA, "reporte_admin.xlsx")

        if os.path.exists(archivo):

            wb = load_workbook(archivo)
            ws = wb.active

        else:

            wb = Workbook()
            ws = wb.active

            ws.append([
                "Cliente",
                "Fecha",
                "Kilos",
                "Tipo ropa",
                "Metodo",
                "Costo base",
                "IVA",
                "Total",
                "Ganancia",
                "Costo energia"
            ])

        ws.append([
            datos["cliente"],
            datos["fecha"],
            datos["kilos"],
            datos["tipo_ropa"],
            datos["metodo"],
            datos["costo_base"],
            datos["iva"],
            datos["total"],
            datos["ganancia"],
            datos["energia"]
        ])

        wb.save(archivo)

        print("✔ reporte_admin.xlsx actualizado")