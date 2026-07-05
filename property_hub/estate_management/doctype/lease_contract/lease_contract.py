import frappe
from frappe.model.document import Document
from frappe.utils import add_months, add_days, getdate, today


class LeaseContract(Document):
	def validate(self):
		if self.start_date and self.end_date:
			if getdate(self.start_date) >= getdate(self.end_date):
				frappe.throw("End Date must be after Start Date.")
		self._set_unit_status()

	def before_submit(self):
		self.status = "Active"

	def on_cancel(self):
		self.status = "Cancelled"
		self._revert_unit_status()

	def _set_unit_status(self):
		if self.unit and self.docstatus == 1:
			frappe.db.set_value("Property Unit", self.unit, "status", "Rented")

	def _revert_unit_status(self):
		if self.unit:
			frappe.db.set_value("Property Unit", self.unit, "status", "Available")


@frappe.whitelist()
def on_submit_generate_rent_schedule(doc, method=None):
	if isinstance(doc, str):
		doc = frappe.get_doc("Lease Contract", doc)
	_generate_rent_schedule(doc)
	frappe.db.set_value("Property Unit", doc.unit, "status", "Rented")


@frappe.whitelist()
def on_cancel_rent_schedule(doc, method=None):
	if isinstance(doc, str):
		doc = frappe.get_doc("Lease Contract", doc)
	frappe.db.delete("Rent Schedule", {"lease_contract": doc.name, "payment_status": "Unpaid"})
	frappe.db.set_value("Property Unit", doc.unit, "status", "Available")


def _generate_rent_schedule(doc):
	existing = frappe.db.count("Rent Schedule", {"lease_contract": doc.name})
	if existing:
		return

	start = getdate(doc.start_date)
	end = getdate(doc.end_date)
	frequency_months = {"Monthly": 1, "Quarterly": 3, "Yearly": 12}.get(doc.payment_frequency, 1)

	due_date = start
	while due_date <= end:
		rs = frappe.get_doc({
			"doctype": "Rent Schedule",
			"lease_contract": doc.name,
			"tenant": doc.tenant,
			"property": doc.property,
			"unit": doc.unit,
			"due_date": due_date,
			"amount": doc.rent_amount,
			"payment_status": "Unpaid",
		})
		rs.insert(ignore_permissions=True)
		due_date = add_months(due_date, frequency_months)


def update_expired_contracts():
	contracts = frappe.get_all(
		"Lease Contract",
		filters={"status": "Active", "end_date": ["<", today()], "docstatus": 1},
		fields=["name"],
	)
	for c in contracts:
		frappe.db.set_value("Lease Contract", c.name, "status", "Expired")
