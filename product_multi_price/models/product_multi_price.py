# Copyright 2020 Tecnativa - David Vidal
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import api, fields, models


class ProductMultiPrice(models.Model):
    _name = "product.multi.price"
    _rec_name = "name_text"
    _description = "Product Multiple Prices"

    name = fields.Many2one("product.multi.price.name", required=True)
    name_text = fields.Char(related="name.name")
    product_id = fields.Many2one(
        comodel_name="product.product",
        required=True,
        ondelete="cascade",
    )
    price = fields.Float(
        digits="Product Price",
    )
    company_id = fields.Many2one(
        comodel_name="res.company",
        related="name.company_id",
        store=True,
        readonly=True,
    )

    _sql_constraints = [
        (
            "multi_price_uniq",
            "unique(name, product_id, company_id)",
            "A field name cannot be assigned to a product twice for the same "
            "company",
        ),
    ]


class ProductMultiPriceName(models.Model):
    _name = "product.multi.price.name"
    _description = "Multi Price Record Options"

    @api.model
    def _get_company(self):
        return self._context.get("company_id", self.env.company)

    name = fields.Char(required=True, string="Price Field Name")
    company_id = fields.Many2one(
        comodel_name="res.company",
        required=True,
        default=lambda self: self._get_company(),
    )

    _sql_constraints = [
        (
            "multi_price_name_uniq",
            "unique(name, company_id)",
            "Prices Names must be unique per company",
        ),
    ]
