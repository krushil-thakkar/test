from odoo import models, fields, api

class ClinicManagement(models.Model):

    _name = "clinic.management"
    _description = "Clinic Management"

    name = fields.Char(string="Name")
    address = fields.Char(string="Address")
    mobile_no = fields.Char(string="Mobile No")
    email = fields.Char(string="Email Id")
    clinic_ids = fields.One2many('doctor.management', 'clinic_id',string="Doctors")
    patient_ids = fields.One2many('patient.management', 'clinics_id',string="Patients")
    patient_ids = fields.One2many('prescription.management', 'patient_id',string="Patients")

