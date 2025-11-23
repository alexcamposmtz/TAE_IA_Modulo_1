# Informe Técnico: Configuración de Entorno de Desarrollo Remoto con CUDA

**Curso:** Talento Altamente Especializado - Inteligencia Artificial 2025  
**Institución:** COCYTEN-Nayarit  
**Instructor:**  
**Estudiante:** Alejandro Campos Martínez  
**Team:** 6  
**Fecha:** 20/11/2025

---

## 1. Resumen Ejecutivo

Este documento detalla la configuración de un entorno de desarrollo distribuido para cómputo acelerado con CUDA, permitiendo el procesamiento remoto de algoritmos de inteligencia artificial desde múltiples equipos cliente hacia un servidor con GPU NVIDIA RTX 4060.

**Tecnologías implementadas:**
- SSH (OpenSSH) para acceso remoto seguro
- Jupyter Lab con port forwarding para desarrollo interactivo
- CuPy 13.6.0 para cómputo paralelo en GPU
- rsync para sincronización eficiente de datasets
- CUDA 12.8 con driver NVIDIA 570.195.03

---

## 2. Arquitectura del Sistema

### 2.1 Configuración de Hardware

| Equipo | Sistema Operativo | Función | Conectividad |
|--------|------------------|---------|--------------|
| Desktop Casa | Ubuntu 22.04 LTS | Cliente de desarrollo | Ethernet (192.XXX.X.XXX) |
| Laptop Móvil | Ubuntu 22.04 LTS | Servidor de cómputo GPU | WiFi (192.XXX.X.XXX) |
| Desktop Oficina | Windows 11 | Cliente de desarrollo | WiFi Universidad |

**Servidor de Cómputo (Laptop):**
- GPU: NVIDIA GeForce RTX 4060 Laptop
- Memoria GPU: 8.2 GB
- CUDA Compute Capability: 8.9 (Arquitectura Ada Lovelace)
- Driver: 570.195.03
- CUDA Toolkit: 12.8

### 2.2 Topología de Red

```
[Desktop Ubuntu Casa] ───Ethernet──┐
                                   │
                              [Router WiFi]
                                   │
[Laptop Ubuntu + RTX 4060] ───WiFi──┘

[Desktop Windows Oficina] ───WiFi Universidad─── [Laptop Ubuntu + RTX 4060]
```

**Nota importante:** Durante las pruebas iniciales se identificó que la laptop estaba conectada a una red de invitados con aislamiento de clientes activado, lo cual impedía la comunicación entre dispositivos. Este problema se resolvió conectando todos los equipos a la red principal.

---

## 3. Implementación

### 3.1 Configuración de SSH Server

En el servidor de cómputo (laptop) se instaló y configuró OpenSSH Server:

```bash
sudo apt update
sudo apt install openssh-server
sudo systemctl enable ssh
sudo systemctl start ssh
```

**Verificación del servicio:**
```bash
sudo systemctl status ssh
sudo ss -tulpn | grep :22
```

**Resultado:** El servidor SSH quedó escuchando correctamente en el puerto 22 para conexiones IPv4 e IPv6.

### 3.2 Autenticación por Clave Pública

Para eliminar la necesidad de contraseñas en cada conexión, se implementó autenticación basada en criptografía de clave pública usando el algoritmo Ed25519:

**En el cliente (desktop):**
```bash
# Generar par de llaves (si no existía previamente)
ssh-keygen -t ed25519 -C "xandro@cresep-desktop"

# Copiar clave pública al servidor
ssh-copy-id xandro@192.168.1.193
```

**Ventajas de Ed25519:**
- Mayor seguridad que RSA con menor tamaño de llave
- Mejor rendimiento en operaciones criptográficas
- Resistencia a ataques de canal lateral

### 3.3 Alias SSH para Conexión Simplificada

Se configuró un alias en `~/.ssh/config` del cliente para simplificar las conexiones:

```bash
Host laptop
    HostName 192.168.1.XXX
    User xandro
    
Host laptop-office
    HostName PENDIENTE
    User xandro
```

**Uso:**
```bash
ssh laptop  # Conexión directa sin especificar IP ni usuario
```

### 3.4 Entorno de Desarrollo con Anaconda y Jupyter Lab

**Inicialización de Conda:**
```bash
~/anaconda3/bin/conda init bash
```

**Paquetes instalados relevantes:**
- Jupyter Lab 4.2.5
- Jupyter Client 8.6.0
- CuPy 13.6.0 (instalado vía conda-forge)
- NumPy (dependencia de CuPy)

**Configuración de Jupyter Lab para acceso remoto:**
```bash
jupyter lab --no-browser --port=8888
```

### 3.5 Port Forwarding SSH

Para acceder a Jupyter Lab desde el cliente sin exponer el servicio directamente en la red, se implementó túnel SSH:

**En el cliente:**
```bash
ssh -N -L 8888:localhost:8888 laptop
```

**Parámetros:**
- `-N`: No ejecutar comandos remotos (solo túnel)
- `-L 8888:localhost:8888`: Redirigir puerto local 8888 al puerto 8888 del servidor

**Acceso:** El cliente puede acceder a Jupyter Lab en `http://127.0.0.1:8888` en su navegador local.

### 3.6 Sincronización de Archivos

Se implementaron dos métodos complementarios para transferencia de archivos:

#### 3.6.1 rsync para Sincronización de Proyectos

**Comando básico:**
```bash
rsync -avz --progress ~/Certificacion/IA/ laptop:~/Certificacion/IA/
```

**Parámetros:**
- `-a`: Modo archivo (preserva permisos, timestamps, enlaces simbólicos)
- `-v`: Verbose (muestra archivos transferidos)
- `-z`: Compresión durante la transferencia
- `--progress`: Muestra progreso de cada archivo

**Aliases configurados en `~/.bashrc`:**
```bash
alias sync-ia-laptop='rsync -avz --progress ~/Certificacion/IA/ laptop:~/Certificacion/IA/'
alias sync-ia-from-laptop='rsync -avz --progress laptop:~/Certificacion/IA/ ~/Certificacion/IA/'
```

**Resultados de sincronización inicial:**
- Archivos transferidos: 597
- Tamaño total: 54.99 MB
- Velocidad: 15.52 MB/s
- Speedup de rsync: 1.42x (eficiencia por compresión)

**Sincronizaciones incrementales:** rsync solo transfiere archivos modificados, haciendo el proceso extremadamente eficiente para actualizaciones frecuentes.

#### 3.6.2 sshfs para Montaje de Sistema de Archivos Remoto

**Instalación:**
```bash
sudo apt install sshfs
```

**Uso:**
```bash
# Crear punto de montaje
mkdir -p ~/laptop_remota

# Montar sistema de archivos remoto
sshfs laptop:/home/xandro ~/laptop_remota

# Desmontar cuando no se necesite
fusermount -u ~/laptop_remota
```

**Aplicación:** Permite editar archivos remotos como si fueran locales, útil para revisiones rápidas sin necesidad de sincronización completa.

---

## 4. Validación de CUDA

### 4.1 Verificación de Disponibilidad

**Comando de diagnóstico:**
```bash
nvidia-smi
```

**Resultado:**
```
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 570.195.03             Driver Version: 570.195.03     CUDA Version: 12.8     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA GeForce RTX 4060 ...    On  |   00000000:01:00.0 Off |                  N/A |
| N/A   42C    P3            590W /   60W |      11MiB /   8188MiB |     15%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
```

### 4.2 Prueba de Cómputo con CuPy

**Código de validación ejecutado en Jupyter Lab:**

```python
import cupy as cp
import numpy as np
import time

print(f"CuPy version: {cp.__version__}")
print(f"CUDA available: {cp.cuda.is_available()}")

# Información del dispositivo
device = cp.cuda.Device(0)
print(f"\nDevice name: {device.compute_capability}")
print(f"Total memory: {device.mem_info[1] / 1e9:.2f} GB")
print(f"Free memory: {device.mem_info[0] / 1e9:.2f} GB")

# Prueba de multiplicación de matrices
x = cp.random.rand(1000, 1000, dtype=cp.float32)
y = cp.random.rand(1000, 1000, dtype=cp.float32)
z = cp.matmul(x, y)

print(f"\n✓ Multiplicación de matrices en GPU exitosa!")
print(f"Resultado shape: {z.shape}")

# Comparación de rendimiento GPU vs CPU
start = time.time()
z_gpu = cp.matmul(x, y)
cp.cuda.Stream.null.synchronize()
gpu_time = time.time() - start

x_cpu = cp.asnumpy(x)
y_cpu = cp.asnumpy(y)
start = time.time()
z_cpu = np.matmul(x_cpu, y_cpu)
cpu_time = time.time() - start

print(f"\nTiempo GPU: {gpu_time*1000:.2f} ms")
print(f"Tiempo CPU: {cpu_time*1000:.2f} ms")
print(f"Speedup: {cpu_time/gpu_time:.2f}x")
```

### 4.3 Resultados de Rendimiento

| Métrica | Valor |
|---------|-------|
| CuPy Version | 13.6.0 |
| CUDA Disponible | Sí |
| Compute Capability | 8.9 |
| Memoria Total | 8.20 GB |
| Memoria Libre | 8.08 GB |
| **Tiempo GPU** | **0.60 ms** |
| **Tiempo CPU** | **10.72 ms** |
| **Speedup GPU vs CPU** | **17.75x** |

**Análisis de resultados:**

La aceleración de 17.75x para multiplicación de matrices (1000×1000) demuestra la efectividad del cómputo paralelo en GPU. Este speedup se debe a:

1. **Arquitectura paralela:** La RTX 4060 (Ada Lovelace) tiene 3,072 CUDA cores que procesan múltiples operaciones simultáneamente
2. **Memoria de alta velocidad:** La memoria GDDR6 de la GPU (hasta 224 GB/s de ancho de banda) supera ampliamente la RAM del sistema
3. **Optimización de CuPy:** La biblioteca está diseñada específicamente para aprovechar las capacidades de CUDA

**Implicaciones para IA:**
- Reducción significativa en tiempos de entrenamiento de redes neuronales
- Capacidad para procesar datasets más grandes en tiempo razonable
- Iteraciones más rápidas durante experimentación y ajuste de hiperparámetros

---

## 5. Flujo de Trabajo Establecido

### 5.1 Inicio de Sesión de Trabajo

**Paso 1:** Conectarse al servidor
```bash
ssh laptop
```

**Paso 2:** Iniciar Jupyter Lab
```bash
jupyter lab --no-browser --port=8888
```

**Paso 3:** En otra terminal del cliente, crear túnel SSH
```bash
ssh -N -L 8888:localhost:8888 laptop
```

**Paso 4:** Copiar la URL con token de Jupyter y pegarla en el navegador local

### 5.2 Durante el Desarrollo

- Editar código en Jupyter Lab a través del navegador
- Ejecutar celdas que automáticamente usan la GPU remota
- Monitorear uso de GPU con `nvidia-smi` en terminal SSH si es necesario

### 5.3 Sincronización de Archivos

**Antes de iniciar trabajo:** (si se modificaron archivos en el cliente)
```bash
sync-ia-laptop
```

**Al finalizar:** (para obtener resultados del servidor)
```bash
sync-ia-from-laptop
```

### 5.4 Cierre de Sesión

1. Detener Jupyter Lab: `Ctrl+C` (dos veces)
2. Cerrar túnel SSH: `Ctrl+C` en la terminal del túnel
3. Cerrar sesión SSH: `exit` o `Ctrl+D`

---

## 6. Consideraciones de Seguridad

### 6.1 Medidas Implementadas

1. **Autenticación por clave pública:** Elimina el riesgo de ataques de fuerza bruta a contraseñas
2. **Conexiones cifradas:** Todo el tráfico SSH (incluyendo Jupyter) está cifrado con AES-256
3. **No exposición de puertos:** Jupyter no está expuesto directamente, solo accesible vía túnel SSH
4. **Acceso en red local:** Las conexiones solo ocurren dentro de la red local confiable

### 6.2 Recomendaciones Adicionales (para implementación futura)

1. **Fail2ban:** Protección contra intentos repetidos de conexión fallidos
2. **Cambio de puerto SSH:** Usar puerto no estándar (diferente del 22) para reducir escaneos automatizados
3. **VPN:** Para acceso desde redes externas (como la universidad), considerar VPN en lugar de port forwarding
4. **Respaldos automatizados:** Implementar scripts de respaldo periódico de datasets y resultados

---

## 7. Escalabilidad: Integración de NVIDIA Jetson

El sistema diseñado está preparado para incorporar dispositivos adicionales de cómputo. Al recibir la tarjeta NVIDIA Jetson, se podrá:

### 7.1 Configuración Prevista

**Agregar alias SSH:**
```bash
Host jetson
    HostName IP_de_jetson
    User usuario_jetson
```

**Replicar configuración:**
- Instalar OpenSSH Server
- Copiar clave pública SSH
- Instalar Anaconda/Miniconda
- Configurar Jupyter Lab
- Instalar CuPy para ARM (jetson usa arquitectura ARM64)

### 7.2 Casos de Uso para Arquitectura Distribuida

1. **Entrenamiento paralelo:** Ejecutar diferentes experimentos simultáneamente en RTX 4060 y Jetson
2. **Pipeline de procesamiento:** Pre-procesamiento en Jetson, entrenamiento en RTX 4060
3. **Comparación de rendimiento:** Evaluar diferencias entre arquitecturas x86-64 (laptop) y ARM64 (Jetson)
4. **Desarrollo edge-to-cloud:** Prototipar modelos en Jetson para implementación en dispositivos embebidos

---

## 8. Métricas de Eficiencia

### 8.1 Tiempo de Configuración

| Tarea | Tiempo Estimado |
|-------|-----------------|
| Instalación y configuración SSH | 5 minutos |
| Configuración de llaves públicas | 3 minutos |
| Instalación de CuPy | 2 minutos |
| Configuración de aliases y scripts | 5 minutos |
| Sincronización inicial de proyecto | 3 minutos |
| **Total** | **18 minutos** |

### 8.2 Comparación de Métodos de Transferencia

**Transferencia inicial (597 archivos, 55 MB):**
- **rsync:** 3.54 segundos (15.52 MB/s)
- **scp convencional (estimado):** ~8-10 segundos

**Transferencia incremental (1 archivo, 36 bytes):**
- **rsync:** < 1 segundo (solo el archivo modificado)
- **scp:** requeriría transferir todo el proyecto nuevamente

**Eficiencia de rsync:** 1.42x por compresión + transferencia diferencial

---

## 9. Conclusiones

### 9.1 Logros

1. Sistema de desarrollo remoto totalmente funcional
2. Aceleración GPU verificada (17.75x en operaciones matriciales)
3. Flujo de trabajo eficiente con sincronización automática
4. Acceso seguro mediante SSH con autenticación por llave pública
5. Entorno escalable para agregar más dispositivos de cómputo

### 9.2 Beneficios para el Curso de IA

**Flexibilidad:**
- Trabajar desde múltiples ubicaciones (casa, oficina)
- Acceso desde diferentes sistemas operativos (Ubuntu, Windows)

**Eficiencia:**
- Aprovechamiento completo de GPU dedicada
- Sincronización rápida de datasets y código
- Iteraciones de desarrollo más rápidas

**Aprendizaje:**
- Experiencia práctica con herramientas profesionales (SSH, rsync, Jupyter)
- Comprensión de arquitecturas cliente-servidor
- Familiarización con cómputo distribuido

### 9.3 Aplicabilidad Profesional

Las habilidades y configuración desarrolladas son directamente aplicables a:

- Entornos de producción en empresas de IA/ML
- Clusters de cómputo académico y de investigación
- Desarrollo cloud (AWS, Google Cloud, Azure) donde se accede remotamente a instancias con GPU
- Administración de infraestructura DevOps

---

## 10. Referencias

### 10.1 Documentación Técnica

1. OpenSSH Official Documentation: https://www.openssh.com/manual.html
2. Jupyter Documentation: https://jupyter.org/documentation
3. CuPy User Guide: https://docs.cupy.dev/en/stable/user_guide/index.html
4. rsync Man Page: https://linux.die.net/man/1/rsync
5. NVIDIA CUDA Documentation: https://docs.nvidia.com/cuda/

### 10.2 Herramientas Utilizadas

| Herramienta | Versión | Propósito |
|-------------|---------|-----------|
| Ubuntu | 22.04.5 LTS | Sistema operativo base |
| OpenSSH | 8.9p1 | Acceso remoto seguro |
| Anaconda | 24.9.2 | Gestión de entornos Python |
| Jupyter Lab | 4.2.5 | Entorno de desarrollo interactivo |
| CuPy | 13.6.0 | Cómputo en GPU |
| NVIDIA Driver | 570.195.03 | Control de GPU |
| CUDA Toolkit | 12.8 | Plataforma de cómputo paralelo |
| rsync | 3.2.7 | Sincronización de archivos |

---

## Anexos

### Anexo A: Comandos de Referencia Rápida

#### A.1 Secuencia de Inicio de Sesión de Trabajo

**Paso 1: Conectarse al servidor (ejecutar en Desktop/Cliente)**
```bash
ssh laptop
# o cuando esté en la oficina:
ssh laptop-office
```

**Paso 2: Iniciar Jupyter Lab (ejecutar en Laptop/Servidor vía SSH)**
```bash
jupyter lab --no-browser --port=8888
```
*Nota: Copiar la URL con token que aparece (ej: http://localhost:8888/lab?token=abc123...)*

**Paso 3: Crear túnel SSH (ejecutar en Desktop/Cliente en OTRA terminal)**
```bash
ssh -N -L 8888:localhost:8888 laptop
```
*Nota: Este comando se queda ejecutando, no devuelve el prompt*

**Paso 4: Abrir navegador (en Desktop/Cliente)**
- Pegar la URL con token del Paso 2 en el navegador
- Trabajar normalmente en Jupyter Lab

#### A.2 Sincronización de Archivos

**Sincronizar archivos locales al servidor (ejecutar en Desktop/Cliente)**
```bash
sync-ia-laptop          # Desktop → Laptop
```

**Obtener archivos del servidor (ejecutar en Desktop/Cliente)**
```bash
sync-ia-from-laptop     # Laptop → Desktop
```

**Comandos rsync completos (si no usas los aliases):**
```bash
# Desktop → Laptop (ejecutar en Desktop/Cliente)
rsync -avz --progress ~/Certificacion/IA/ laptop:~/Certificacion/IA/

# Laptop → Desktop (ejecutar en Desktop/Cliente)
rsync -avz --progress laptop:~/Certificacion/IA/ ~/Certificacion/IA/
```

#### A.3 Monitoreo de GPU

**Ver estado de GPU (ejecutar en Laptop/Servidor vía SSH)**
```bash
nvidia-smi
```

**Monitoreo continuo (ejecutar en Laptop/Servidor vía SSH)**
```bash
watch -n 1 nvidia-smi   # Actualización cada segundo
```

#### A.4 Montaje Remoto de Sistema de Archivos (Opcional)

**Montar carpeta remota (ejecutar en Desktop/Cliente)**
```bash
sshfs laptop:/home/xandro ~/laptop_remota
```

**Desmontar cuando no se necesite (ejecutar en Desktop/Cliente)**
```bash
fusermount -u ~/laptop_remota
```

#### A.5 Cierre de Sesión de Trabajo

**Paso 1: Detener Jupyter Lab (en la terminal SSH del Paso 2)**
```
Ctrl+C (presionar dos veces)
```

**Paso 2: Cerrar túnel SSH (en la terminal del Paso 3)**
```
Ctrl+C
```

**Paso 3: Cerrar sesión SSH (en la terminal del Paso 1)**
```bash
exit
# o presionar Ctrl+D
```

#### A.6 Tabla Resumen de Ubicación de Comandos

| Comando | Dónde se ejecuta | Propósito |
|---------|------------------|-----------|
| `ssh laptop` | Desktop/Cliente | Conectarse al servidor |
| `jupyter lab --no-browser --port=8888` | Laptop/Servidor (vía SSH) | Iniciar Jupyter |
| `ssh -N -L 8888:localhost:8888 laptop` | Desktop/Cliente (nueva terminal) | Crear túnel |
| `sync-ia-laptop` | Desktop/Cliente | Sincronizar archivos |
| `sync-ia-from-laptop` | Desktop/Cliente | Obtener archivos |
| `nvidia-smi` | Laptop/Servidor (vía SSH) | Monitorear GPU |
| `sshfs laptop:/home/xandro ~/laptop_remota` | Desktop/Cliente | Montar sistema remoto |
| `fusermount -u ~/laptop_remota` | Desktop/Cliente | Desmontar sistema remoto |

### Anexo B: Resolución de Problemas Comunes

**Problema:** "No route to host" al conectar via SSH
- **Causa:** Dispositivo en red de invitados con aislamiento
- **Solución:** Conectar a la red principal del router

**Problema:** Jupyter Lab no accesible en navegador
- **Causa:** Túnel SSH no establecido correctamente
- **Solución:** Verificar que el comando `ssh -N -L` esté ejecutándose

**Problema:** CuPy no encuentra CUDA
- **Causa:** Variable de entorno CUDA_PATH no configurada
- **Solución:** Reinstalar CuPy con versión específica para CUDA 12

**Problema:** rsync lento en primera sincronización
- **Causa:** Normal para transferencia inicial
- **Solución:** Transferencias subsecuentes serán incrementales y rápidas

---

**Documento preparado como parte del Módulo 1 del Programa de Certificación en Inteligencia Artificial**  
**COCYTEN-Nayarit**
