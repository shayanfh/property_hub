import frappe
from frappe.model.document import Document


class PropertyOwner(Document):
	def validate(self):
		if self.email:
			frappe.utils.validate_email_address(self.email, throw=True)

	def after_insert(self):
		if not self.supplier:
			self._create_supplier()

	def _create_supplier(self):
		supplier = frappe.get_doc({
			"doctype": "Supplier",
			"supplier_name": self.owner_name,
			"supplier_group": frappe.db.get_single_value("Buying Settings", "supplier_group") or "All Supplier Groups",
			"supplier_type": "Individual",
		})
		supplier.insert(ignore_permissions=True)
		self.db_set("supplier", supplier.name)
