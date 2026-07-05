import frappe
from frappe.model.document import Document
from frappe.utils import today, getdate


class RentSchedule(Document):
	pass


@frappe.whitelist()
def create_invoice_for_schedule(rent_schedule):
	doc = frappe.get_doc("Rent Schedule", rent_schedule)
	if doc.sales_invoice:
		frappe.throw(f"Invoice already exists: {doc.sales_invoice}")

	tenant_doc = frappe.get_doc("Customer", doc.tenant)
	company = frappe.defaults.get_user_default("Company") or frappe.db.get_single_value("Global Defaults", "default_company")

	inv = frappe.get_doc({
		"doctype": "Sales Invoice",
		"customer": doc.tenant,
		"company": company,
		"due_date": doc.due_date,
		"items": [{
			"item_name": f"Rent - {doc.unit}",
			"description": f"Rent for unit {doc.unit}, property {doc.property}",
			"qty": 1,
			"rate": doc.amount,
			"income_account": frappe.db.get_value(
				"Company", company, "default_income_account"
			) or "Sales - " + frappe.db.get_value("Company", company, "abbr"),
		}],
	})
	inv.insert(ignore_permissions=True)
	doc.db_set("sales_invoice", inv.name)
	return inv.name


@frappe.whitelist()
def create_invoice_for_contract(lease_contract):
	unpaid = frappe.get_all(
		"Rent Schedule",
		filters={"lease_contract": lease_contract, "payment_status": "Unpaid", "sales_invoice": ["is", "not set"]},
		fields=["name"],
		order_by="due_date asc",
		limit=1,
	)
	if not unpaid:
		frappe.msgprint("No unpaid schedules without an invoice.")
		return None
	return create_invoice_for_schedule(unpaid[0].name)


def mark_overdue_schedules():
	frappe.db.sql("""
		UPDATE `tabRent Schedule`
		SET payment_status = 'Overdue'
		WHERE payment_status = 'Unpaid'
		  AND due_date < %s
	""", today())


def update_payment_status_from_payment_entry(doc, method=None):
	if doc.payment_type != "Receive":
		return
	for ref in doc.references:
		if ref.reference_doctype == "Sales Invoice":
			_update_schedule_from_invoice(ref.reference_name)


def revert_payment_status_from_payment_entry(doc, method=None):
	if doc.payment_type != "Receive":
		return
	for ref in doc.references:
		if ref.reference_doctype == "Sales Invoice":
			schedule = frappe.db.get_value("Rent Schedule", {"sales_invoice": ref.reference_name}, "name")
			if schedule:
				frappe.db.set_value("Rent Schedule", schedule, "payment_status", "Unpaid")


def _update_schedule_from_invoice(invoice_name):
	schedule = frappe.db.get_value("Rent Schedule", {"sales_invoice": invoice_name}, "name")
	if not schedule:
		return
	inv = frappe.get_doc("Sales Invoice", invoice_name)
	if inv.outstanding_amount == 0:
		frappe.db.set_value("Rent Schedule", schedule, "payment_status", "Paid")
	elif inv.outstanding_amount < inv.grand_total:
		frappe.db.set_value("Rent Schedule", schedule, "payment_status", "Partially Paid")


def link_sales_invoice_to_schedule(doc, method=None):
	pass
