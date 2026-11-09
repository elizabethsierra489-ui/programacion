#Actividad 3: Sistema de Acceso de la Baticueva 
#Para proteger los secretos de Batman, el sistema informático de la Baticueva necesita almacenar 
#datos confidenciales que nadie más pueda alterar directamente desde fuera del sistema. 

#• Requerimientos: 
#1. Crea la clase BatcuevaSystem con los atributos privados __mando_central_pass 
#(contraseña) y __nivel_alerta (por ejemplo: "Verde", "Amarillo", "Rojo"). 
##2. Implementa un método getter obtener_alerta() para consultar el nivel de alerta actual. 
#3. Implementa un método setter cambiar_alerta(nueva_alerta, clave_ingresada) que solo permita cambiar el nivel de alerta
#si la clave_ingresada coincide exactamente con la contraseña guardada en __mando_central_pass. 
#4. Intenta cambiar la alerta pasando una clave correcta y luego una incorrecta para probar la seguridad. 
class BatcuevaSystem:
    def __init__(self, password: str, nivel_inicial: str):
        self._mando_central_pass = password
        self._nivel_alerta = nivel_inicial

    # Getter para consultar el nivel de alerta
    def obtener_alerta(self) -> str:
        return self._nivel_alerta

    # Setter para cambiar el nivel de alerta con validación de clave
    def cambiar_alerta(self, nueva_alerta: str, clave_ingresada: str):
        if clave_ingresada == self._mando_central_pass:
            self._nivel_alerta = nueva_alerta
            print(f"Acceso concedido. Nivel de alerta actualizado a: {self._nivel_alerta}")
        else:
            print("Acceso denegado: Contraseña incorrecta. El nivel de alerta no cambió.")

# Pruebas del sistema de la Baticueva
baticueva = BatcuevaSystem("batisecreto123", "Verde")

print(f"Nivel de alerta actual: {baticueva.obtener_alerta()}")

# Intento fallido con clave incorrecta
baticueva.cambiar_alerta("Rojo", "clave_falsa")

# Intento exitoso con clave correcta
baticueva.cambiar_alerta("Rojo", "batisecreto123")
print(f"Nivel de alerta actualizado: {baticueva.obtener_alerta()}")