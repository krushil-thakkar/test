from odoo import models,fields,api

class CreateDoctor(models.TransientModel):
    _name = "create.doctor"
    _description = "Create a doctor"

    name = fields.Char(string="Name")
    specializations = fields.Char(string="Specializations")

    def action_done(self):
        print("You clicked create button")

    def cancel_button(self):
        print("You clicked cancel button")
