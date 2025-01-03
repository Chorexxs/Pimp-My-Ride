# Pimp-My-Ride

Proyecto en el que voy a tratar de modernizar mi SEAT del 2004 o cargármelo en el intento

## Say whaaaaaaaaaaaaaaaaaaaaaaaaat?

# La idea:

Proyecto en Python en el cual voy a crear una app para poder automatizar algunas de las funciones que tiene el coche y también poder agregarle funciones que no tiene.

Dentro de esas funciones estarían:

Añadir luces a los retrovisores que cuando algún coche me esté adelantando en la carretera, que se enciendan para notificármelo.

Pantalla para poder ver una cámara trasera del coche y que me indique cómo retroceder (que tenga guías virtuales que me enseñe hacia dónde iría mi coche según la posición del volante).

Que la vista de retroceso sólo se active cuando la marcha atrás esté puesta.

Que las puertas del coche se abran automáticamente cuando las llaves del coche estén cerca (1 metro o así) y que cuando las llaves se alejen lo suficiente (3 metros o así) el coche se enllave automáticamente. Aunque yo también pueda hacer esto de manera manual (tanto abrirlo como cerrarlo). Y que esto se pueda hacer con mi móvil (así como los Teslas).

Que dentro de la app se pueda usar Google maps para cuando lo necesite.

Poder usar comando de voz para poder interactuar con la app, para poder tener las dos manos en el volante.

Poder conectar mi teléfono al coche para poder usar todas las herramientas también desde mi teléfono.

Poder hacer y contestar llamadas.

Que las luces del coche se enciendan automáticamente cuando esté anocheciendo o cuando vaya por tramos de vía en los cuales hay poca iluminación (tales como túneles, pasos bajos, etc).

Ponerle luces de ambiente al coche (de diferente colores) y poder controlarlas a través de la app.

Modo centinela. Cuando el coche esté aparcado y enllavado, que haya una opción desde la app de activar este modo, y que las cámaras del coche graben en todo momento para evitar algún robo o similar. Las grabaciones se eliminarán a las 72 horas. a menos que quiera guardar una en específico.

---

Aquí tienes un roadmap actualizado y detallado, que incorpora las mejoras y la resolución de contradicciones identificadas:

---

## **📅 Roadmap**

### **Fase 1: Planificación y Requisitos**

#### 1.1. **Definir objetivos y alcance**

- [ ] Documentar los objetivos clave:
  - Automatización y modernización de funciones del coche.
  - Integración de hardware y software en una app móvil.
- [ ] Identificar limitaciones (presupuesto, disponibilidad de componentes, tiempo de desarrollo).

#### 1.2. **Lista de hardware**

- **Microcontrolador**: Raspberry Pi (control central) y ESP32 (control específico para BLE y luces).
- **Sensores**:
  - mmWave o LIDAR para detección de adelantamientos.
  - LDR (sensor de luz ambiental) para luces automáticas.
  - Cámara de visión trasera (compatible con OpenCV).
  - Sensores PIR o de vibración para el modo centinela.
- **Actuadores**:
  - LEDs RGB para luces de ambiente.
  - Servos o actuadores eléctricos para apertura/cierre de puertas.
- **Módulos de comunicación**:
  - BLE para interacción con el móvil.
  - GPS para Google Maps.
  - Wi-Fi para conexión remota y notificaciones.
- **Otros componentes**:
  - Pantalla táctil para la app en el coche.
  - Fuente de alimentación estable con batería auxiliar.

#### 1.3. **Lista de software**

- Python para lógica principal y comunicación con hardware.
- Flask/Django para el backend.
- React Native/Kivy para el frontend de la app.
- OpenCV para procesamiento de imágenes (guías virtuales, modo centinela).
- API de Google Maps para navegación.
- SpeechRecognition para comandos de voz.
- Integración con Firebase para notificaciones push.

#### 1.4. **Diseño inicial**

- Crear un esquema eléctrico del coche con conexiones de hardware.
- Dibujar un flujo de funciones:
  - Qué hardware controla cada funcionalidad.
  - Cómo interactúa el software con los dispositivos.

---

### **Fase 2: Desarrollo de Funciones Básicas**

#### 2.1. **Luces en retrovisores para adelantamientos**

- **Hardware**:
  - Instalar sensores mmWave en los laterales traseros.
  - Conectar LEDs a un ESP32 para control independiente.
- **Software**:
  - Programar el sensor para detectar objetos en movimiento en un rango definido.
  - Activar LEDs cuando un coche esté en la zona de adelantamiento.
- **Pruebas**:
  - Validar el rango de detección en carretera.

#### 2.2. **Luces automáticas según iluminación**

- **Hardware**:
  - Instalar un LDR cerca del parabrisas.
  - Conectar el sensor a un microcontrolador.
- **Software**:
  - Programar la activación/desactivación de luces según niveles de luz ambiental.
- **Pruebas**:
  - Simular condiciones de túneles, día/noche.

#### 2.3. **Cámara trasera con guías virtuales**

- **Hardware**:
  - Instalar cámara trasera y pantalla.
  - Añadir un sensor de posición del volante (potenciómetro o giroscopio).
- **Software**:
  - Capturar imágenes de la cámara con OpenCV.
  - Superponer guías virtuales dinámicas según el ángulo del volante.
  - Activar la cámara cuando se detecte la marcha atrás (usar sensor de cambio de marcha o microinterruptor).
- **Pruebas**:
  - Validar la precisión de las guías y el funcionamiento automático.

---

### **Fase 3: Desarrollo de Funciones Avanzadas**

#### 3.1. **Apertura y cierre automáticos**

- **Hardware**:
  - Instalar un módulo BLE para detección de proximidad.
  - Conectar actuadores eléctricos a las cerraduras.
- **Software**:
  - Configurar BLE para detectar la distancia del móvil.
  - Programar acciones automáticas según el rango (1 m para apertura, 3 m para cierre).
  - Añadir un botón manual en la app para control remoto.
- **Pruebas**:
  - Validar apertura/cierre en diferentes entornos y obstáculos.

#### 3.2. **Luces de ambiente personalizables**

- **Hardware**:
  - Instalar LEDs RGB con controlador WS2812B.
- **Software**:
  - Crear una interfaz en la app para cambiar colores.
  - Programar efectos dinámicos (transiciones, pulsaciones).
- **Pruebas**:
  - Validar el control desde la app y verificar el consumo energético.

#### 3.3. **Modo centinela**

- **Hardware**:
  - Instalar cámaras para monitoreo de 360°.
  - Añadir un disco SSD o microSD para almacenamiento.
  - Usar sensores PIR o de vibración para activación.
- **Software**:
  - Programar grabación continua con OpenCV.
  - Eliminar grabaciones automáticamente tras 72 horas.
  - Añadir alertas en caso de detección de movimiento.
- **Pruebas**:
  - Verificar el consumo energético y la calidad de grabación.

---

### **Fase 4: Integración y App Móvil**

#### 4.1. **Backend**

- Crear un servidor Flask/Django para manejar la lógica central.
- Configurar endpoints para comunicación entre hardware y app.

#### 4.2. **Frontend**

- Diseñar una app con React Native/Kivy con estas secciones:
  - **Luces**: Control de ambiente y automáticas.
  - **Cámara trasera**: Vista en tiempo real.
  - **Modo centinela**: Activar/desactivar grabaciones.
  - **Navegación**: Google Maps integrado.
  - **Comandos de voz**: Enlace para activar funciones.

#### 4.3. **Pruebas de integración**

- Verificar la comunicación entre app, backend y hardware.
- Simular diferentes escenarios (viaje nocturno, túneles, estacionamiento).

---

### **Fase 5: Optimización y Pruebas Finales**

#### 5.1. **Optimización**

- Reducir consumo energético optimizando grabaciones y luces.
- Mejorar tiempos de respuesta de comandos.

#### 5.2. **Pruebas en condiciones reales**

- Probar cada funcionalidad durante trayectos reales.
- Simular emergencias (fallos en sensores, desconexión de la app).

#### 5.3. **Documentación**

- Esquemáticos eléctricos y conexiones.
- Manual de usuario y guía de configuración.
- Video demostrativo de todas las funcionalidades.

---

### **Fase 6: Extensiones Futuras**

- Reconocimiento facial para desbloqueo.
- Integración con asistentes de voz como Alexa o Google Assistant.
- Sensores adicionales (lluvia, temperatura).
