# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date

# class my_module(models.Model):
#     _name = 'my_module.my_module'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

# class SaleOrderLine(models.Model):
#     _inherit = 'sale.order.line'
#
#     @api.onchange('product_uom', 'product_uom_qty')
#     def product_uom_change(self):
#         super(SaleOrderLine, self).product_uom_change()
#         res = {}
#         if self.product_uom_qty and self.product_uom_qty > 1:
#             warning = {
#                 'title': "Error validación en el producto {}".format(
#                     self.product_id.name
#                 ),
#                 'message': "Supera la cantidad máxima de (1)",
#                 'type': 'notification',
#             }
#             res.update({'warning': warning})
#         return res

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    @api.onchange('date_order')
    def date_order_change(self):
        res = {}
        if self.date_order and self.date_order.date() < date.today():
            warning = {
                'title': "Error validación en la fecha {}".format(
                    self.date_order
                ),
                'message': "Fecha Pedido no puede ser menor a la fecha actual.",
                #'type': 'notification',
            }
            res.update({'warning': warning})
        return res

class StockReturnPicking(models.TransientModel):
    _inherit = "stock.return.picking"

    @api.onchange('quantity')
    def quantity_change(self):
        res = {}
        if self.quantity and self.quantity > 5:
            warning = {
                'title': "Error validación en la cantidad {}".format(
                    self.quantity
                ),
                'message': "La cantidad a devolver no puede ser mayor a la cantidad terminada.",
                #'type': 'notification',
            }
            res.update({'warning': warning})
        return res


# class ReturnPickingLine(models.TransientModel):
#     _name = "stock.return.picking.line"


# class ReturnPicking(models.TransientModel):
#     _name = 'stock.return.picking'