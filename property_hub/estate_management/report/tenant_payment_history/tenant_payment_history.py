import frappe


def execute(filters=None):
	filters = filters or {}
	columns = [
		{"label": "Schedule", "fieldname": "name", "fieldtype": "Link", "options": "Rent Schedule", "width": 150},
		{"label": "Tenant", "fieldname": "tenant", "fieldtype": "Link", "options": "Customer", "width": 150},
		{"label": "Lease Contract", "fieldname": "lease_contract", "fieldtype": "Link", "options": "Lease Contract", "width": 160},
		{"label": "Property", "fieldname": "property", "fieldtype": "Link", "options": "Property", "width": 150},
		{"label": "Unit", "fieldname": "unit", "fieldtype": "Link", "options": "Property Unit", "width": 120},
		{"label": "Due Date", "fieldname": "due_date", "fieldtype": "Date", "width": 110},
		{"label": "Amount", "fieldname": "amount", "fieldtype": "Currency", "width": 120},
		{"label": "Payment Status", "fieldname": "payment_status", "fieldtype": "Data", "width": 120},
		{"label": "Sales Invoice", "fieldname": "sales_invoice", "fieldtype": "Link", "options": "Sales Invoice", "width": 150},
	]

	where = "1=1"
	values = {}
	if filters.get("tenant"):
		where += " AND rs.tenant = %(tenant)s"
		values["tenant"] = filters["tenant"]
	if filters.get("from_date"):
		where += " AND rs.due_date >= %(from_date)s"
		values["from_date"] = filters["from_date"]
	if filters.get("to_date"):
		where += " AND rs.due_date <= %(to_date)s"
		values["to_date"] = filters["to_date"]

	data = frappe.db.sql(f"""
		SELECT rs.name, rs.tenant, rs.lease_contract, rs.property, rs.unit,
			   rs.due_date, rs.amount, rs.payment_status, rs.sales_invoice
		FROM `tabRent Schedule` rs
		WHERE {where}
		ORDER BY rs.tenant, rs.due_date
	""", values, as_dict=True)

	return columns, data
