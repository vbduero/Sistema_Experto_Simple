
#Valentina Bermeo
class SistemaExpertoAuto:
    def __init__(self):
        self.diagnostico = None

    def preguntar(self, texto, opciones=("si", "no")):
  
        while True:
            respuesta = input(texto).strip().lower()
            if respuesta in opciones:
                return respuesta
            print(f"⚠️ Respuesta no válida. Opciones permitidas: {opciones}")

    def iniciar(self):
        print("===============================================")
        print("🚗 Sistema Experto: Diagnóstico de Fallas en Automóvil")
        print("===============================================\n")
        print("Responde las siguientes preguntas con 'si' o 'no'.\n")

        arranca = self.preguntar("¿El auto arranca? (si/no): ")

        if arranca == "no":
            luces = self.preguntar("¿Las luces del tablero encienden? (si/no): ")
            if luces == "no":
                self.diagnostico = "🔋 Posible causa: Batería descargada."
            else:
                self.diagnostico = "⚙️ Posible causa: Fallo en el motor de arranque."
        else:
            se_apaga = self.preguntar("¿El auto se apaga al acelerar? (si/no): ")
            if se_apaga == "si":
                self.diagnostico = "⛽ Posible causa: Problema en el suministro de combustible."
            else:
                humo = self.preguntar("¿El auto tiene humo por el escape? (si/no): ")
                if humo == "si":
                    color = self.preguntar("¿De qué color es el humo? (negro/blanco): ", ("negro", "blanco"))
                    if color == "negro":
                        self.diagnostico = "🌫️ Posible causa: Mezcla rica de combustible."
                    else:
                        self.diagnostico = "💨 Posible causa: Falla en la junta de culata."
                else:
                    self.diagnostico = "✅ No se detectaron fallas conocidas en la base de reglas."

        
        print("\n===============================================")
        print("🔎 Diagnóstico final")
        print(self.diagnostico)
        print("===============================================")


if __name__ == "__main__":
    experto = SistemaExpertoAuto()
    experto.iniciar()