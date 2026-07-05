import frappe
from frappe.utils import today, get_first_day, get_last_day


def execute(filters=None):
	filters = filters or {}
	from_date = filters.get("from_date") or get_first_day(today())
	to_date = filters.get("to_date") or get_last_day(today())

	columns = [
		{"label": "Property", "fieldname": "property", "fieldtype": "Link", "options": "Property", "width": 180},
		{"label": "Month", "fieldname": "month_year", "fieldtype": "Data", "width": 100},
		{"label": "Expected", "fieldname": "expected", "fieldtype": "Currency", "width": 130},
		{"label": "Collected", "fieldname": "collected", "fieldtype": "Currency", "width": 130},
		{"label": "Outstanding", "fieldname": "outstanding", "fieldtype": "Currency", "width": 130},
		{"label": "Collection %", "fieldname": "collection_pct", "fieldtype": "Percent", "width": 110},
	]

	data = frappe.db.sql("""
		SELECT
			rs.property,
			DATE_FORMAT(rs.due_date, '%%Y-%%m') AS month_year,
			SUM(rs.amount) AS expected,
			SUM(CASE WHEN rs.payment_status = 'Paid' THEN rs.amount ELSE 0 END) AS collected,
			SUM(CASE WHEN rs.payment_status != 'Paid' THEN rs.amount ELSE 0 END) AS outstanding,
			ROUND(100.0 * SUM(CASE WHEN rs.payment_status = 'Paid' THEN rs.amount ELSE 0 END)
				/ NULLIF(SUM(rs.amount), 0), 1) AS collection_pct
		FROM `tabRent Schedule` rs
		WHERE rs.due_date BETWEEN %(from_date)s AND %(to_date)s
		GROUP BY rs.property, month_year
		ORDER BY rs.property, month_year
	""", {"from_date": from_date, "to_date": to_date}, as_dict=True)

	return columns, data
