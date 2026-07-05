import frappe
from frappe.model.document import Document


class Property(Document):
	def autoname(self):
		if self.property_code:
			self.name = self.property_code
		else:
			from frappe.model.naming import make_autoname
			self.name = make_autoname("PROP-.#####")

	def validate(self):
		self._sync_status_from_units()

	def _sync_status_from_units(self):
		if self.is_new():
			return
		rented = frappe.db.count("Property Unit", {"property": self.name, "status": "Rented"})
		total = frappe.db.count("Property Unit", {"property": self.name})
		if total and rented == total:
			self.status = "Occupied"
