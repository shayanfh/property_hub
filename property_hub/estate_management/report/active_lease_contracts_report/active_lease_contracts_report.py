import frappe


def execute(filters=None):
	filters = filters or {}
	columns = [
		{"label": "Contract", "fieldname": "name", "fieldtype": "Link", "options": "Lease Contract", "width": 150},
		{"label": "Tenant", "fieldname": "tenant", "fieldtype": "Link", "options": "Customer", "width": 150},
		{"label": "Property", "fieldname": "property", "fieldtype": "Link", "options": "Property", "width": 150},
		{"label": "Unit", "fieldname": "unit", "fieldtype": "Link", "options": "Property Unit", "width": 120},
		{"label": "Start Date", "fieldname": "start_date", "fieldtype": "Date", "width": 110},
		{"label": "End Date", "fieldname": "end_date", "fieldtype": "Date", "width": 110},
		{"label": "Rent Amount", "fieldname": "rent_amount", "fieldtype": "Currency", "width": 120},
		{"label": "Payment Frequency", "fieldname": "payment_frequency", "fieldtype": "Data", "width": 130},
		{"label": "Security Deposit", "fieldname": "security_deposit", "fieldtype": "Currency", "width": 130},
	]

	where = "lc.status = 'Active' AND lc.docstatus = 1"
	values = {}
	if filters.get("tenant"):
		where += " AND lc.tenant = %(tenant)s"
		values["tenant"] = filters["tenant"]
	if filters.get("property"):
		where += " AND lc.property = %(property)s"
		values["property"] = filters["property"]

	data = frappe.db.sql(f"""
		SELECT lc.name, lc.tenant, lc.property, lc.unit,
			   lc.start_date, lc.end_date, lc.rent_amount,
			   lc.payment_frequency, lc.security_deposit
		FROM `tabLease Contract` lc
		WHERE {where}
		ORDER BY lc.end_date
	""", values, as_dict=True)

	return columns, data
