import frappe
from frappe.model.document import Document


class PropertyUnit(Document):
	def validate(self):
		if self.bedrooms and self.bedrooms < 0:
			frappe.throw("Bedrooms cannot be negative.")
		if self.area and self.area < 0:
			frappe.throw("Area cannot be negative.")
