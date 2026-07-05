app_name = "property_hub"
app_title = "Property Hub"
app_publisher = "Mozaicweb"
app_description = "Real Estate and Property Management for ERPNext"
app_email = "abdullahs@mozaicweb.com"
app_license = "mit"
app_version = "0.0.1"

required_apps = ["erpnext"]

# Fixtures - custom fields installed on bench migrate
fixtures = [
	{"dt": "Custom Field", "filters": [["module", "=", "Property Hub"]]},
]

# Document Events
doc_events = {
	"Lease Contract": {
		"on_submit": "property_hub.estate_management.doctype.lease_contract.lease_contract.on_submit_generate_rent_schedule",
		"on_cancel": "property_hub.estate_management.doctype.lease_contract.lease_contract.on_cancel_rent_schedule",
	},
	"Payment Entry": {
		"on_submit": "property_hub.estate_management.doctype.rent_schedule.rent_schedule.update_payment_status_from_payment_entry",
		"on_cancel": "property_hub.estate_management.doctype.rent_schedule.rent_schedule.revert_payment_status_from_payment_entry",
	},
	"Sales Invoice": {
		"on_submit": "property_hub.estate_management.doctype.rent_schedule.rent_schedule.link_sales_invoice_to_schedule",
	},
}

# Scheduled Tasks
scheduler_events = {
	"daily": [
		"property_hub.estate_management.doctype.rent_schedule.rent_schedule.mark_overdue_schedules",
		"property_hub.estate_management.doctype.lease_contract.lease_contract.update_expired_contracts",
	],
}

# Installation hooks
after_install = "property_hub.estate_management.setup.install.after_install"
