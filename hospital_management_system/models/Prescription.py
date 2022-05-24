from odoo import models, fields, api
from odoo.exceptions import ValidationError

class PrescriptionManagement(models.Model):

    _name = "prescription.management"
    _inherits = {'patient.management': 'patient_id'}
    _description = "Prescription Management"

    patient_id = fields.Many2one("patient.management",string="Patient")
    total_prescription = fields.Integer(string="Prescription Id")
    date_start = fields.Date(string="Start Date")
    date_end = fields.Date(string="End date")


    # @api.constrains('date_end')
    # def _check_date_end(self):
    #     for record in self:
    #         if record.date_end < fields.Date.today():
    #             raise ValidationError("The end date cannot be set in the past")
    #         elif record.date_end < record.date_start:
    #             raise ValidationError("The end date must be greater than start date")


