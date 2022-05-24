from odoo import models, fields, api

class DoctorManagement(models.Model):

    _name = "patient.management"
    _description = "Patient Management"
    _inherits = {'res.partner': 'partner_id'}
    _order = "id Desc"

    partner_id = fields.Many2one("res.partner", string="Partner Id")
    age = fields.Integer(string="Age")
    image = fields.Binary(string="Image")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    patient_id = fields.Integer(string="Patient Id")
    doctor_id = fields.Many2one("doctor.management",string="Doctor")
    marital_status = fields.Selection([('married', 'Married'), ('unmarried', 'Unmarried')])
    blood_group = fields.Char(string="Blood Group")
    mobile_no = fields.Char(string="Mobile No")
    clinics_id = fields.Many2one("clinic.management", string="Clinic")
    medicine_name = fields.Char(string="Medicine Name")
    dose = fields.Char(string="Dose")
    qty = fields.Integer(string="Quantity")
    duration_period = fields.Datetime(string="Duration Period")
    comment = fields.Html(string="Comment")
    patient_ids = fields.One2many("prescription.management", "patient_id", string="Prescriptions")
    # total_invoices = fields.Integer(string="Total invoice", compute="_invoices")
    total_prescription = fields.Integer(string="Total Prescription", compute="_prescription")
    active = fields.Boolean(string="active", default=True)

    # def _invoices(self):
    #     for rec in self:
    #         rec.total_invoices = len(rec.invoice_ids)

    def _prescription(self):
        for rec in self:
            rec.total_prescription = len(rec.patient_ids)

    # def get_action_school(self):
    #     action = {
    #         'name': 'partner',
    #         'view_mode': 'tree,form',
    #         'res_model': 'account.move',
    #         'type': 'ir.actions.act_window',
    #         'domain': [('id', '=', self.invoice_ids.ids)]
    #     }
    #     return action

    def action_url(self):
        return {
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': 'https://getbootstrap.com/docs/4.0/components/buttons/'
        }




