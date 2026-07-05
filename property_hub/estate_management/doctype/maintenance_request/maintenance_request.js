frappe.ui.form.on('Maintenance Request', {
	refresh(frm) {
		if (frm.doc.purchase_invoice) {
			frm.add_custom_button(__('View Purchase Invoice'), () => {
				frappe.set_route('Form', 'Purchase Invoice', frm.doc.purchase_invoice);
			}, __('Links'));
		}
		if (frm.doc.status === 'Completed' && !frm.doc.purchase_invoice && !frm.is_new()) {
			frm.add_custom_button(__('Create Purchase Invoice'), () => {
				frappe.new_doc('Purchase Invoice', {
					remarks: `Maintenance for ${frm.doc.property} - ${frm.doc.unit || ''}`,
				});
			});
		}
	},
	unit(frm) {
		if (frm.doc.unit) {
			frappe.db.get_value('Property Unit', frm.doc.unit, 'property', (r) => {
				if (r && r.property) frm.set_value('property', r.property);
			});
		}
	}
});
