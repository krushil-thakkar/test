""" coding: utf-8 """
from odoo import http
from odoo.http import request

# class HospitalManagement(http.Controller):
#     """this is hospital management"""
#     @http.route('/Hospital/Management', type='http', auth='public', website=True)
#     # @classmethod
#     def clinic(self):
#         """this is clinic management"""
#         clinic_manage = request.env['clinic.management'].sudo().search([])
#         return http.request.render('hospital_management_system.clinic_page', {'my_details': clinic_manage})
#
#     @http.route('/Doctor/Management', type='http', auth='public', website=True)
#     # @classmethod
#     def doctor(self):
#         """this is doctor management"""
#         doctor_manage = request.env['doctor.management'].sudo().search([])
#         return http.request.render('hospital_management_system.doctor_page', {'my_details': doctor_manage})
#
#     @http.route('/Patient/Management', type='http', auth='public', website=True)
#     # @classmethod
#     def patient(self):
#         """this is patient management"""
#         patient_manage = request.env['patient.management'].sudo().search([])
#         return http.request.render('hospital_management_system.patient_page', {'my_details': patient_manage})
#
#     @http.route('/Prescription/Management', type='http', auth='public', website=True)
#     # @classmethod
#     def prescription(self):
#         """this is prescription management"""
#         prescription_manage = request.env['prescription.management'].sudo().search([])
#         return http.request.render('hospital_management_system.prescription_page', {'my_details': prescription_manage})

class Hospital(http.Controller):
    """this is hospital management form"""
    @http.route('/website', type='http', auth='public', website=True)
    def patient_web_form(self):
        """this method defines create the patient"""
        return request.render('hospital_management_system.create_patient', {})

    # @http.route('/create/webpatient', type='http', auth='public', website=True)
    # # @classmethod
    # def patient_web_patient(self, **kwargs):
    #     """this method defines write the message"""
    #     request.env['patient.management'].sudo().create(kwargs)
    #     return http.request.render('hospital_management_system.patient_thanks', {})
    