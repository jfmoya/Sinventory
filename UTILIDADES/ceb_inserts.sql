INSERT INTO proveedor (pro_codigo, pro_cacreg, pro_cedula, pro_nombre, pro_ruc, pro_fecnac, pro_genero, pro_estado, pro_sap, ope_codigo) 
VALUES( 100, 1000, 1784446386, 'Neppas Nepas Ana Luisa', 1784446386001, '1951-02-20', 'M', 1, 100000100, 711);

insert into operador (ope_codigo, ope_nombre, ope_cedula, cac_codigo, ope_clave, ope_estado)
values (711, 'Moya Dobronski JuanFernando', 1710217520, 1000, 0, 1);

insert into centro_acopio (cac_codigo, cac_nombre, cac_ruc, cac_coord, cac_correo, cac_telf, cac_direccion, cac_estado)
values (1000, 'Puerta del Sol - Lote 3', 1792826548001, point(-0.0989849, -78.1756194), 'lote3@elordeno.ec', '0996665552', 'Lote 3', 1);

INSERT INTO producto (prd_codigo, prd_nombre, prd_preciokg, prd_estado, prd_sap, ope_codigo)
VALUES (100001, "Cebolla Blanca Larga", 1.5738, 1, 100100001, 711);


