# -*- coding: utf-8 -*-

from odoo import models, fields, api

class FormularioParametrizacion(models.Model):
    _name = 'keralty_module.formulario.param'
    _description = 'Formulario Parametrización'

    nombre_codigo = fields.Char(required=True, string="Nombre o Código", help="PRUEBA AYUDA")
    casilleros = fields.Float(string="Área de casilleros para funcionarios", required=True)
    banios_hombres = fields.Float(string="Baños públicos hombres", required=True, help="Baños públicos hombres")
    banios_mujeres = fields.Float(string="Baños públicos mujeres", required=True, help="Baños públicos mujeres")
    banios_hombres_disc = fields.Float(string="Baños públicos hombres en condición de discapacidad.", required=True, help="Baños publícos hombres en condición de discapacidad")
    banios_mujeres_disc = fields.Float(string="Baños públicos mujeres en condición de discapacidad", required=True, help="Baños públicos mujeres en condición de discapacidad")
    cafeteria_empleados = fields.Float(string="Cafeteria empleados", required=True, help="Cafeteria empleados")
    cuarto_aseo = fields.Float(string="Cuarto de aseo (poceta)", required=True, help="Cuarto de aseo (poceta)")
    banios_hombres_emp = fields.Float(string="Baño hombres para empleados", required=True, help="Baño hombres para empleados")
    banios_mujeres_emp = fields.Float(string="Baño mujeres para empleados", required=True, help="Baño mujeres para empleados")
    # Laboratorio
    banios_hombres_lab = fields.Float(string="Baños públicos hombres laboratorio", required=True, help="Baños públicos hombres laboratorio")
    banios_mujeres_lab = fields.Float(string="Baños públicos mujeres laboratorio", required=True, help="Baños públicos mujeres laboratorio")
    banios_hombres_lab_disc = fields.Float(string="Baños públicos hombres en condición de discapacidad laboratorio", required=True, help="Baños públicos hombres en condición de discapacidad laboratorio")
    banios_mujeres_lab_disc = fields.Float(string="Baños públicos mujeres en condición de discapacidad laboratorio", required=True, help="Baños públicos mujeres en condición de discapacidad laboratorio")
    banio_mixto = fields.Float(string="Baño mixto para empleados", required=True, help="Baño mixto para empleados")
    vestier = fields.Float(string="Vestier con casilleros mixto para empleados", required=True, help="Vestier con casilleros mixto para empleados")
    oficina_admon = fields.Float(string="Oficina coordinación adminsitrativa", required=True, help="Oficina coordinación adminsitrativa")

    #     value = fields.Integer()


class FormularioParametrizacion(models.Model):
    _name = 'keralty_module.formulario.param'
    _description = 'Formulario Parametrización'

    nombre_codigo = fields.Char(required=True)
# class keralty_module(models.Model):
#     _name = 'keralty_module.keralty_module'
#     _description = 'keralty_module.keralty_module'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
