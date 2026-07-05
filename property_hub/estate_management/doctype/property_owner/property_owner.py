import frappe
from frappe.model.document import Document


class PropertyOwner(Document):
	def validate(self):
		if self.email:
			frappe.utils.validate_email_address(self.email, throw=True)

	def after_insert(self):
		if not self.supplier:
			try:
				self._create_supplier()
			except Exception:
				pass  # supplier creation is optional; owner record remains valid

	def _create_supplier(self):
		sg = (
			frappe.db.get_single_value("Buying Settings", "supplier_group")
			or _default_supplier_group()
		)
		if not sg:
			return
		supplier = frappe.get_doc({
			"doctype": "Supplier",
			"supplier_name": self.owner_name,
			"supplier_group": sg,
		})
		supplier.insert(ignore_permissions=True)
		self.db_set("supplier", supplier.name)


def _default_supplier_group():
	row = frappe.get_all("Supplier Group", limit=1, fields=["name"])
	return row[0].name if row else None
