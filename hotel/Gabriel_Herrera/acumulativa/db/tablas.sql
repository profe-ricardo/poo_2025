CREATE TABLE inventario (
    id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nombre VARCHAR2(100),
    tipo VARCHAR2(50),
    cantidad NUMBER,
    precio_costo NUMBER
);

CREATE TABLE habitacion (
    numero NUMBER PRIMARY KEY,
    cant_personas NUMBER,
    estado VARCHAR2(20)
);

CREATE TABLE cliente (
    id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nombre VARCHAR2(100),
    telefono VARCHAR2(20),
    nacionalidad VARCHAR2(50),
    habitacion NUMBER REFERENCES habitacion(numero)
);

CREATE TABLE usuario (
    id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nombre VARCHAR2(100),
    telefono VARCHAR2(20)
);

CREATE TABLE recepcionista (
    id NUMBER PRIMARY KEY REFERENCES usuario(id),
    ubicacion VARCHAR2(100)
);

CREATE TABLE boleta (
    folio NUMBER PRIMARY KEY,
    cliente NUMBER REFERENCES cliente(id),
    usuario NUMBER REFERENCES usuario(id)
);
