# Prueba de funcionamiento de Apache Spark

Este documento describe una prueba básica para verificar que el clúster de
**Apache Spark** ejecutándose en **Docker** funciona correctamente y acepta
trabajos enviados desde Python (PyCharm).

---

## 🎯 Objetivo de la prueba

- Comprobar que PyCharm puede conectarse al Spark Master.
- Validar que Spark ejecuta un job distribuido.
- Confirmar que la comunicación se realiza por el puerto `7077`.

---

## 🧱 Entorno de ejecución

- Sistema operativo: Windows
- Entorno Big Data: Docker + Apache Spark
- Cliente: Python (PyCharm)
- Configuración del clúster:
  - 1 Spark Master
  - 1 Spark Worker (2GB RAM)

---

## ▶️ Ejecución de la prueba

1. El clúster Spark debe estar arrancado:
   ```bash
   docker compose up -d
## Requisitos
2. Instalar libreríasWindows 10/11
- (Para la prueba) `pyspark` en tu entorno local:
  ```bash
  pip install pyspark
### Ejecución desde terminal (opcional)
2. Ejecutar script

![img](images/containers.png)

![img](images/spark-master.png)

Ejecutamos en el contenedor spark master

    ls /opt/bitnami/spark/scripts
    test_spark.py
    spark-submit \
      --master spark://spark-master:7077 \
      /opt/bitnami/spark/scripts/test_spark.py

![img](images/example.png)






