# Instalación de .NET Core en Void Linux @daianalogy

Para otras distribuciones de Linux, sobre todo las más populares, existe ya documentación guiada por comandos con respecto a la instalación de .NET Core. Para todos los demás sabores de Linux no tan populares y no conocidos existe por parte de Microsoft la guía de [“Instalación con script y binarios"](https://learn.microsoft.com/es-mx/dotnet/core/install/linux-scripted-manual)

Es la que nos tocará aplicar para tener corriendo el entorno completo (runtime + sdk) de .NET Core en Void Linux. 

1. Lo que primero necesitaremos es el script de **dotnet-install.sh**

Lo puede descargar [aquí](https://dot.net/v1/dotnet-install.sh) o ejecutando el siguiente comando:

```bash
wget https://dot.net/v1/dotnet-install.sh
```

1. Luego procedemos a comprobar que tengamos la carpeta oculta de .dotnet en nuestro directorio /home

```bash
cd ~/.dotnet
```

1. (OPCIONAL) Podemos dejar nuestra carpeta en ese mismo lugar o  copiarla a /usr/share/ para tener todo más ordenado. Igualmente podemos renombrarla si queremos que deje de ser una carpeta oculta. Siéntete libre de saltarte el siguiente paso si no lo consideras necesario y no sabes mucho de directorios. 

```bash
sudo cp -rv ~/.dotnet /usr/share

sudo rm -r ~/.dotnet
```

1. Una vez tenemos la carpeta en el directorio de nuestra preferencia o defecto debemos crear un enlace simbólico del archivo dotnet que apunte a los binarios de nuestro sistema. Recuerda siempre utilizar las rutas absolutas para éste tipo de procedimientos si no sabes lo que haces.

```bash
sudo ln -s /usr/share/.dotnet/dotnet /usr/bin
```

1. Comprobamos que dotnet está instalado en nuestro sistema Void Linux ejecutando el siguiente comando.

```bash
dotnet --info
```

Felicidades, ya tiene el entorno completo de .NET Core en tu sistema Void Linux ¡Excelente! Ahora sácale provecho.