import frappe


def execute(filters=None):
	filters = filters or {}
	columns = [
		{"label": "Owner", "fieldname": "owner", "fieldtype": "Link", "options": "Property Owner", "width": 160},
		{"label": "Property", "fieldname": "property_name", "fieldtype": "Link", "options": "Property", "width": 180},
		{"label": "Property Code", "fieldname": "property_code", "fieldtype": "Data", "width": 120},
		{"label": "City", "fieldname": "city", "fieldtype": "Data", "width": 100},
		{"label": "Property Type", "fieldname": "property_type", "fieldtype": "Data", "width": 120},
		{"label": "Total Units", "fieldname": "total_units", "fieldtype": "Int", "width": 100},
		{"label": "Available", "fieldname": "available_units", "fieldtype": "Int", "width": 90},
		{"label": "Rented", "fieldname": "rented_units", "fieldtype": "Int", "width": 90},
		{"label": "Monthly Revenue", "fieldname": "monthly_revenue", "fieldtype": "Currency", "width": 140},
	]

	where = "1=1"
	values = {}
	if filters.get("owner"):
		where += " AND p.owner = %(owner)s"
		values["owner"] = filters["owner"]

	data = frappe.db.sql(f"""
		SELECT
			p.owner,
			p.name AS property_name,
			p.property_code,
			p.city,
			p.property_type,
			COUNT(pu.name) AS total_units,
			SUM(CASE WHEN pu.status = 'Available' THEN 1 ELSE 0 END) AS available_units,
			SUM(CASE WHEN pu.status = 'Rented' THEN 1 ELSE 0 END) AS rented_units,
			SUM(CASE WHEN pu.status = 'Rented' THEN pu.rent_amount ELSE 0 END) AS monthly_revenue
		FROM `tabProperty` p
		LEFT JOIN `tabProperty Unit` pu ON pu.property = p.name
		WHERE {where}
		GROUP BY p.name
		ORDER BY p.owner, p.name
	""", values, as_dict=True)

	return columns, data
