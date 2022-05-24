from odoo import models, fields, api

class DoctorManagement(models.Model):

    _name = "doctor.management"
    _description = "Doctor Management"
    _inherit = "mail.thread"
    _order = "set_priority Desc"

    name = fields.Char(string="Name")
    specializations = fields.Char(string="Specializations")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')])
    mobile_no = fields.Char(string="Mobile No")
    email = fields.Char(string="Email Id")
    set_priority = fields.Selection([('0', 'Very Low'), ('1', 'Low'), ('2', 'Normal'), ('3', 'High'), ('4', 'Very High'), ('5', 'Higher')], string="Set Priority", default="1")
    clinic_id = fields.Many2one("clinic.management", string="Clinic", ondelete='cascade')
    user_id = fields.Many2one("res.users", string="User")
    active = fields.Boolean(string="active", default=True)