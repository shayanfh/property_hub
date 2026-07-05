"""
Run via: bench --site your-site execute property_hub.estate_management.setup.setup_demo_data.setup
"""
import frappe
from frappe.utils import today, add_months, add_days, getdate
import random


OWNERS = [
	{"owner_name": "Ahmed Al-Rashidi", "phone": "+965-9911-2233", "email": "ahmed.rashidi@demo.com", "nationality": "Kuwaiti", "civil_id": "287061234567"},
	{"owner_name": "Sara Al-Mutairi", "phone": "+965-9922-3344", "email": "sara.mutairi@demo.com", "nationality": "Kuwaiti", "civil_id": "291071234568"},
	{"owner_name": "Gulf Properties LLC", "phone": "+965-2234-5566", "email": "info@gulfproperties.demo", "nationality": "Company", "civil_id": ""},
]

PROPERTIES = [
	{"property_name": "Al-Noor Tower", "property_code": "ANT-001", "owner_index": 0, "property_type": "Residential", "address": "Block 5, Al-Salmiya", "city": "Salmiya"},
	{"property_name": "Gulf Commercial Center", "property_code": "GCC-001", "owner_index": 2, "property_type": "Commercial", "address": "Abdullah Al-Salem, Block 3", "city": "Kuwait City"},
	{"property_name": "Marina Residences", "property_code": "MR-001", "owner_index": 1, "property_type": "Residential", "address": "Marina District, Block 2", "city": "Salmiya"},
	{"property_name": "Jabriya Villas Complex", "property_code": "JVC-001", "owner_index": 0, "property_type": "Residential", "address": "Block 11, Jabriya", "city": "Jabriya"},
	{"property_name": "Al-Rai Warehouse Park", "property_code": "AWP-001", "owner_index": 2, "property_type": "Warehouse", "address": "Industrial Zone, Al-Rai", "city": "Al-Rai"},
]

UNITS = [
	# Al-Noor Tower (index 0)
	{"unit_number": "101", "prop_index": 0, "floor": 1, "unit_type": "2 Bedroom", "rent_amount": 450, "bedrooms": 2, "bathrooms": 2, "area": 120},
	{"unit_number": "102", "prop_index": 0, "floor": 1, "unit_type": "1 Bedroom", "rent_amount": 280, "bedrooms": 1, "bathrooms": 1, "area": 75},
	{"unit_number": "201", "prop_index": 0, "floor": 2, "unit_type": "3 Bedroom", "rent_amount": 650, "bedrooms": 3, "bathrooms": 2, "area": 160},
	# Gulf Commercial Center (index 1)
	{"unit_number": "G01", "prop_index": 1, "floor": 0, "unit_type": "Shop", "rent_amount": 800, "bedrooms": 0, "bathrooms": 1, "area": 60},
	{"unit_number": "G02", "prop_index": 1, "floor": 0, "unit_type": "Office", "rent_amount": 1200, "bedrooms": 0, "bathrooms": 2, "area": 150},
	# Marina Residences (index 2)
	{"unit_number": "A101", "prop_index": 2, "floor": 1, "unit_type": "2 Bedroom", "rent_amount": 550, "bedrooms": 2, "bathrooms": 2, "area": 130},
	{"unit_number": "A102", "prop_index": 2, "floor": 1, "unit_type": "Studio", "rent_amount": 200, "bedrooms": 0, "bathrooms": 1, "area": 45},
	{"unit_number": "B201", "prop_index": 2, "floor": 2, "unit_type": "Penthouse", "rent_amount": 1500, "bedrooms": 4, "bathrooms": 3, "area": 250},
	# Jabriya Villas (index 3)
	{"unit_number": "V01", "prop_index": 3, "floor": 1, "unit_type": "4 Bedroom", "rent_amount": 900, "bedrooms": 4, "bathrooms": 3, "area": 280},
	{"unit_number": "V02", "prop_index": 3, "floor": 1, "unit_type": "3 Bedroom", "rent_amount": 700, "bedrooms": 3, "bathrooms": 2, "area": 200},
	# Al-Rai Warehouse (index 4)
	{"unit_number": "W01", "prop_index": 4, "floor": 0, "unit_type": "Warehouse", "rent_amount": 600, "bedrooms": 0, "bathrooms": 1, "area": 400},
	{"unit_number": "W02", "prop_index": 4, "floor": 0, "unit_type": "Warehouse", "rent_amount": 500, "bedrooms": 0, "bathrooms": 1, "area": 300},
	{"unit_number": "W03", "prop_index": 4, "floor": 0, "unit_type": "Warehouse", "rent_amount": 400, "bedrooms": 0, "bathrooms": 0, "area": 200},
	{"unit_number": "W04", "prop_index": 4, "floor": 0, "unit_type": "Warehouse", "rent_amount": 350, "bedrooms": 0, "bathrooms": 0, "area": 150},
	{"unit_number": "W05", "prop_index": 4, "floor": 0, "unit_type": "Warehouse", "rent_amount": 300, "bedrooms": 0, "bathrooms": 0, "area": 120},
]

TENANTS = [
	{"customer_name": "Mohammed Al-Osaimi", "customer_group": "Individual", "territory": "Kuwait", "civil_id": "298101234560", "tenant_type": "Individual"},
	{"customer_name": "Fatima Al-Ajmi", "customer_group": "Individual", "territory": "Kuwait", "civil_id": "295081234561", "tenant_type": "Individual"},
	{"customer_name": "Kuwait Tech Solutions W.L.L.", "customer_group": "Commercial", "territory": "Kuwait", "civil_id": "", "tenant_type": "Corporate"},
	{"customer_name": "Nasser Al-Shammari", "customer_group": "Individual", "territory": "Kuwait", "civil_id": "291041234562", "tenant_type": "Individual"},
	{"customer_name": "Gulf Trading Co.", "customer_group": "Commercial", "territory": "Kuwait", "civil_id": "", "tenant_type": "Corporate"},
	{"customer_name": "Layla Al-Kandari", "customer_group": "Individual", "territory": "Kuwait", "civil_id": "300021234563", "tenant_type": "Individual"},
	{"customer_name": "Ali Al-Enezi", "customer_group": "Individual", "territory": "Kuwait", "civil_id": "297071234564", "tenant_type": "Individual"},
	{"customer_name": "Pearls Import & Export", "customer_group": "Commercial", "territory": "Kuwait", "civil_id": "", "tenant_type": "Corporate"},
	{"customer_name": "Hessa Al-Fahad", "customer_group": "Individual", "territory": "Kuwait", "civil_id": "302031234565", "tenant_type": "Individual"},
	{"customer_name": "Blue Sky Logistics", "customer_group": "Commercial", "territory": "Kuwait", "civil_id": "", "tenant_type": "Corporate"},
]

LEASE_CONTRACTS = [
	{"tenant_index": 0, "unit_index": 0, "start_months_ago": 6, "duration_months": 12},
	{"tenant_index": 1, "unit_index": 1, "start_months_ago": 3, "duration_months": 12},
	{"tenant_index": 2, "unit_index": 3, "start_months_ago": 8, "duration_months": 12},
	{"tenant_index": 3, "unit_index": 5, "start_months_ago": 4, "duration_months": 12},
	{"tenant_index": 4, "unit_index": 10, "start_months_ago": 2, "duration_months": 12},
	{"tenant_index": 5, "unit_index": 8, "start_months_ago": 12, "duration_months": 24},
	{"tenant_index": 6, "unit_index": 9, "start_months_ago": 5, "duration_months": 12},
	{"tenant_index": 9, "unit_index": 11, "start_months_ago": 1, "duration_months": 12},
]

MAINTENANCE_REQUESTS = [
	{"unit_index": 0, "tenant_index": 0, "issue_type": "Plumbing", "priority": "High", "status": "Completed", "estimated_cost": 150, "actual_cost": 180, "desc": "Leaking pipe under kitchen sink."},
	{"unit_index": 1, "tenant_index": 1, "issue_type": "Electrical", "priority": "Urgent", "status": "In Progress", "estimated_cost": 300, "actual_cost": None, "desc": "Power outage in bedroom outlets."},
	{"unit_index": 3, "tenant_index": 2, "issue_type": "HVAC", "priority": "Medium", "status": "Open", "estimated_cost": 500, "actual_cost": None, "desc": "AC unit not cooling properly in main office."},
	{"unit_index": 5, "tenant_index": 3, "issue_type": "Appliance", "priority": "Low", "status": "Assigned", "estimated_cost": 80, "actual_cost": None, "desc": "Dishwasher making noise."},
	{"unit_index": 8, "tenant_index": 5, "issue_type": "Structural", "priority": "High", "status": "Completed", "estimated_cost": 2000, "actual_cost": 1850, "desc": "Crack in balcony wall - needs sealing."},
	{"unit_index": 10, "tenant_index": 4, "issue_type": "Cleaning", "priority": "Low", "status": "Completed", "estimated_cost": 200, "actual_cost": 200, "desc": "Deep cleaning needed before new tenant move-in."},
]


def setup():
	frappe.flags.ignore_account_permission = True
	print("Setting up Property Hub demo data...")

	owner_names = _create_owners()
	property_names = _create_properties(owner_names)
	unit_names = _create_units(property_names)
	tenant_names = _create_tenants()
	_create_lease_contracts(tenant_names, owner_names, property_names, unit_names)
	_create_maintenance_requests(property_names, unit_names, tenant_names)

	frappe.db.commit()
	print("Demo data setup complete!")


def _create_owners():
	names = []
	for o in OWNERS:
		if frappe.db.exists("Property Owner", o["owner_name"]):
			names.append(o["owner_name"])
			continue
		doc = frappe.get_doc({"doctype": "Property Owner", **o})
		doc.insert(ignore_permissions=True)
		names.append(doc.name)
		print(f"  Created owner: {doc.name}")
	return names


def _create_properties(owner_names):
	names = []
	for p in PROPERTIES:
		prop_code = p["property_code"]
		if frappe.db.exists("Property", prop_code):
			names.append(prop_code)
			continue
		doc = frappe.get_doc({
			"doctype": "Property",
			"property_name": p["property_name"],
			"property_code": p["property_code"],
			"owner": owner_names[p["owner_index"]],
			"property_type": p["property_type"],
			"address": p["address"],
			"city": p["city"],
			"status": "Available",
		})
		doc.insert(ignore_permissions=True)
		names.append(doc.name)
		print(f"  Created property: {doc.name}")
	return names


def _create_units(property_names):
	names = []
	for u in UNITS:
		prop = property_names[u["prop_index"]]
		existing = frappe.db.get_value("Property Unit", {"property": prop, "unit_number": u["unit_number"]}, "name")
		if existing:
			names.append(existing)
			continue
		doc = frappe.get_doc({
			"doctype": "Property Unit",
			"unit_number": u["unit_number"],
			"property": prop,
			"floor": u["floor"],
			"unit_type": u["unit_type"],
			"rent_amount": u["rent_amount"],
			"bedrooms": u["bedrooms"],
			"bathrooms": u["bathrooms"],
			"area": u["area"],
			"status": "Available",
		})
		doc.insert(ignore_permissions=True)
		names.append(doc.name)
		print(f"  Created unit: {doc.name}")
	return names


def _create_tenants():
	names = []
	cg_map = {"Individual": "Individual", "Commercial": "Commercial"}
	default_cg = frappe.db.get_single_value("Selling Settings", "customer_group") or "All Customer Groups"

	for t in TENANTS:
		cg = t["customer_group"]
		if not frappe.db.exists("Customer Group", cg):
			cg = default_cg
		existing = frappe.db.get_value("Customer", {"customer_name": t["customer_name"]}, "name")
		if existing:
			names.append(existing)
			continue
		doc = frappe.get_doc({
			"doctype": "Customer",
			"customer_name": t["customer_name"],
			"customer_group": cg,
			"territory": t.get("territory", "Kuwait"),
			"customer_type": "Individual" if t["tenant_type"] == "Individual" else "Company",
		})
		doc.insert(ignore_permissions=True)
		if t.get("civil_id"):
			frappe.db.set_value("Customer", doc.name, "civil_id", t["civil_id"])
		frappe.db.set_value("Customer", doc.name, "tenant_type", t["tenant_type"])
		names.append(doc.name)
		print(f"  Created tenant: {doc.name}")
	return names


def _create_lease_contracts(tenant_names, owner_names, property_names, unit_names):
	company = frappe.defaults.get_user_default("Company") or frappe.db.get_single_value("Global Defaults", "default_company")

	for lc_data in LEASE_CONTRACTS:
		tenant = tenant_names[lc_data["tenant_index"]]
		unit = unit_names[lc_data["unit_index"]]
		prop_index = UNITS[lc_data["unit_index"]]["prop_index"]
		prop = property_names[prop_index]
		owner_index = PROPERTIES[prop_index]["owner_index"]
		owner = owner_names[owner_index]
		unit_data = UNITS[lc_data["unit_index"]]

		start_date = add_months(today(), -lc_data["start_months_ago"])
		end_date = add_months(start_date, lc_data["duration_months"])

		existing = frappe.db.get_value("Lease Contract", {"tenant": tenant, "unit": unit, "docstatus": 1}, "name")
		if existing:
			continue

		lc = frappe.get_doc({
			"doctype": "Lease Contract",
			"tenant": tenant,
			"owner": owner,
			"property": prop,
			"unit": unit,
			"start_date": start_date,
			"end_date": end_date,
			"rent_amount": unit_data["rent_amount"],
			"payment_frequency": "Monthly",
			"security_deposit": unit_data["rent_amount"],
			"status": "Draft",
		})
		lc.insert(ignore_permissions=True)
		lc.submit()
		print(f"  Created lease contract: {lc.name} for {tenant}")

		_pay_past_schedules(lc.name, lc_data["start_months_ago"], company)


def _pay_past_schedules(lease_contract, months_paid, company):
	past_due = frappe.get_all(
		"Rent Schedule",
		filters={
			"lease_contract": lease_contract,
			"due_date": ["<=", today()],
			"payment_status": "Unpaid",
		},
		fields=["name", "amount", "tenant", "due_date"],
		order_by="due_date asc",
		limit=months_paid - 1,
	)
	for rs in past_due:
		from property_hub.estate_management.doctype.rent_schedule.rent_schedule import create_invoice_for_schedule
		try:
			inv_name = create_invoice_for_schedule(rs.name)
			if inv_name:
				inv = frappe.get_doc("Sales Invoice", inv_name)
				inv.submit()
				frappe.db.set_value("Rent Schedule", rs.name, "payment_status", "Paid")
		except Exception as e:
			print(f"    Warning: could not create invoice for {rs.name}: {e}")


def _create_maintenance_requests(property_names, unit_names, tenant_names):
	for mr_data in MAINTENANCE_REQUESTS:
		unit = unit_names[mr_data["unit_index"]]
		prop_index = UNITS[mr_data["unit_index"]]["prop_index"]
		prop = property_names[prop_index]
		tenant = tenant_names[mr_data["tenant_index"]]

		existing = frappe.db.get_value("Maintenance Request", {"unit": unit, "issue_type": mr_data["issue_type"], "status": mr_data["status"]}, "name")
		if existing:
			continue

		doc = frappe.get_doc({
			"doctype": "Maintenance Request",
			"property": prop,
			"unit": unit,
			"tenant": tenant,
			"issue_type": mr_data["issue_type"],
			"priority": mr_data["priority"],
			"status": mr_data["status"],
			"description": mr_data["desc"],
			"estimated_cost": mr_data["estimated_cost"],
			"actual_cost": mr_data.get("actual_cost"),
		})
		doc.insert(ignore_permissions=True)
		print(f"  Created maintenance request: {doc.name}")
