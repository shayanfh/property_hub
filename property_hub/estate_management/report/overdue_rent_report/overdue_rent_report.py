import frappe
from frappe.utils import today


def execute(filters=None):
	filters = filters or {}
	columns = [
		{"label": "Schedule", "fieldname": "name", "fieldtype": "Link", "options": "Rent Schedule", "width": 150},
		{"label": "Tenant", "fieldname": "tenant", "fieldtype": "Link", "options": "Customer", "width": 150},
		{"label": "Property", "fieldname": "property", "fieldtype": "Link", "options": "Property", "width": 150},
		{"label": "Unit", "fieldname": "unit", "fieldtype": "Link", "options": "Property Unit", "width": 120},
		{"label": "Due Date", "fieldname": "due_date", "fieldtype": "Date", "width": 110},
		{"label": "Days Overdue", "fieldname": "days_overdue", "fieldtype": "Int", "width": 110},
		{"label": "Amount", "fieldname": "amount", "fieldtype": "Currency", "width": 120},
		{"label": "Sales Invoice", "fieldname": "sales_invoice", "fieldtype": "Link", "options": "Sales Invoice", "width": 150},
	]

	where = "rs.payment_status IN ('Unpaid', 'Overdue') AND rs.due_date < CURDATE()"
	values = {}
	if filters.get("tenant"):
		where += " AND rs.tenant = %(tenant)s"
		values["tenant"] = filters["tenant"]
	if filters.get("property"):
		where += " AND rs.property = %(property)s"
		values["property"] = filters["property"]

	data = frappe.db.sql(f"""
		SELECT rs.name, rs.tenant, rs.property, rs.unit,
			   rs.due_date, DATEDIFF(CURDATE(), rs.due_date) AS days_overdue,
			   rs.amount, rs.sales_invoice
		FROM `tabRent Schedule` rs
		WHERE {where}
		ORDER BY rs.due_date
	""", values, as_dict=True)

	return columns, data
