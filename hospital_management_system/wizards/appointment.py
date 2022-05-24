from odoo import fields, models


class AppointmentReportWizard(models.TransientModel):
    _name = "prescription.report.wizard"

    patient_id = fields.Many2one("patient.management", string="Patient", required=True)
    date_start = fields.Date(string="Date From", required=True)
    date_end = fields.Date(string="Date To", required=True)

    def action_print_report(self):
        prescriptions = self.env['prescription.management'].search_read([])
        data = {
            'form': self.read()[0],
            'prescriptions': prescriptions
        }
        return self.env.ref('hospital_management_system.action_prescription_details').report_action(self, data=data)
