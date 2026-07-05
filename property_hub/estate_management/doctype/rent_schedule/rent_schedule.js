frappe.ui.form.on('Rent Schedule', {
	refresh(frm) {
		if (!frm.is_new() && frm.doc.payment_status !== 'Paid' && !frm.doc.sales_invoice) {
			frm.add_custom_button(__('Create Invoice'), () => {
				frappe.call({
					method: 'property_hub.estate_management.doctype.rent_schedule.rent_schedule.create_invoice_for_schedule',
					args: { rent_schedule: frm.doc.name },
					callback(r) {
						if (r.message) {
							frappe.msgprint(__('Invoice created: ') + r.message);
							frm.reload_doc();
						}
					}
				});
			});
		}
		if (frm.doc.sales_invoice) {
			frm.add_custom_button(__('View Invoice'), () => {
				frappe.set_route('Form', 'Sales Invoice', frm.doc.sales_invoice);
			}, __('Links'));
		}
	}
});
